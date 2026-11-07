#!/usr/bin/env python3
"""Import exact PMC article PDFs only after metadata, DOI, licence and credit-line checks.

Uses NCBI's official PMC Article Datasets Cloud Service on AWS. This is a
fail-closed importer: unknown licence, wrong DOI/version, unavailable PDF, or
possible third-party credit line means no repository copy is made.
"""
from __future__ import annotations
import argparse, csv, hashlib, io, json, re, sys, xml.etree.ElementTree as ET
from datetime import date
from pathlib import Path
from urllib.parse import urlparse
import requests
from pypdf import PdfReader

BUCKET = "https://pmc-oa-opendata.s3.amazonaws.com"
OUT = Path("sources/open-access")
MANIFEST = OUT / "manifest.csv"
LICENSES = {
    "CC BY": ("Creative Commons Attribution 4.0 International (CC BY 4.0)", "https://creativecommons.org/licenses/by/4.0/", "commercial and non-commercial redistribution permitted with attribution"),
    "CC BY 4.0": ("Creative Commons Attribution 4.0 International (CC BY 4.0)", "https://creativecommons.org/licenses/by/4.0/", "commercial and non-commercial redistribution permitted with attribution"),
    "CC BY-NC": ("Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)", "https://creativecommons.org/licenses/by-nc/4.0/", "non-commercial redistribution only; attribution required"),
    "CC BY-NC 4.0": ("Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)", "https://creativecommons.org/licenses/by-nc/4.0/", "non-commercial redistribution only; attribution required"),
    "CC BY-NC-ND": ("Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)", "https://creativecommons.org/licenses/by-nc-nd/4.0/", "non-commercial redistribution of unchanged file only; no derivatives"),
    "CC BY-NC-ND 4.0": ("Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)", "https://creativecommons.org/licenses/by-nc-nd/4.0/", "non-commercial redistribution of unchanged file only; no derivatives"),
}
CANDIDATES = [
 {"id":"DOM-061","pmcid":"PMC11907869","doi":"10.1186/s40560-025-00776-0","year":"2025","issuer":"Japanese Society of Intensive Care Medicine; Japanese Association for Acute Medicine","title":"The Japanese Clinical Practice Guidelines for Management of Sepsis and Septic Shock 2024","source":"https://link.springer.com/article/10.1186/s40560-025-00776-0"},
 {"id":"DOM-062","pmcid":"PMC10629099","doi":"10.1186/s40560-023-00697-w","year":"2023","issuer":"Japanese Society of Intensive Care Medicine","title":"Japanese Clinical Practice Guidelines for Rehabilitation in Critically Ill Patients 2023 (J-ReCIP 2023)","source":"https://link.springer.com/article/10.1186/s40560-023-00697-w"},
 {"id":"DOM-063","pmcid":"PMC11369916","doi":"10.5005/jp-journals-10071-24682","year":"2024","issuer":"Indian Society of Critical Care Medicine","title":"The Indian Society of Critical Care Medicine Position Statement on the Management of Sepsis in Resource-limited Settings","source":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11369916/"},
 {"id":"DOM-064","pmcid":"PMC11369924","doi":"10.5005/jp-journals-10071-24747","year":"2024","issuer":"Indian Society of Critical Care Medicine","title":"ISCCM Position Statement on the Management of Invasive Fungal Infections in the Intensive Care Unit","source":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11369924/"},
 {"id":"DOM-065","pmcid":"PMC11369922","doi":"10.5005/jp-journals-10071-24748","year":"2024","issuer":"Indian Society of Critical Care Medicine","title":"ISCCM Position Statement: Management of Severe Dengue in Intensive Care Unit","source":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11369922/"},
 {"id":"DOM-066","pmcid":"PMC11369926","doi":"10.5005/jp-journals-10071-24765","year":"2024","issuer":"Indian Society of Critical Care Medicine","title":"ISCCM Position Statement on the Management of Severe Malaria in Intensive Care Unit","source":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11369926/"},
 {"id":"DOM-067","pmcid":"PMC11369919","doi":"10.5005/jp-journals-10071-24783","year":"2024","issuer":"Indian Society of Critical Care Medicine","title":"ISCCM Position Statement on the Approach to and Management of Critically Ill Patients with Tuberculosis","source":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11369919/"},
 {"id":"DOM-070","pmcid":"PMC12883282","doi":"10.1111/aas.70201","year":"2026","issuer":"Saudi Critical Care Society; Scandinavian Society of Anaesthesiology and Intensive Care Medicine; endorsed by Kuwait Anesthesia and Critical Care Society","title":"Recommendations for Stress Ulcer Prophylaxis in Critically Ill Adults: A Contextualized Clinical Practice Guideline","source":"https://onlinelibrary.wiley.com/doi/10.1111/aas.70201"},
]
FIELDS=["guideline_id","pdf_path","doi","issuing_organisations","publication_year","version_edition","original_source_url","access_date","licence_name_version","licence_url","attribution_copyright_notice","redistribution_basis","rights_evidence_url","notes","sha256"]
SUSPICIOUS=re.compile(r"reproduced\\s+with\\s+permission|adapted\\s+from|courtesy\\s+of|used\\s+with\\s+permission|copyright\\s*[©(]|all rights reserved|permission from|not covered by (?:the )?(?:article )?licen[cs]e",re.I)

def get(url):
 r=requests.get(url,timeout=90,headers={"User-Agent":"GCCGRD research repository; NCBI PMC OA Cloud Service"})
 r.raise_for_status()
 return r

def https_url(u):
 if u.startswith("s3://"):
  bucket,key=u[5:].split("/",1)
  return f"https://{bucket}.s3.amazonaws.com/{key}"
 return u

def metadata_versions(pmcid):
 # New PMC Cloud Service keeps per-version JSON files under metadata/.
 r=get(f"{BUCKET}/?list-type=2&prefix=metadata/{pmcid}.")
 root=ET.fromstring(r.content)
 ns={"s3":"http://s3.amazonaws.com/doc/2006-03-01/"}
 keys=[e.text for e in root.findall(".//s3:Contents/s3:Key",ns) if e.text and e.text.endswith(".json")]
 if not keys: raise RuntimeError("No per-version PMC Cloud metadata JSON found")
 found=[]
 for key in keys:
  m=get(f"{BUCKET}/{key}").json()
  if (m.get("doi") or "").lower()==next(c["doi"].lower() for c in CANDIDATES if c["pmcid"]==pmcid):
   if not m.get("is_manuscript",False): found.append((key,m))
 if not found: raise RuntimeError("No matching DOI publisher-version metadata found (author manuscript excluded)")
 return found[-1]

def scan_xml(xml):
 root=ET.fromstring(xml)
 hits=[]
 for el in root.iter():
  tag=el.tag.rsplit("}",1)[-1]
  if tag not in ("fig","table-wrap","supplementary-material"):
   continue
  s=" ".join(" ".join(el.itertext()).split())
  if SUSPICIOUS.search(s): hits.append(f"{tag}: {s[:500]}")
 return hits

def load_manifest():
 if not MANIFEST.exists(): return []
 with MANIFEST.open(newline="",encoding="utf-8") as f: return list(csv.DictReader(f))

def main():
 p=argparse.ArgumentParser()
 p.add_argument("--allow-noncommercial",action="store_true",help="Allow CC BY-NC / CC BY-NC-ND files for non-commercial redistribution")
 args=p.parse_args()
 OUT.mkdir(parents=True,exist_ok=True)
 rows=load_manifest(); existing={r.get("guideline_id") for r in rows}
 imported=0; skipped=[]
 for c in CANDIDATES:
  if c["id"] in existing:
   print(f"SKIP {c['id']}: already in manifest"); continue
  try:
   key,meta=metadata_versions(c["pmcid"])
   lic=str(meta.get("license_code") or "").strip().upper()
   if lic not in LICENSES: raise RuntimeError(f"Unrecognised or restrictive licence code: {lic!r}")
   if lic.startswith("CC BY-NC") and not args.allow_noncommercial:
    raise RuntimeError(f"{lic}: requires explicit non-commercial redistribution approval")
   if not meta.get("pdf_url") or not meta.get("xml_url"): raise RuntimeError("No PMC Cloud PDF/XML object URLs")
   xml=get(https_url(meta["xml_url"])).content
   flags=scan_xml(xml)
   if flags: raise RuntimeError("Possible third-party credit/exclusion requires manual review: "+" | ".join(flags[:3]))
   pdf=get(https_url(meta["pdf_url"])).content
   if not pdf.startswith(b"%PDF-"): raise RuntimeError("PDF object signature invalid")
   reader=PdfReader(io.BytesIO(pdf),strict=False)
   if len(reader.pages)<2: raise RuntimeError(f"Unexpected PDF length: {len(reader.pages)} page(s)")
   pdf_text=" ".join((page.extract_text() or "") for page in reader.pages)
   pdf_flags=SUSPICIOUS.findall(pdf_text)
   if pdf_flags: raise RuntimeError("Possible third-party credit/exclusion detected in PDF text: "+", ".join(sorted(set(pdf_flags))))
   filename=f"{c['id']}_{c['year']}_{c['pmcid']}.pdf"; path=OUT/filename
   path.write_bytes(pdf); sha=hashlib.sha256(pdf).hexdigest()
   lname,lurl,basis=LICENSES[lic]
   rows.append({"guideline_id":c["id"],"pdf_path":str(path),"doi":c["doi"],"issuing_organisations":c["issuer"],"publication_year":c["year"],"version_edition":f"PMC Cloud publisher version; metadata object {key}","original_source_url":c["source"],"access_date":date.today().isoformat(),"licence_name_version":lname,"licence_url":lurl,"attribution_copyright_notice":f"{c['title']}; DOI {c['doi']}; cite and attribute original authors/publisher","redistribution_basis":basis,"rights_evidence_url":lurl,"notes":f"Exact DOI matched; author manuscript excluded; PMC XML figure/table/supplementary credit scan and extracted PDF text scan found no obvious third-party permission/reuse exclusions; {len(reader.pages)} pages. Automated text scans cannot rule out image-only credit notices; retain original unchanged and perform human spot-check before public release.","sha256":sha})
   imported+=1; print(f"IMPORTED {c['id']} ({lic}), {len(reader.pages)} pages, sha256={sha}")
  except Exception as e:
   skipped.append((c["id"],str(e))); print(f"SKIPPED {c['id']}: {e}")
 if imported:
  with MANIFEST.open("w",newline="",encoding="utf-8") as f:
   w=csv.DictWriter(f,fieldnames=FIELDS); w.writeheader()
   for row in rows: w.writerow({k:row.get(k,"") for k in FIELDS})
 print(f"Imported {imported}; skipped {len(skipped)}; manifest entries {len(rows)}")
 if skipped:
  print("Manual follow-up required:")
  for gid,reason in skipped: print(f"  {gid}: {reason}")

if __name__=="__main__": main()

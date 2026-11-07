#!/usr/bin/env python3
"""Fetch exact PMC article PDFs from the official PMC AWS dataset, validate rights,
check figure/table credit lines for obvious third-party exclusions, and build manifest.
This is deliberately fail-closed: uncertain rights or third-party credits are skipped.
"""
from __future__ import annotations
import argparse, csv, hashlib, io, json, os, re, sys, xml.etree.ElementTree as ET
from datetime import date
from pathlib import Path
from urllib.parse import urlparse
import requests
from pypdf import PdfReader

BUCKET = "https://pmc-oa-opendata.s3.amazonaws.com"
OUT = Path("sources/open-access")
MANIFEST = OUT / "manifest.csv"
LICENSE_URLS = {
    "CC BY": "https://creativecommons.org/licenses/by/4.0/",
    "CC BY 4.0": "https://creativecommons.org/licenses/by/4.0/",
    "CC BY-NC": "https://creativecommons.org/licenses/by-nc/4.0/",
    "CC BY-NC 4.0": "https://creativecommons.org/licenses/by-nc/4.0/",
}
CANDIDATES = [
    {"id":"DOM-061","pmcid":"PMC11907869","doi":"10.1186/s40560-025-00776-0","title":"The Japanese Clinical Practice Guidelines for Management of Sepsis and Septic Shock 2024","year":"2025","issuer":"Japanese Society of Intensive Care Medicine; Japanese Association for Acute Medicine","source":"https://link.springer.com/article/10.1186/s40560-025-00776-0"},
    {"id":"DOM-062","pmcid":"PMC10629099","doi":"10.1186/s40560-023-00697-w","title":"Japanese Clinical Practice Guidelines for Rehabilitation in Critically Ill Patients 2023 (J-ReCIP 2023)","year":"2023","issuer":"Japanese Society of Intensive Care Medicine","source":"https://link.springer.com/article/10.1186/s40560-023-00697-w"},
    {"id":"DOM-063","pmcid":"PMC11369916","doi":"10.5005/jp-journals-10071-24682","title":"The Indian Society of Critical Care Medicine Position Statement on the Management of Sepsis in Resource-limited Settings","year":"2024","issuer":"Indian Society of Critical Care Medicine","source":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11369916/"},
    {"id":"DOM-064","pmcid":"PMC11369924","doi":"10.5005/jp-journals-10071-24747","title":"ISCCM Position Statement on the Management of Invasive Fungal Infections in the Intensive Care Unit","year":"2024","issuer":"Indian Society of Critical Care Medicine","source":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11369924/"},
    {"id":"DOM-065","pmcid":"PMC11369922","doi":"10.5005/jp-journals-10071-24748","title":"ISCCM Position Statement: Management of Severe Dengue in Intensive Care Unit","year":"2024","issuer":"Indian Society of Critical Care Medicine","source":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11369922/"},
    {"id":"DOM-066","pmcid":"PMC11369926","doi":"10.5005/jp-journals-10071-24765","title":"ISCCM Position Statement on the Management of Severe Malaria in Intensive Care Unit","year":"2024","issuer":"Indian Society of Critical Care Medicine","source":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11369926/"},
    {"id":"DOM-067","pmcid":"PMC11369919","doi":"10.5005/jp-journals-10071-24783","title":"ISCCM Position Statement on the Approach to and Management of Critically Ill Patients with Tuberculosis","year":"2024","issuer":"Indian Society of Critical Care Medicine","source":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11369919/"},
    {"id":"DOM-070","pmcid":"PMC12883282","doi":"10.1111/aas.70201","title":"Recommendations for Stress Ulcer Prophylaxis in Critically Ill Adults: A Contextualized Clinical Practice Guideline","year":"2026","issuer":"Saudi Critical Care Society; Scandinavian Society of Anaesthesiology and Intensive Care Medicine; endorsed by Kuwait Anesthesia and Critical Care Society","source":"https://onlinelibrary.wiley.com/doi/10.1111/aas.70201"},
]
FIELDS = ["guideline_id","pdf_path","doi","issuing_organisations","publication_year","version_edition","original_source_url","access_date","licence_name_version","licence_url","attribution_copyright_notice","redistribution_basis","rights_evidence_url","notes","sha256"]

def get(url):
    r = requests.get(url, timeout=90, headers={"User-Agent":"GCCGRD/1.0 (research archive; contact via repository)"})
    r.raise_for_status()
    return r

def version_metadata(pmcid):
    r = get(f"{BUCKET}/?list-type=2&delimiter=%2F&prefix={pmcid}.")
    root = ET.fromstring(r.content)
    ns = {"s3":"http://s3.amazonaws.com/doc/2006-03-01/"}
    versions = sorted({x.text.rstrip("/") for x in root.findall(".//s3:CommonPrefixes/s3:Prefix", ns)})
    if not versions:
        raise RuntimeError(f"No PMC AWS version prefix found for {pmcid}")
    # Select highest version suffix; the DOI check below prevents an incorrect manifestation.
    prefix = versions[-1]
    version = prefix.rsplit(".",1)[-1]
    meta_url = f"{BUCKET}/{prefix}{pmcid}.{version}.json"
    meta = get(meta_url).json()
    return version, meta

def third_party_flags(xml_bytes):
    root = ET.fromstring(xml_bytes)
    flagged=[]
    terms=re.compile(r"reproduced\s+with\s+permission|adapted\s+from|courtesy\s+of|used\s+with\s+permission|copyright\s*[©(]|all rights reserved|permission from",re.I)
    for node in root.iter():
        tag=node.tag.rsplit("}",1)[-1]
        if tag not in ("fig","table-wrap"):
            continue
        text=" ".join(" ".join(node.itertext()).split())
        if terms.search(text):
            flagged.append((tag,text[:600]))
    return flagged

def load_manifest():
    if not MANIFEST.exists():
        return []
    with MANIFEST.open(newline="",encoding="utf-8") as f:
        return list(csv.DictReader(f))

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--allow-noncommercial",action="store_true",help="Explicitly allow CC BY-NC files in this non-commercial research repository")
    args=ap.parse_args()
    OUT.mkdir(parents=True,exist_ok=True)
    rows=load_manifest()
    known={r.get("guideline_id") for r in rows}
    added=0
    for c in CANDIDATES:
        if c["id"] in known:
            print(f"SKIP {c['id']}: already in manifest"); continue
        try:
            version,meta=version_metadata(c["pmcid"])
            doi=(meta.get("doi") or "").lower()
            if doi != c["doi"].lower():
                raise RuntimeError(f"DOI mismatch: PMC metadata says {doi!r}")
            lic=str(meta.get("license_code") or "").strip().upper()
            # PMC machine-readable values are expected to be CC BY, CC BY-NC, etc.
            if lic not in ("CC BY","CC BY 4.0","CC BY-NC","CC BY-NC 4.0"):
                raise RuntimeError(f"Licence not approved/recognised: {lic!r}")
            if lic.startswith("CC BY-NC") and not args.allow_noncommercial:
                raise RuntimeError("CC BY-NC requires explicit --allow-noncommercial approval")
            xml_url=meta.get("xml_url")
            pdf_url=meta.get("pdf_url")
            if not xml_url or not pdf_url:
                raise RuntimeError("PMC metadata does not provide both XML and PDF URLs")
            xml_bytes=get(xml_url).content
            flags=third_party_flags(xml_bytes)
            if flags:
                raise RuntimeError("Possible third-party figure/table credit lines require manual review: "+repr(flags[:4]))
            pdf_bytes=get(pdf_url).content
            if not pdf_bytes.startswith(b"%PDF-"):
                raise RuntimeError("Retrieved object is not a PDF")
            reader=PdfReader(io.BytesIO(pdf_bytes),strict=False)
            if len(reader.pages)<2:
                raise RuntimeError(f"Unexpectedly short PDF ({len(reader.pages)} pages)")
            sha=hashlib.sha256(pdf_bytes).hexdigest()
            filename=f"{c['id']}_{c['year']}_{c['pmcid']}.pdf"
            path=OUT/filename
            path.write_bytes(pdf_bytes)
            license_url=LICENSE_URLS[lic]
            license_name="Creative Commons Attribution 4.0 International (CC BY 4.0)" if lic.startswith("CC BY ") or lic=="CC BY" else "Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)"
            rows.append({
                "guideline_id":c["id"],"pdf_path":str(path),"doi":c["doi"],
                "issuing_organisations":c["issuer"],"publication_year":c["year"],
                "version_edition":f"PMC version {version}; publisher version of record",
                "original_source_url":c["source"],"access_date":date.today().isoformat(),
                "licence_name_version":license_name,"licence_url":license_url,
                "attribution_copyright_notice":f"{c['title']}; DOI: {c['doi']}; attribution to original authors and source required",
                "redistribution_basis":"PMC article-level licence permits redistribution; CC BY-NC file retained only for non-commercial research repository use" if lic.startswith("CC BY-NC") else "PMC article-level CC BY 4.0 licence permits redistribution",
                "rights_evidence_url":license_url,
                "notes":f"Retrieved from official PMC AWS Cloud Service; {len(reader.pages)} PDF pages; XML figure/table credit scan found no obvious third-party permission/reuse exclusions. Manual visual PDF check still required.",
                "sha256":sha
            })
            added+=1
            print(f"ADDED {c['id']} {len(reader.pages)} pages {license_name} sha256={sha}")
        except Exception as e:
            print(f"REVIEW REQUIRED {c['id']}: {e}")
    if added:
        with MANIFEST.open("w",newline="",encoding="utf-8") as f:
            w=csv.DictWriter(f,fieldnames=FIELDS); w.writeheader()
            for r in rows:
                w.writerow({k:r.get(k,"") for k in FIELDS})
    print(f"Completed: {added} PDF(s) added; {len(rows)} manifest record(s) total.")
    # Exit nonzero if any candidates were not safely imported.
    if added < len(CANDIDATES)-len(known):
        sys.exit(2)

if __name__=="__main__":
    main()

# Sedation, analgesia and delirium — historical search log (2000–2026)

**Work-package code:** GCCGRD-PADIS  
**Domain:** `sedation_analgesia_delirium`  
**Search date:** 2026-11-03  
**Coverage:** 2000-01-01 to 2026-11-03; planned end date 2026-12-31.  
**Population:** Adults 18+; mixed-age documents only if adult recommendations can be separately identified.  
**Status:** Initial search protocol created; discovery and screening are incomplete.

## Search concepts

pain; anxiety; agitation; sedation; delirium; sleep disruption; ICU liberation; restraint; neuromuscular blockade.

## Issuing bodies and repositories to search

SCCM; ESICM; American Society of Anesthesiologists; European Society of Anaesthesiology and Intensive Care.

## Reproducible PubMed discovery query

`("adult ICU" OR "critically ill adults") AND (pain OR anxiety OR sedation OR delirium OR sleep) AND (guideline OR focused update OR consensus) AND ("2000/01/01"[Date - Publication] : "2026/11/03"[Date - Publication])`

This is a candidate-discovery query, not a final eligibility filter. Do not use an adult title/abstract filter as a hard exclusion. Search exact issuing-body guideline titles and catalogue entries in parallel; preserve exact query, search date, result count and export file when the database interface permits.

## Other source searches

1. Official guideline archive/catalogue for each issuing body listed above.
2. PubMed and Europe PMC for bibliographic discovery and identifier checks.
3. PMC for full-text candidates; inspect the article's licence statement individually.
4. GIN and WHO repositories where relevant.
5. National/regional authorities and professional societies in each country/region; use local-language terms and record the language searched.
6. Citation chaining from eligible guidelines to earlier editions, focused updates, corrections and formal consensus documents.

## Screening questions

- Is this a formal clinical practice guideline, formal consensus statement/definition, or evidence-based position statement with clinical recommendations?
- Is the issuing body recognised and the development process documented?
- Is the document directly relevant to adult critical care?
- Does it apply to adults aged 18+ or provide separately identifiable adult recommendations?
- Is the complete text publicly readable without payment or login?
- Is the DOI/PMID/PMCID or official document identifier traceable to the same document?
- Is the exact publication date, edition, status and relationship to predecessor/successor documents established?
- Has a second reviewer independently checked eligibility, primary source, full text/access and status?

## Candidate register

Candidate rows for this domain are maintained in `data/screening/sedation-analgesia-delirium_candidates.csv`. Do not promote a candidate to `data/guidelines.csv` until all mandatory criteria and independent review are complete.

## Search audit

| Item | Value |
|---|---|
| Search date | 2026-11-03 |
| Databases/catalogues searched | Initial discovery protocol only |
| Exact result count | Not captured |
| Exported result set | Not yet saved |
| Duplicates removed | Not yet assessed |
| Full texts screened | Not yet assessed |
| Included | Not yet determined |
| Excluded with reasons | Not yet determined |
| Second reviewer | Pending |

## Limitations and next actions

This is an initial domain search protocol, not an exhaustive search or completed systematic review. Exact result counts, exports, screening counts, full-text exclusions and a country-by-country gap audit remain outstanding. Search the entire 2000–2026 historical period, not only the current guideline. Preserve each substantive edition and verify historical status using the issuing body.

## First-pass source checks — 2026-11-03

- SCCM PADIS guideline (2018): DOI 10.1097/CCM.0000000000003299; PMID 30113379. Adult ICU guideline; PubMed identifies a free article and SCCM hosts the official recommendations. It updated the 2013 PAD guideline.
- SCCM PADIS focused update (2025): DOI 10.1097/CCM.0000000000006574; PMID 39982143; Crit Care Med. 2025;53(3):e711-e727; online 2025-02-21. SCCM explicitly describes it as an update/expansion of the 2018 adult ICU guideline. Record separately and map the exact recommendations updated; verify full text and reuse licence.

The 2018 and 2025 records should be linked as an original guideline and focused update, not collapsed into one record.

## Historical candidate expansion — 2026-11-04

- 2002 guideline for sustained use of sedatives and analgesics in critically ill adults: PMID 11826570; PubMed classifies the AJHP publication as a guideline and identifies a free-article route. A parallel Critical Care Medicine publication exists; confirm canonical metadata and avoid double-counting.
- 2002 guideline for sustained neuromuscular blockade in adult critically ill patients: PMID 11826571; AJHP publisher page located, but full freely accessible text not established. A parallel Critical Care Medicine publication exists (PMID 11902255); do not treat parallel publications as distinct guidelines.
- These early documents are important historical baseline candidates preceding PAD/PADIS. Verify full text, exact DOI, licence, recommendations and supersession history before inclusion.

- 2016 SCCM guideline update on sustained neuromuscular blockade: DOI 10.1097/CCM.0000000000002027; PMID 27755068. PubMed describes it as an update to the 2002 adult ICU guideline and confirms GRADE-based methods. Retain 2002 and 2016 as separate editions. A 2017 AJHP executive summary (PMID 28069681) is a companion summary, not another guideline edition.
- The 2002 neuromuscular-blockade guideline's AJHP record is DOI 10.1093/ajhp/59.2.179; PMID 11826571; its parallel Critical Care Medicine paper is DOI 10.1097/00003246-200201000-00021; PMID 11902255.

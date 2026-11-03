# Mobilisation, rehabilitation and recovery — historical search log (2000–2026)

**Work-package code:** GCCGRD-REHAB  
**Domain:** `mobilisation_rehabilitation_and_recovery`  
**Search date:** 2026-11-03  
**Coverage:** 2000-01-01 to 2026-11-03; planned end date 2026-12-31.  
**Population:** Adults 18+; mixed-age documents only if adult recommendations can be separately identified.  
**Status:** Initial search protocol created; discovery and screening are incomplete.

## Search concepts

early mobilisation; ICU rehabilitation; physical therapy; post-intensive care syndrome; survivorship; post-ICU follow-up; weakness; respiratory muscle training.

## Issuing bodies and repositories to search

SCCM; ESICM; ATS; ERS; European Society of Physical and Rehabilitation Medicine (ESPRM); ASSOBRAFIR; NICE; ANZICS.

## Reproducible PubMed discovery query

`(ICU OR "critically ill adults" OR "post-intensive care") AND (mobilisation OR mobilization OR rehabilitation OR survivorship OR recovery) AND (guideline OR consensus) AND ("2000/01/01"[Date - Publication] : "2026/11/03"[Date - Publication])`

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

Candidate rows for this domain are maintained in `data/screening/mobilisation-rehabilitation-and-recovery_candidates.csv`. Do not promote a candidate to `data/guidelines.csv` until all mandatory criteria and independent review are complete.

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

- ATS/CHEST guideline on liberation from mechanical ventilation in critically ill adults (2017): DOI 10.1164/rccm.201610-2075ST; PMID 27762595. Primary publication confirms adult ICU scope and GRADE methodology. Four conditional recommendations include protocolised rehabilitation directed toward early mobilisation and ventilator liberation. Full-text publisher page located; licence and reuse terms need checking.
- A separate executive summary exists (DOI 10.1164/rccm.201610-2076ST; PMID 27762608). Treat it as a companion publication, not a separate guideline edition.
- This domain overlaps with sedation/PADIS and airway/ventilator liberation. Use one canonical guideline record and multiple tags where appropriate; do not duplicate the ATS/CHEST guideline across domains.

The recovery search must continue to include post-intensive-care syndrome, ICU follow-up, long-term physical/cognitive recovery and rehabilitation guidance beyond ventilator liberation.

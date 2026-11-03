# Cardiac critical care — historical search log (2000–2026)

**Work-package code:** GCCGRD-CARD  
**Domain:** `cardiac_critical_care`  
**Search date:** 2026-11-03  
**Coverage:** 2000-01-01 to 2026-11-03; planned end date 2026-12-31.  
**Population:** Adults 18+; mixed-age documents only if adult recommendations can be separately identified.  
**Status:** Initial search protocol created; discovery and screening are incomplete.

## Search concepts

acute coronary syndromes; cardiac arrest; post-resuscitation care; cardiogenic shock; acute heart failure; arrhythmias; mechanical circulatory support.

## Issuing bodies and repositories to search

AHA; ACC; ESC; ERC; ESICM; SCCM; ANZCOR; International Liaison Committee on Resuscitation (ILCOR).

## Reproducible PubMed discovery query

`(cardiac arrest OR "acute coronary syndrome" OR "cardiogenic shock" OR "post-resuscitation") AND (guideline OR consensus) AND (adult OR intensive care) AND ("2000/01/01"[Date - Publication] : "2026/11/03"[Date - Publication])`

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

Candidate rows for this domain are maintained in `data/screening/cardiac-critical-care_candidates.csv`. Do not promote a candidate to `data/guidelines.csv` until all mandatory criteria and independent review are complete.

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

- ERC Adult Advanced Life Support (2021): DOI 10.1016/j.resuscitation.2021.02.010; PMID 33773825. Primary bibliographic record and full-text PDF located; verify official PDF provenance, licence and later updates.
- ERC/ESICM Post-resuscitation Care (2021): DOI 10.1007/s00134-021-06368-4; PMID 33765189; PMCID PMC7993077. Joint adult ICU guideline; verify licence and current status.
- AHA 2020 adult basic and advanced life support guideline: DOI 10.1161/CIR.0000000000000916; PMID 33081529. Primary bibliographic record confirmed; obtain and check full text, licence and subsequent focused updates.

The candidate register flags the repeated ERC ALS entry as a duplicate of the original candidate; do not create two catalogue records for the same guideline edition.

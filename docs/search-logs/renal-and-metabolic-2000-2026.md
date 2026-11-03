# Renal and metabolic — historical search log (2000–2026)

**Work-package code:** GCCGRD-RENAL  
**Domain:** `renal_and_metabolic`  
**Search date:** 2026-11-03  
**Coverage:** 2000-01-01 to 2026-11-03; planned end date 2026-12-31.  
**Population:** Adults 18+; mixed-age documents only if adult recommendations can be separately identified.  
**Status:** Initial search protocol created; discovery and screening are incomplete.

## Search concepts

acute kidney injury; renal replacement therapy; CRRT; electrolyte disorders; acid-base disorders; glycaemic management; endocrine emergencies.

## Issuing bodies and repositories to search

KDIGO; ADQI; ISN; SCCM; ESICM; American Society of Nephrology (ASN); Endocrine Society.

## Reproducible PubMed discovery query

`("acute kidney injury" OR "renal replacement therapy" OR CRRT OR electrolyte OR acid-base) AND (guideline OR consensus) AND (adult OR ICU OR critically ill) AND ("2000/01/01"[Date - Publication] : "2026/11/03"[Date - Publication])`

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

Candidate rows for this domain are maintained in `data/screening/renal-and-metabolic_candidates.csv`. Do not promote a candidate to `data/guidelines.csv` until all mandatory criteria and independent review are complete.

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

- KDIGO AKI guideline (2012): DOI 10.1038/kisup.2012.1; official KDIGO guideline page and full-text PDF identified. It covers adult and paediatric AKI; confirm adult recommendations are separable. The 2026 AKI/AKD guideline was still explicitly a public-review draft on the search date and must not be represented as a final adopted guideline.
- International consensus report on hyperglycaemic crises in adults (2024): DOI 10.2337/dci24-0032; PMID 39052901; PMCID PMC11272983. Primary source and public full text identified. It is retained as a borderline candidate pending a direct critical-care relevance assessment; do not include solely because severe DKA/HHS can require ICU care.

The renal domain requires a further search for ADQI consensus statements, RRT/CRRT guidance, electrolyte emergencies, and formally adopted KDIGO updates. Drafts are excluded from the main guideline catalogue until final adoption/publication.

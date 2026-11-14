# Obstetric critical care — historical search log (2000–2026)

**GCCGRD domain:** `obstetric_critical_care`  
**Search date:** 2026-11-03  
**Coverage:** 2000-01-01 to 2026-11-03; the planned end date 2026-12-31 is still in the future.  
**Population:** Adults 18+; mixed-age guidance only where adult recommendations can be separated.  
**Status:** Initial domain mapping and discovery anchors; not exhaustive and not verified.

## Scope
Include formal adult clinical practice guidelines, consensus statements/definitions and evidence-based position statements with clinical recommendations directly relevant to critical care. Exclude reviews, trials, editorials, local protocols and standards without clinical recommendations. Apply GCCGRD full-text public-access requirements.

## Initial discovery anchors (candidates, not verified inclusions)
- SMFM Consult Series #67: Maternal Sepsis (2023)
- WHO recommendations for prevention and treatment of maternal peripartum infections (2015)

Verify exact title, issuer, publication/online-first date, identifiers, full text, licence, adult scope, methods and status against the primary source. Do not infer eligibility or currency from titles.

## Sources to search
- SMFM
- RCOG
- WHO
- FIGO
- ANZCOR
Also search PubMed, PMC, Europe PMC, Crossref, GIN and national guideline registries. Search official archives for older/withdrawn editions, focused updates and errata.

## Reproducible PubMed discovery query
`("maternal sepsis" OR "obstetric haemorrhage" OR "hypertensive emergencies" OR "maternal critical illness" OR "venous thromboembolism"[Title/Abstract]) AND (guideline[Publication Type] OR guideline*[Title/Abstract] OR consensus[Title/Abstract] OR position statement[Title/Abstract]) AND ("2000/01/01"[Date - Publication] : "2026/11/03"[Date - Publication])`

Run in PubMed and save exact query, date, result count and exported PMID set. This is a discovery strategy, not a final eligibility filter. Do not use an adult title/abstract filter as a hard exclusion.

## Required audit trail
For each source, record date searched, exact query/filter, result count, export/PMID set, duplicates removed, title/abstract screened, full texts sought/unavailable, included/excluded counts, exclusion reasons and reviewer initials.

## Edition and verification rules
- One record per substantive edition; parallel journal publications are linked, not counted twice.
- Preserve historical editions; do not infer supersession without issuing-body evidence.
- Record online-first and print issue dates separately.
- Public readability and licence/reuse permission are separate.
- Keep primary-source, full-text/licence and independent-review statuses distinct.
- Do not promote candidates to `data/guidelines.csv` before all mandatory checks and second review.

## Domain-specific concepts to search
- maternal sepsis
- obstetric haemorrhage
- hypertensive emergencies
- maternal critical illness
- venous thromboembolism

## Completeness statement
**Preliminary discovery only.** Exact result counts, deduplication and screening numbers, full-text eligibility and independent review remain outstanding.

## First-pass source checks — 2026-11-03

- SMFM Consult Series #67: Maternal Sepsis (2023): DOI 10.1016/j.ajog.2023.05.019; PMID 37236495. The official SMFM page states it was reaffirmed in 2025, replaces Consult Series #47, and is endorsed by ACOG. It provides explicit recommendations for maternal sepsis and septic shock, including vasopressor, fluid and antimicrobial management.
- Pregnancy is not itself an adult age criterion; retain only where the patient population meets the database's 18+ rule or adult recommendations are explicitly separable. This document is a strong critical-care candidate because it includes septic shock recommendations.

Cross-link maternal sepsis to the sepsis topic, but keep one canonical obstetric-domain record.

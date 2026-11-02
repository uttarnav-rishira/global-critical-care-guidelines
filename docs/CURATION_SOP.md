# Curation standard operating procedure

## 1. Discover candidate documents

Search official guideline catalogues and bibliographic databases. Start with `data/source_registry.csv`. Suggested search concepts:

`(intensive care OR critical care OR ICU OR critically ill) AND (guideline OR consensus OR position statement OR practice recommendations)`

Search by clinical domain as well as general terms. Search each source from 2000 onward. Save the search date, database, query, and result count in the pull-request description or a search log.

## 2. Screen title and document type

Exclude obvious non-guidelines, paediatric-only documents, abstracts, reviews, and local protocols. Do not include a paper merely because its title contains “consensus” unless it is a formal consensus product with clinical relevance.

## 3. Inspect the primary source

Open the issuing-body document and/or primary journal publication. Verify:
- exact title and author/group;
- publication date and edition;
- target population;
- scope and clinical relevance to adult critical care;
- issuing and endorsing organisations;
- development method and grading system;
- full-text access;
- DOI, PMID, PMCID, or official document identifier.

Do not use a search-engine snippet as evidence. If primary-source metadata conflict, investigate and document the discrepancy; do not guess.

## 4. Verify open access

Open the full text in a logged-out/private browser session where feasible. Confirm that the complete guideline (not just abstract or summary) is accessible without payment or institutional login. Record the URL and access type. Record the licence only when explicitly stated. Publicly readable does not necessarily mean permission to redistribute.

## 5. Verify citation

Check DOI resolution and compare the citation against the publisher/issuing-body page and PubMed/Crossref metadata where available. DOI presence alone does not prove open access. Record PMID/PMCID only after checking the identifier resolves to the same document.

## 6. Determine edition status

Check the issuing organisation's current guideline page and the primary document for updates, withdrawal, errata, or supersession. Preserve older editions as separate historical records. Record the date and evidence for the status decision.

## 7. Create the record

Assign the next stable `guideline_id`. Populate all applicable fields in `data/guidelines.csv`. Use ISO dates. Leave unknown fields blank or use the explicit `unclear`/`not_reported` values; never fill gaps with inference.

## 8. Independent second review

A second reviewer independently checks the nine items in `INCLUSION_CRITERIA.md`. Set `review_status=verified_two_reviewers` only after all checks pass. If a record fails, reject it with a reason or return it for correction.

## 9. Pull request and audit trail

Every pull request should state:
- candidate(s) added/changed;
- source databases/catalogues and search date;
- primary-source links;
- eligibility rationale;
- open-access verification;
- status/supersession evidence;
- reviewers.

Keep changes small enough to review. Never edit a published historical record to make it look like a newer edition. Correct metadata in place only with an explanatory commit/PR.

## 10. Periodic maintenance

At least every six months, check records marked `current` against the issuing body's catalogue. Prioritise high-impact domains (sepsis, ARDS/ventilation, shock, cardiac arrest, renal support, sedation/delirium, infection prevention). Update `last_official_status_check`; create a new record for a new edition; link versions. A date check is not proof of clinical currency unless the issuing body confirms status.

## 11. Automated discovery safeguards

If PubMed, Europe PMC, Crossref, or other APIs are used:
- treat results as candidates only;
- do not auto-include based on title/abstract;
- respect API rate limits and terms;
- respect publisher and repository licences;
- do not bulk-download PMC content except through permitted NCBI services;
- do not mirror full text unless the licence allows it.

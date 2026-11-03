# Historical critical-care guideline work programme (2000–2026)

**Project:** Global Critical Care Guidelines Research Database (GCCGRD)  
**Search date:** 2026-11-03  
**Coverage target:** 2000-01-01 to 2026-12-31. Search completeness can only be claimed through the actual search date.

## Purpose

This programme extends the sepsis work package across all remaining controlled clinical domains. Each domain has a dedicated search log with initial discovery anchors, issuing-body sources, a reproducible PubMed query, audit requirements and domain-specific screening concepts.

## Domain work packages

| Domain | Search log |
|---|---|
| Airway management and artificial airways | [Airway and ventilation](search-logs/airway-and-ventilation-2000-2026.md) |
| ARDS and acute respiratory failure | [ARDS and respiratory failure](search-logs/ards-and-respiratory-failure-2000-2026.md) |
| Haemodynamics and circulatory shock | [Haemodynamics and shock](search-logs/haemodynamics-and-shock-2000-2026.md) |
| Cardiac critical care and resuscitation | [Cardiac critical care](search-logs/cardiac-critical-care-2000-2026.md) |
| Neurology and neurocritical care | [Neurology and neurocritical care](search-logs/neurology-and-neurocritical-care-2000-2026.md) |
| Renal, electrolyte and metabolic critical care | [Renal and metabolic](search-logs/renal-and-metabolic-2000-2026.md) |
| Nutrition and gastrointestinal critical care | [Nutrition and gastrointestinal](search-logs/nutrition-and-gastrointestinal-2000-2026.md) |
| Haematology, coagulation and transfusion | [Haematology and transfusion](search-logs/haematology-and-transfusion-2000-2026.md) |
| Sedation, analgesia, delirium and sleep | [Sedation, analgesia and delirium](search-logs/sedation-analgesia-delirium-2000-2026.md) |
| Mobilisation, rehabilitation and recovery | [Mobilisation and recovery](search-logs/mobilisation-rehabilitation-and-recovery-2000-2026.md) |
| Trauma and burns | [Trauma and burns](search-logs/trauma-and-burns-2000-2026.md) |
| Toxicology and poisoning | [Toxicology](search-logs/toxicology-2000-2026.md) |
| Obstetric critical care | [Obstetric critical care](search-logs/obstetric-critical-care-2000-2026.md) |
| Ethics, end-of-life and palliative care | [Ethics and end-of-life](search-logs/ethics-end-of-life-and-palliative-care-2000-2026.md) |
| Organisation, safety, staffing and quality | [Organisation and safety](search-logs/organisation-safety-and-quality-2000-2026.md) |

The sepsis work package remains separately documented in [Work package 01](sepsis-work-package-01.md), with international and regional search logs.

## Candidate register

`data/screening/domain_candidates_2000_2026.csv` contains 28 initial discovery anchors across the remaining domains. These are **not verified inclusions** and have not been added to `data/guidelines.csv`. Some are broad candidates requiring exact document retrieval; cross-domain overlap must be resolved to avoid duplicate records.

## Curation workflow

1. Run the domain PubMed query and save exact result counts and PMID exports.
2. Search issuing-body archives and regional/national guideline repositories, including native-language sources where relevant.
3. Deduplicate parallel journal publications; retain one record per substantive edition.
4. Screen document type, adult 18+ scope (or separable adult recommendations), direct ICU relevance and issuing authority.
5. Obtain the complete public full text; record access URL and exact licence separately.
6. Check DOI/PMID/PMCID and publication/online-first dates against the primary document.
7. Check official status, corrections, addenda and supersession; preserve historical editions.
8. Complete independent second review before promoting eligible records into the master catalogue.

## Priority order

Suggested first-pass sequencing:
1. Airway/ventilation and ARDS/respiratory failure
2. Haemodynamics/shock and cardiac critical care
3. Renal/metabolic and nutrition/gastrointestinal
4. Sedation/delirium and mobilisation/recovery
5. Neurology/neurocritical care and trauma/burns
6. Haematology/transfusion and toxicology
7. Obstetric critical care and ethics/end-of-life
8. Organisation, safety and quality

This is a practical workflow order, not a ranking of clinical importance.

## Completeness and governance

- The 15 logs are initial search frameworks and candidate maps, not evidence that each domain has been exhaustively searched.
- Exact database counts, export files, deduplication and screening numbers remain to be entered after reproducible database runs.
- The 28 candidate anchors require primary-source verification; the screening register deliberately leaves unverified identifiers, licences and review decisions blank/pending.
- Cross-domain documents should have one canonical record and multiple domain tags where the schema supports it.
- Standards, service specifications, pathways and local protocols must be distinguished from formal CPGs.
- No record is promoted solely because a society website calls it a guideline.
- No claim of global completeness through 2026-12-31 is possible before that date and a final update search.

## Research-index disclaimer

GCCGRD is a research index, not clinical decision support. Inclusion does not imply endorsement, currency, or suitability for an individual patient.

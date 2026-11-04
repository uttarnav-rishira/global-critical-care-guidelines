# Global Critical Care Guidelines Research Database (GCCGRD)

A developing, open-access research index of **adult critical-care clinical practice guidelines, international consensus statements, and formal evidence-based position statements**, with a target historical scope of **1 January 2000–31 December 2026**.

> **Beta status (4 November 2026):** This is an early-stage research index. The catalogue is not exhaustive, historical and geographic searches are still in progress, and records may remain provisional until primary-source, full-text access, licence and independent-review checks are complete. The year 2026 is not yet complete.

> **Important:** GCCGRD is a research and discovery resource, not a clinical decision-support system. It does not provide patient-specific recommendations and does not replace current issuing-body guidance, local protocols or specialist advice.

## Project scope

| Setting | Definition |
|---|---|
| Population | Adults aged 18 years and older; mixed-population documents only when adult recommendations are separately identifiable |
| Publication period | 1 January 2000–31 December 2026 (target period; 2026 is ongoing) |
| Publication access | Publicly readable complete guideline/consensus text or official full-text document; an abstract alone is insufficient |
| Geography | International, national and regional guidance; no country or income-setting exclusion |
| Document types | Clinical practice guidelines, formal consensus statements/definitions and formal evidence-based position statements with clinical recommendations |
| Primary references | Original issuing-body document and/or primary peer-reviewed publication, with DOI/PMID/official URL where available |
| Versioning | Materially revised editions are retained separately and linked where the relationship is documented |
| Curation | Human-reviewed; automated discovery is never automatic inclusion |

## Current catalogue status

The public website reads its catalogue from [`data/guidelines.csv`](data/guidelines.csv). At this beta stage, the catalogue contains a starter record and should not be interpreted as a systematic or exhaustive inventory.

The current 2026 Surviving Sepsis Campaign entry is **provisional**: its primary issuing-body page has been checked, but the full-text access/licence check is not complete and independent second review is pending. It is therefore not a fully verified record. The website displays these checks separately.

Candidate research and search logs are maintained separately from the public catalogue. In particular, records in the open research branch or candidate screening register are not approved catalogue entries.

## What is included

A document is eligible only if **all mandatory criteria** in [`docs/INCLUSION_CRITERIA.md`](docs/INCLUSION_CRITERIA.md) are met. The database records the issuing body, panel, methods, adult population, clinical scope, publication/version dates, recommendation methodology, access status, primary references, verification evidence and supersession relationships.

## Repository layout

```text
.
├── README.md
├── LICENSE
├── CITATION.cff
├── requirements.txt
├── .github/workflows/
├── data/
│   ├── guidelines.csv
│   ├── source_registry.csv
│   └── screening/
├── docs/
│   ├── INCLUSION_CRITERIA.md
│   ├── DATA_DICTIONARY.md
│   ├── CURATION_SOP.md
│   ├── GITHUB_SETUP.md
│   ├── LAUNCH_READINESS.md
│   └── search-logs/
├── index.html
└── scripts/validate_guidelines.py
```

## Using the website

The website is a static, searchable view of the curated catalogue. Search by title, topic, issuing organisation, DOI or identifier; filter by clinical domain and publication year. Links lead to issuing-body pages, full-text access routes, DOI records and PubMed where available.

The website is deployed through GitHub Pages when the Pages workflow completes successfully and repository Pages settings permit deployment. See the [Actions workflow](.github/workflows/pages.yml) and [launch-readiness record](docs/LAUNCH_READINESS.md). A repository code change alone does not prove that a public deployment has succeeded.

## Curation and verification

The project distinguishes:
1. **Candidate identified** — a potentially eligible document has been located.
2. **Primary source checked** — bibliographic details and the issuing-body/primary source have been checked.
3. **Open-access verified** — the complete text is publicly accessible and its access/licensing conditions have been assessed.
4. **Second review complete** — an independent reviewer has checked eligibility and the key record fields.

A record is not fully verified merely because a DOI, abstract or public landing page exists. Do not infer that a newer publication supersedes an older edition unless the issuing body or primary source supports that relationship. See [inclusion criteria](docs/INCLUSION_CRITERIA.md), [data dictionary](docs/DATA_DICTIONARY.md) and [curation SOP](docs/CURATION_SOP.md).

## Quality principles

- Do not infer guideline status from a search snippet.
- Do not treat a systematic review, narrative review, trial, editorial, protocol, educational page or local hospital pathway as a guideline.
- Do not include paywalled full texts under an open-access-only setting, even if an abstract is free.
- Do not silently replace historical editions. Preserve each edition and document its relationship to later versions.
- Distinguish publication date from the date a guideline was last reviewed or verified.
- Record corrections transparently in Git history and the change log.
- Never fabricate a DOI, PMID, author list, recommendation, consensus percentage or access status.
- Do not describe the database as exhaustive until documented searching, deduplication, screening, verification and gap assessment have been completed.

## Primary discovery sources

See [`data/source_registry.csv`](data/source_registry.csv). Key starting points include the Society of Critical Care Medicine (SCCM), European Society of Intensive Care Medicine (ESICM), American Thoracic Society (ATS), European Respiratory Society (ERS), Kidney Disease: Improving Global Outcomes (KDIGO), World Health Organization (WHO), PubMed and PubMed Central.

Automated metadata services are discovery aids only. For PMC, comply with NCBI's API and reuse/licensing conditions; not every PMC article is reusable as full text.

## Citation and licensing

The repository software and schema are MIT-licensed. **Guideline texts, figures, tables and publisher PDFs are not relicensed by this repository.** GCCGRD links to source documents and stores bibliographic metadata; it does not republish source full texts unless the relevant licence explicitly permits reuse. Each record must state the access route and, where relevant, the licence.

## Contributing

See [`docs/CURATION_SOP.md`](docs/CURATION_SOP.md). Contributions should include the primary source, evidence for eligibility, a completed record and a short rationale. A second reviewer should verify the primary reference, eligibility and access status before a record is treated as fully verified.

# Global Critical Care Guidelines Research Database

A GitHub-based, open-access research register of **adult critical-care clinical practice guidelines, international consensus statements, and formal position statements**, with historical coverage from **1 January 2000 onward**.

> **Important:** This repository is a research index, not a clinical decision-support system. It does not replace local protocols, specialist advice, or the current version of a guideline. A record marked `current` means that its status was checked against the issuing organisation at the stated verification date; it is not a guarantee that the recommendation is appropriate for an individual patient.

## Project settings

| Setting | Value |
|---|---|
| Historical coverage | 1 January 2000 onward |
| Population | Adults (18 years and older); mixed-population documents only when adult recommendations are separately identifiable |
| Publication access | Open access only: a publicly readable full guideline/consensus text or official full-text document |
| Geography | International; no country or income-setting exclusion |
| Document types | Clinical practice guidelines, international consensus statements, formal evidence-based position statements |
| Primary references | Original issuing-body document and/or the primary peer-reviewed publication, with DOI/PMID/official URL where available |
| Versioning | Every materially revised edition is a separate record linked to its predecessor/successor |
| Curation | Human-reviewed; automated discovery is never automatic inclusion |

## What is included

A document is eligible only if **all mandatory criteria** in [`docs/INCLUSION_CRITERIA.md`](docs/INCLUSION_CRITERIA.md) are met. The database records the issuing body, panel, methods, adult population, clinical scope, publication/version dates, recommendation methodology, access status, primary references, verification evidence, and supersession relationships.

## Repository layout

```text
.
├── README.md
├── LICENSE
├── CITATION.cff
├── requirements.txt
├── .gitignore
├── .github/workflows/validate.yml
├── data/
│   ├── guidelines.csv          # Curated guideline records
│   └── source_registry.csv     # Official discovery/catalogue sources
├── docs/
│   ├── INCLUSION_CRITERIA.md
│   ├── DATA_DICTIONARY.md
│   ├── CURATION_SOP.md
│   └── GITHUB_SETUP.md
└── scripts/
    └── validate_guidelines.py
```

## Quick start

1. Create a public GitHub repository named `global-critical-care-guidelines`.
2. Upload the contents of this folder to the repository's root.
3. Follow [`docs/GITHUB_SETUP.md`](docs/GITHUB_SETUP.md).
4. Add candidate documents to `data/guidelines.csv` only after applying the inclusion criteria and curation SOP.
5. Open a pull request for each batch. The GitHub Actions validation workflow must pass before merge.

## Database status at creation

The repository includes:
- the agreed scope and eligibility rules;
- a structured CSV schema;
- a starter list of official discovery sources;
- automated data-quality checks;
- one **illustrative verified seed record**: the 2026 adult Surviving Sepsis Campaign guideline, based on the official SCCM/issuing-body page and its primary DOI citation.

This is a **starter database, not an exhaustive inventory** of all eligible documents published since 2000. Do not describe it as complete until a documented search, deduplication, screening, and verification exercise has been completed across the source registry and bibliographic databases.

## Quality principles

- Do not infer guideline status from a search snippet.
- Do not treat a systematic review, narrative review, trial, editorial, protocol, educational page, or local hospital pathway as a guideline.
- Do not include paywalled full texts under an open-access-only setting, even if an abstract is free.
- Do not silently replace historical editions. Preserve each edition and link it to the next edition.
- Distinguish the publication date from the date the guideline was last reviewed or verified.
- Record corrections transparently in Git history and the change log.
- Never fabricate a DOI, PMID, author list, recommendation, consensus percentage, or access status.

## Primary discovery sources

See [`data/source_registry.csv`](data/source_registry.csv). Key starting points include the Society of Critical Care Medicine (SCCM), European Society of Intensive Care Medicine (ESICM), American Thoracic Society (ATS), European Respiratory Society (ERS), Kidney Disease: Improving Global Outcomes (KDIGO), World Health Organization (WHO), and PubMed/PMC.

Automated metadata services are discovery aids only. For PMC, comply with NCBI's API and reuse/licensing conditions; not every PMC article is reusable as full text.

## Citation and licensing

The repository software and schema are MIT-licensed. **Guideline texts, figures, tables, and publisher PDFs are not relicensed by this repository.** Store metadata and links, not copied full texts, unless the source's licence explicitly permits reuse. Each record must state the access route and, where relevant, the licence.

## Contributing

See [`docs/CURATION_SOP.md`](docs/CURATION_SOP.md). Contributions should include the primary source, evidence for eligibility, a completed record, and a short rationale. A second reviewer should verify the primary reference and access status before merge.

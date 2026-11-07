# Priority batch 01 — PDF redistribution rights assessment

Assessment date: 2026-11-06. Scope: DOM-057, DOM-060–DOM-067, DOM-069–DOM-071.

## Potentially eligible for repository storage under CC BY 4.0

- DOM-061 — Japanese Sepsis Guidelines, J Intensive Care manifestation DOI 10.1186/s40560-025-00776-0 only. Do not substitute the parallel Acute Medicine & Surgery manifestation, which has a different licence.
- DOM-062 — J-ReCIP 2023.
- DOM-063 — ISCCM sepsis in resource-limited settings.
- DOM-064 — ISCCM invasive fungal infections in ICU.
- DOM-065 — ISCCM severe dengue (adult-scope decision still requires Reviewer 2).
- DOM-066 — ISCCM severe malaria (adult recommendation separability still requires Reviewer 2).
- DOM-067 — ISCCM tuberculosis in critically ill patients (adult-scope decision still requires Reviewer 2).
- DOM-070 — Saudi/SSAI contextualised stress-ulcer prophylaxis.

These eight are only provisionally rights-cleared based on the article-level CC BY 4.0 records. Before upload, check the exact PDF manifestation, edition, attribution requirements, and third-party figure/table exclusions.

## Not cleared for mirroring on current evidence

- DOM-057 — EUR repository terms limit use to personal use and sharing the repository link; do not mirror.
- DOM-060 — ERC/ESICM 2025 post-resuscitation guideline: public PDF found, but no redistribution licence established; do not mirror without permission.
- DOM-069 — SCCM 2025 adult end-of-life guideline: copyright/reuse permission not established; do not mirror.
- DOM-071 — Ketamine analgo-sedation: Wiley says Free Access, but repository manuscript record says licence unspecified; free access alone is not redistribution permission.

## Repository action and limitations

No PDF has been added and the manifest remains header-only. The available GitHub workflow here can create UTF-8 text files but does not expose a binary PDF upload path. The eight potential candidates require exact PDF retrieval, local inspection, and upload through a supported Git/GitHub binary route. Do not add manifest rows until each binary is committed. All 12 candidates remain pending independent second review; rights clearance is not eligibility approval.

## Sources

- DOM-061: https://doi.org/10.1186/s40560-025-00776-0
- DOM-062: https://pmc.ncbi.nlm.nih.gov/articles/PMC10629099/
- DOM-063: https://pmc.ncbi.nlm.nih.gov/articles/PMC11369916/
- DOM-064: https://pmc.ncbi.nlm.nih.gov/articles/PMC11369924/
- DOM-065: https://pmc.ncbi.nlm.nih.gov/articles/PMC11369922/
- DOM-066: https://pmc.ncbi.nlm.nih.gov/articles/PMC11369926/
- DOM-067: https://pmc.ncbi.nlm.nih.gov/articles/PMC11369919/
- DOM-070: https://pmc.ncbi.nlm.nih.gov/articles/PMC12883282/
- DOM-071: https://onlinelibrary.wiley.com/doi/10.1111/aas.14470 and https://researchportal.helsinki.fi/en/publications/ketamine-analgo-sedation-for-mechanically-ventilated-critically-i/
- DOM-060: https://www.scienceopen.com/document?vid=185212ab-cc28-41b1-b8b6-cf4593d7d33c


## Current retrieval automation

- Importer: [`scripts/import_open_access_pdfs.py`](../../scripts/import_open_access_pdfs.py)
- Manual workflow: [`.github/workflows/import-open-access-pdfs.yml`](../../.github/workflows/import-open-access-pdfs.yml)
- The workflow uses the current NCBI PMC Article Datasets Cloud Service structure (metadata JSON per article version; XML and PDF objects), not the retired legacy FTP layout.
- The default run accepts only commercial-redistribution CC BY licences. The optional non-commercial setting permits CC BY-NC and CC BY-NC-ND unchanged files only; do not select it unless the repository's use and redistribution are genuinely non-commercial.
- No action run has yet been triggered from this session. The manifest remains empty until the workflow actually commits PDF binaries and checksums.

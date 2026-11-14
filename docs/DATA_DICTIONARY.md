# Data dictionary

The authoritative machine-readable schema is the header row in `data/guidelines.csv`.

| Field | Meaning / permitted values |
|---|---|
| `guideline_id` | Stable repository ID, e.g. `GCCG-000001`; never recycle an ID |
| `title` | Exact title from the primary source |
| `short_title` | Useful abbreviated title |
| `publication_year` | Year of first publication of this edition |
| `publication_date` | ISO date `YYYY-MM-DD`, earliest official publication date |
| `online_first_date` | ISO date if different and reported |
| `document_type` | `clinical_practice_guideline`, `international_consensus_statement`, `consensus_definition`, `position_statement`, `focused_update`, `correction_or_erratum` |
| `population` | `adult` or `adult_subgroup_separable` |
| `age_minimum` | Usually `18`; explain exceptions in notes |
| `critical_care_relevance` | Concise explanation of direct ICU relevance |
| `clinical_domain` | Controlled broad domain; see controlled vocabulary below |
| `subdomains` | Semicolon-separated topics |
| `issuing_organisations` | Exact organisation names, semicolon-separated |
| `endorsement_organisations` | Exact endorsing bodies, semicolon-separated |
| `geographic_classification` | Values defined in inclusion criteria |
| `panel_countries_regions` | Semicolon-separated only when documented |
| `development_method` | `GRADE`, `Delphi`, `modified_Delphi`, `nominal_group`, `evidence_to_decision`, `other`, `not_reported`, `unclear` |
| `consensus_threshold` | Exact threshold if reported; otherwise blank |
| `recommendation_grading` | Exact system/labels reported; otherwise blank |
| `doi` | DOI without URL prefix; blank if none |
| `pmid` | PubMed ID; blank if none |
| `pmcid` | PMC ID; blank if none |
| `primary_citation_vancouver` | Full primary citation, checked against source |
| `official_guideline_url` | Official issuing-body full text or document page |
| `open_access_url` | Direct public full-text access URL |
| `access_type` | `official_html`, `official_pdf`, `open_access_journal`, `repository_full_text` |
| `licence` | Exact licence if stated; `not_stated` if not stated |
| `status` | Values defined in inclusion criteria |
| `supersedes_id` | Earlier record ID, if applicable |
| `superseded_by_id` | Later record ID, if applicable |
| `last_official_status_check` | ISO date when status was checked |
| `primary_source_verified` | `yes` only after direct inspection |
| `open_access_verified` | `yes` only after full-text access check |
| `review_status` | `pending_second_review`, `verified_two_reviewers`, `rejected`, `needs_correction` |
| `reviewer_1` / `reviewer_2` | Reviewer initials or GitHub handles; avoid personal contact details |
| `verification_notes` | Concise evidence trail: what was checked and where |
| `record_created` / `record_updated` | ISO dates |
| `notes` | Important caveats; do not place unstructured recommendations here |

## Controlled clinical domains

Use one primary domain and semicolon-separated subdomains:
- `airway_and_ventilation`
- `ards_and_respiratory_failure`
- `sepsis_and_infection`
- `haemodynamics_and_shock`
- `cardiac_critical_care`
- `neurology_and_neurocritical_care`
- `renal_and_metabolic`
- `nutrition_and_gastrointestinal`
- `haematology_and_transfusion`
- `sedation_analgesia_delirium`
- `mobilisation_rehabilitation_and_recovery`
- `trauma_and_burns`
- `toxicology`
- `obstetric_critical_care`
- `ethics_end_of_life_and_palliative_care`
- `organisation_safety_and_quality`
- `other`

Use Australian/British spelling in repository-authored metadata (e.g. `haemodynamics`), while preserving exact source titles.


## Stored full-text PDF manifest

The main catalogue does not store PDF binaries or detailed file-rights metadata. For every PDF stored under `sources/open-access/`, use `sources/open-access/manifest.csv`. Its columns are:

| Column | Meaning |
|---|---|
| `guideline_id` | Stable catalogue identifier |
| `pdf_path` | Repository-relative path to the committed PDF |
| `doi` | DOI of the exact stored edition |
| `issuing_organisations` | Exact issuing organisation names |
| `publication_year` | Year of the stored edition |
| `version_edition` | Version, edition, update, or document designation |
| `original_source_url` | URL from which the document was obtained |
| `access_date` | Date accessed/downloaded, ISO `YYYY-MM-DD` |
| `licence_name_version` | Exact licence and version, or explicit permission description |
| `licence_url` | Canonical licence URL, where available |
| `attribution_copyright_notice` | Required attribution and copyright statement |
| `redistribution_basis` | Why redistribution in this public repository is permitted |
| `rights_evidence_url` | URL to licence/permission evidence |
| `notes` | Conditions, restrictions, or provenance notes |

A blank or unclear licence is not permission to redistribute. The manifest must not list a PDF until the file exists in the repository and its rights have been checked.

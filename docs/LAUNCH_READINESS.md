# GCCGRD launch-readiness record

**Assessment date:** 4 November 2026  
**Release stage:** Early public beta (conditional)  
**Repository:** https://github.com/uttarnav-rishira/global-critical-care-guidelines  
**Expected Pages URL:** https://uttarnav-rishira.github.io/global-critical-care-guidelines/

## Decision

The project is suitable for a clearly labelled **early public beta as a research index**, provided the public site is reachable and the Pages deployment completes. It is **not ready to be described as a complete, systematically verified global guideline database**.

## Checks completed

- [x] Public repository and website source exist on `main`.
- [x] Website reads the catalogue from `data/guidelines.csv`.
- [x] Search and filters are provided for title/topic/organisation/identifier, clinical domain and year.
- [x] Primary-source, full-text access and independent-review states are displayed separately.
- [x] Clinical decision-support disclaimer is visible.
- [x] README corrected: the 2026 Surviving Sepsis Campaign seed record is provisional, not a verified record.
- [x] Website banner and metadata identify the release as beta and clarify that 2000–2026 is a target period, not completed coverage.
- [x] Candidate research register remains separate from the public catalogue; the research expansion PR is not treated as approved catalogue data.

## Outstanding checks / limitations

- [x] Confirm the GitHub Pages deployment completed successfully: workflow run [41772040032](https://github.com/uttarnav-rishira/global-critical-care-guidelines/actions/runs/41772040032) finished with conclusion `success` for commit `92de5433d9b05f474ad5dc3c997b6d5a4d45f102`.
- [ ] Human browser smoke test remains outstanding: open the public Pages URL on desktop and mobile. The deployment workflow succeeded, but this environment's browser could not independently load the GitHub Pages host, so visual/public reachability is not claimed as independently confirmed.
- [ ] Test live search, filters, external links and dataset loading in the deployed site from a normal browser.
- [ ] Complete the primary full-text accessibility and licence assessment for the seed record.
- [ ] Complete independent second review of the seed record before calling it fully verified.
- [ ] Continue systematic searching, screening, deduplication and geographic/domain gap assessment.
- [ ] Reassess 2026 coverage after 31 December 2026; until then, describe the end date as a target.

## Catalogue status at this release

The public CSV contains one starter record. It is the 2026 adult Surviving Sepsis Campaign guideline. The issuing-body page and primary DOI citation have been checked, but the record itself states:

- `primary_source_verified=yes`
- `open_access_verified=no`
- `review_status=pending_second_review`

The record must not be described as fully verified until the complete guideline text and access/licensing conditions have been checked and an independent second reviewer has completed the required review. Public availability of an issuing-body landing page is not, by itself, proof of open-access full text or a reuse licence.

## Publication wording

Recommended description:

> GCCGRD is an early-stage, open-access research index of adult critical-care guidelines and consensus documents. Historical and geographic coverage is being expanded. Records display their source, access and review status; provisional entries should not be treated as fully verified. The resource is for research and discovery, not clinical decision support.

Do not claim:
- exhaustive coverage of all eligible guidelines from 2000–2026;
- every listed record is independently verified;
- public readability means permission to reproduce guideline text, tables or figures;
- a record marked current is a patient-specific clinical recommendation.

## Beta acceptance criteria

A limited beta announcement is reasonable after the public URL is confirmed reachable and the basic website smoke tests above are completed. A broader launch as a mature research database should wait until the catalogue has meaningful verified coverage across domains and regions, documented search methods, independent review, and a reproducible gap audit.

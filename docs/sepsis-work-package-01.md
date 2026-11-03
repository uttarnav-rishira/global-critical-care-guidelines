# Work package 01 — Sepsis and septic shock (2000–2026)

**Repository:** Global Critical Care Guidelines Research Database (GCCGRD)  
**Package status:** Initial discovery and screening infrastructure created; candidate verification in progress  
**Search date:** 2026-11-03

## Objectives

1. Establish a reproducible search strategy for adult sepsis and septic shock guidance.
2. Identify historical editions and formal consensus-definition documents.
3. Preserve one record per substantive guideline edition, while documenting parallel journal publications.
4. Record candidate identification separately from primary-source, full-text access/licence, and independent-review verification.
5. Add only fully eligible, openly readable documents to the master catalogue after second review.

## Files in this package

- `docs/search-logs/sepsis-2000-2026.md` — search sources, reproducible PubMed queries, source trail, limitations and next actions.
- `data/screening/sepsis_candidates.csv` — first-pass candidate register; not the master catalogue.
- `docs/templates/sepsis-screening-form.md` — individual candidate screening and review form.

## First-pass candidates

The candidate register currently contains eight entries:

- 2001 International Sepsis Definitions Conference (published 2003)
- SSC 2004
- SSC 2008
- SSC 2012
- SSC 2016 edition (journal publication in 2017)
- Sepsis-3 consensus definitions (2016)
- SSC 2021
- SSC 2026

The register is intentionally conservative. Some candidates have an identified full-text location, but no candidate is marked as independently verified. The 2004 and 2016 SSC documents require further full-text access checks. The 2001 consensus document requires full-text and scope checks. The 2021 PMC reuse statement is conditional; do not interpret it as a general open licence.

## Edition handling

Several SSC editions were published in both *Critical Care Medicine* and *Intensive Care Medicine*. These parallel publications represent the same guideline edition, not separate revisions. The candidate register chooses a canonical publication and records the companion DOI/PMID in notes. The database should not inflate its edition count by counting the same recommendations twice.

For 2008, online-first publication occurred on 4 December 2007, before the 2008 journal issue. Record both the first online date and issue year. For 2012 and 2016, use the actual publication date while retaining the conventional guideline edition label.

## Inclusion caution

The 2001 definitions conference publication and Sepsis-3 are formal consensus-definition candidates rather than treatment guidelines. Their inclusion depends on the repository's formal document-type criteria and direct adult critical-care relevance. The 2012 SSC publication includes a paediatric subgroup; adult recommendations must be separable before inclusion.

## Current work status

- [x] Create work-package search log
- [x] Create candidate screening register
- [x] Create candidate-level screening template
- [x] Identify primary bibliographic records for initial SSC editions and consensus documents
- [ ] Complete reproducible PubMed exports and capture result counts
- [ ] Search national/regional sepsis guideline sources
- [ ] Verify full text and licence for each candidate
- [ ] Independent second review
- [ ] Add eligible records to `data/guidelines.csv`
- [ ] Link historical editions and confirm current/superseded status

## No clinical decision support

GCCGRD is a research index. It does not provide clinical recommendations, replace local protocols, or establish the current standard of care.

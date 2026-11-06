# Inclusion and exclusion criteria

## Scope

A global, historical register of adult critical-care clinical practice guidelines and formal international or national consensus guidance published from **1 January 2000 onward**.

## Mandatory inclusion criteria — all must be met

1. **Date:** First published on or after 2000-01-01. If online-first and print dates differ, record both where available and use the earliest official publication date for screening.
2. **Population:** Adults aged 18 years or older. A mixed adult/paediatric document is eligible only when adult recommendations are explicitly separable and the record clearly identifies the adult section.
3. **Clinical relevance:** Directly addresses prevention, diagnosis, monitoring, treatment, rehabilitation, organisation, or end-of-life care of critically ill adults, or a condition commonly managed in an ICU. The rationale must be recorded.
4. **Document type:** Formal clinical practice guideline, international consensus statement/definition, or formal evidence-based position statement containing clinical recommendations or consensus definitions.
5. **Issuing authority:** Issued, endorsed, or formally co-sponsored by a recognised professional society, governmental/public health authority, intergovernmental organisation, or multidisciplinary expert panel with a stated development process.
6. **Primary-source verification:** The actual guideline/consensus document or primary peer-reviewed publication is located and checked. A catalogue page or secondary summary alone is insufficient.
7. **Open access:** The full guideline text is publicly readable without payment or institutional login through an official source or a lawful open-access repository. An abstract alone does not qualify. Record the exact access URL and access type.
8. **Traceable citation:** At least one verifiable primary reference is available: DOI, PMID, official document identifier, or stable official URL. If no DOI/PMID exists, the issuing body's official document URL and title/date must be verifiable.
9. **Version status:** Publication date, version/edition, and current/historical/withdrawn status are recorded. Unknown status must be `status_unknown`, not guessed.

## Eligible document types

- Evidence-based clinical practice guidelines.
- International consensus definitions and consensus management statements.
- Formal society/government position statements when they contain explicit clinical recommendations.
- Joint or endorsed guidelines from multiple organisations.
- Major revisions, focused updates, addenda, and corrigenda when they materially alter recommendations or correct the source record.

## Exclusion criteria

- Paediatric-only or neonatal-only documents.
- Documents first published before 2000 (may be listed in a separate future bibliography, but not in the core database).
- Narrative reviews, systematic reviews, meta-analyses, original trials, editorials, letters, conference abstracts, educational summaries, podcasts, slide decks, and news releases.
- Local hospital protocols or unendorsed institutional pathways.
- Documents with no identifiable issuing authority or no primary source.
- Documents whose full text is paywalled, inaccessible, or available only through an abstract.
- Documents that merely mention critical care without providing applicable adult ICU recommendations or consensus definitions.
- Duplicate database records for the same edition. Instead, merge metadata and retain all primary references in one record.
- Drafts, consultation versions, and preprints unless formally adopted as the final guidance by the issuing authority.

## International consensus classification

Do not call a document “international consensus” solely because it has authors from multiple countries.

Use one of these values:
- `international_multisociety`: jointly issued/endorsed by two or more international or national professional bodies from different countries/regions, or explicitly designated international by the issuing bodies.
- `international_panel`: explicitly international panel with documented multinational representation, but not formally jointly issued by multiple bodies.
- `national_or_regional`: issued by one national or regional authority.
- `not_applicable`: use only for formal consensus definitions where geographic classification is not meaningful; explain in notes.

Record the organisations, countries/regions represented, and the evidence supporting the classification. Do not invent panel geography or consensus thresholds.

## Recommendation methodology

Record the method exactly as reported:
- GRADE;
- Delphi / modified Delphi;
- nominal group technique;
- evidence-to-decision framework;
- other named method;
- not reported / unclear.

Do not infer GRADE from the presence of evidence tables. If consensus percentage, voting threshold, or agreement level is stated, record the exact value and source location. Otherwise leave it blank.

## Historical and current status

Each edition is a separate record. Use:
- `current` — issuing body or primary source explicitly identifies it as current, or a curator has checked the official source and found no superseding edition; include verification date and evidence.
- `superseded` — a later edition explicitly replaces it.
- `withdrawn` — issuing body explicitly withdrew it.
- `archived_historical` — retained for historical research; current applicability not asserted.
- `status_unknown` — unable to verify.

A newer publication on the same topic does not automatically supersede an older document unless the issuing body or primary source establishes that relationship. Record supersession links in `supersedes_id` and `superseded_by_id`.

## Two-person verification

For each record, Reviewer 1 enters and checks the record. Reviewer 2 independently verifies:
1. title, issuing body, and date against the primary source;
2. adult population and ICU relevance;
3. full-text open access;
4. DOI/PMID/official URL;
5. edition and supersession status.

Until the second review is complete, set `review_status` to `pending_second_review`. A pending record must not be presented as fully verified.


## Full-text access versus permission to redistribute

The open-access eligibility criterion concerns public readability of the complete guideline. It does **not** itself grant permission to copy or redistribute the PDF. The main catalogue may link to a lawfully readable full text even when the PDF cannot be mirrored.

Only place a PDF in `sources/open-access/` when its exact licence or explicit written permission permits redistribution in this public repository. Record the licence/permission, attribution requirements, original URL, access date, and version in `sources/open-access/manifest.csv`. Do not upload paywalled, restricted, copyright-restricted, or rights-unclear files. See `sources/open-access/README.md` and the curation SOP for operational requirements.

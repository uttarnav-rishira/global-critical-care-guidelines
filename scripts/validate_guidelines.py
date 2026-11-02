#!/usr/bin/env python3
"""Conservative structural validator for the curated guideline CSV."""
import csv
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "data" / "guidelines.csv"
REQUIRED = [
    "guideline_id", "title", "publication_year", "publication_date",
    "document_type", "population", "critical_care_relevance", "clinical_domain",
    "issuing_organisations", "geographic_classification", "doi",
    "primary_citation_vancouver", "official_guideline_url", "open_access_url",
    "access_type", "status", "primary_source_verified", "open_access_verified",
    "review_status"
]
ENUMS = {
    "document_type": {"clinical_practice_guideline", "international_consensus_statement",
        "consensus_definition", "position_statement", "focused_update", "correction_or_erratum"},
    "population": {"adult", "adult_subgroup_separable"},
    "geographic_classification": {"international_multisociety", "international_panel",
        "national_or_regional", "not_applicable"},
    "access_type": {"official_html", "official_pdf", "open_access_journal", "repository_full_text"},
    "status": {"current", "superseded", "withdrawn", "archived_historical", "status_unknown"},
    "primary_source_verified": {"yes", "no"},
    "open_access_verified": {"yes", "no"},
    "review_status": {"pending_second_review", "verified_two_reviewers", "rejected", "needs_correction"},
}
DOI_RE = re.compile(r"^10\.\d{4,9}/\S+$", re.I)
URL_RE = re.compile(r"^https://", re.I)

def main():
    if not CSV_PATH.exists():
        print(f"ERROR: missing {CSV_PATH}")
        return 1
    errors, warnings, seen = [], [], set()
    with CSV_PATH.open(newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            print("ERROR: CSV has no header")
            return 1
        rows = list(reader)
        for i, row in enumerate(rows, start=2):
            label = f"row {i} ({row.get('guideline_id','no ID')})"
            for field in REQUIRED:
                if not (row.get(field) or "").strip():
                    errors.append(f"{label}: missing required field '{field}'")
            gid = (row.get("guideline_id") or "").strip()
            if gid and gid in seen:
                errors.append(f"{label}: duplicate guideline_id '{gid}'")
            seen.add(gid)
            for field, allowed in ENUMS.items():
                value = (row.get(field) or "").strip()
                if value and value not in allowed:
                    errors.append(f"{label}: invalid {field} '{value}'")
            try:
                pubdate = date.fromisoformat(row.get("publication_date", ""))
                if pubdate < date(2000, 1, 1):
                    errors.append(f"{label}: publication date is before 2000-01-01")
            except ValueError:
                errors.append(f"{label}: publication_date must be YYYY-MM-DD")
            try:
                year = int(row.get("publication_year", ""))
                if year < 2000 or year > date.today().year + 1:
                    errors.append(f"{label}: publication_year outside expected range")
            except ValueError:
                errors.append(f"{label}: publication_year must be an integer")
            doi = (row.get("doi") or "").strip()
            if doi and not DOI_RE.match(doi):
                errors.append(f"{label}: DOI format appears invalid: '{doi}'")
            for field in ("official_guideline_url", "open_access_url"):
                val = (row.get(field) or "").strip()
                if val and not URL_RE.match(val):
                    errors.append(f"{label}: {field} must be an https URL")
            if row.get("review_status") == "verified_two_reviewers":
                if row.get("primary_source_verified") != "yes" or row.get("open_access_verified") != "yes":
                    errors.append(f"{label}: two-reviewer verified requires primary source and OA verification=yes")
                if not (row.get("reviewer_1") or "").strip() or not (row.get("reviewer_2") or "").strip():
                    errors.append(f"{label}: two-reviewer verified requires reviewer_1 and reviewer_2")
                if row.get("reviewer_1") == row.get("reviewer_2"):
                    errors.append(f"{label}: reviewer_1 and reviewer_2 must differ")
            if row.get("open_access_verified") == "yes" and not (row.get("open_access_url") or "").strip():
                errors.append(f"{label}: open_access_verified=yes requires open_access_url")
            if row.get("status") == "current" and not (row.get("last_official_status_check") or "").strip():
                warnings.append(f"{label}: current status should have last_official_status_check")
            if row.get("geographic_classification") in {"international_multisociety", "international_panel"}:
                if not (row.get("panel_countries_regions") or "").strip():
                    warnings.append(f"{label}: international classification needs documented panel countries/regions")
    for warning in warnings:
        print("WARNING:", warning)
    for error in errors:
        print("ERROR:", error)
    if errors:
        print(f"Validation failed: {len(errors)} error(s), {len(warnings)} warning(s).")
        return 1
    print(f"Validation passed: {len(rows)} record(s), {len(warnings)} warning(s).")
    return 0

if __name__ == "__main__":
    sys.exit(main())

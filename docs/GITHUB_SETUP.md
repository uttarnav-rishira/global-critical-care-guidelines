# GitHub setup — step by step

These instructions create a public, version-controlled research database using GitHub. You need a GitHub account. You do not need to install Git to start; the GitHub website can upload the files.

## A. Create the repository

1. Sign in at https://github.com/.
2. Select **New repository**.
3. Repository name: `global-critical-care-guidelines`.
4. Description: `Curated open-access register of adult critical-care guidelines and international consensus documents, 2000 onward`.
5. Select **Public** if you want the database to be openly discoverable. Do not upload private patient data or confidential documents.
6. Select **Add a README file** only if creating an empty repository from scratch; if uploading this starter kit, you can leave it unchecked.
7. Choose **MIT License** for the code/schema only. Guideline content remains subject to its own copyright/licence.
8. Select **Create repository**.

## B. Upload the starter files through the website

1. Download and unzip the starter kit.
2. In the new GitHub repository, select **Add file → Upload files**.
3. Drag the *contents* of the unzipped `global-critical-care-guidelines` folder into the upload area. Upload the files and folders, not the outer ZIP.
4. In the commit message enter `Add initial database structure and curation policy`.
5. Commit directly to `main` for the initial setup.
6. Confirm that `README.md`, `data/`, `docs/`, `scripts/`, and `.github/workflows/` appear in the repository.

## C. Enable validation workflow

1. Open the repository's **Actions** tab.
2. If GitHub asks, select **I understand my workflows, go ahead and enable them**.
3. Open **Settings → Actions → General**.
4. Under Workflow permissions, the default read-only permission is sufficient for the supplied validation workflow.
5. The workflow runs when a pull request or push changes `data/guidelines.csv` or the validator.

## D. Configure repository safeguards

Recommended settings:
1. **Settings → General → Pull Requests:** enable pull requests; disable force-pushes on the default branch through branch protection/rulesets.
2. **Settings → Rules → Rulesets** (or **Branches**, depending on GitHub UI): create a ruleset for `main`.
3. Require a pull request before merging.
4. Require the `validate-guidelines` status check.
5. Require at least one approving review; for clinical reference records, use two-person verification in the record itself.
6. Restrict direct pushes to `main` where your plan permits.
7. Enable **Settings → Security → Private vulnerability reporting** if you later add application code.
8. Add a `CODEOWNERS` file if you have designated maintainers.

GitHub features and menu names can change. If a menu differs, use GitHub's current documentation linked below.

## E. Add a guideline record

1. Open `data/guidelines.csv`.
2. Select the pencil icon to edit, or use **Add file → Create new file** only if you are creating a new data file.
3. Add one CSV row using the exact header order. Use double quotes around values containing commas; use semicolons between multiple organisations or subdomains.
4. Never use a line break inside a CSV cell.
5. Save changes on a new branch and open a pull request.
6. Include the primary guideline link, DOI/PMID, access verification, and eligibility rationale in the PR description.
7. Wait for the automated validation to pass and the independent review to be completed.
8. Merge only after approval. The merged Git history is the audit trail.

## F. Download and use the database

- Select `data/guidelines.csv` in GitHub and use **Raw** to retrieve the CSV.
- Download the repository using **Code → Download ZIP**.
- Open the CSV in Excel, LibreOffice, R, or Python.
- For a future searchable website, build a separate front end that reads the curated CSV or a database generated from it. Do not make a clinical decision-support interface without clinical governance and formal validation.

## G. Optional local workflow (Git)

If you use Git locally:

```bash
git clone https://github.com/YOUR-ORG/global-critical-care-guidelines.git
cd global-critical-care-guidelines
python -m pip install -r requirements.txt
python scripts/validate_guidelines.py
```

After editing:

```bash
git checkout -b add-guideline-records
git add data/guidelines.csv
git commit -m "Add verified adult critical care guideline records"
git push -u origin add-guideline-records
```

Then open a pull request on GitHub.

## H. GitHub documentation

- Creating a repository: https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository
- Uploading files: https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository
- GitHub Actions: https://docs.github.com/en/actions
- Branch protection/rulesets: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository
- Pull requests: https://docs.github.com/en/pull-requests

## I. Before public launch

- Confirm the project owner and clinical editorial board.
- Define a reviewer conflict-of-interest declaration.
- Agree a controlled vocabulary and record ID allocation process.
- Pilot the criteria on 20–30 candidate documents across several domains.
- Resolve disagreements and revise the SOP before large-scale screening.
- Publish a search log and a dated versioned release.
- Clearly label the database as a research index, not bedside treatment advice.

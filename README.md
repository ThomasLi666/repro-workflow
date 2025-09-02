# Reproducible Workflow Template

**Author:** Thomas Lee (Lund University)  
**Contact:** thomas.lee@example.com  
**License:** MIT (code), data license per dataset owner

This repository provides a fully reproducible analysis pipeline for a tabular dataset (CSV). It ships with:
- A Jupyter notebook with rich Markdown, equations, code, and **output cells**.
- Pinned dependencies via `environment.yml`.
- CI example for running the notebook on every push.
- FAIR principles section.

## Quickstart (Conda/Mamba)

```bash
mamba env create -f environment.yml
mamba activate repro-workflow
jupyter lab
```

Open `notebooks/workflow.ipynb` and run all cells.

## Data

Place your CSV in `data/raw/data.csv` (already included as a copy of what you uploaded).  
Columns detected on creation:
- **Datetime column:** From the date
- **Numeric columns:** Rainfall

## Results

Generated artifacts are stored in `outputs/`, e.g.:
- `summary_stats.csv`

- figures like histograms, time series, and scatter plots.

## Version pinning & risk assessment

We pin versions with **major.minor wildcards** (e.g., `pandas==2.2.*`) to balance stability and security updates.

**Risks:**
- Upstream breaking changes may land in patch releases.
- Deprecations can affect APIs over time.
- Wheels for some platforms may lag behind.

**Mitigations:**
- CI runs the notebook on pushes/PRs.
- Use `mamba update --all` in a new branch to test upgrades.
- If a break occurs, tighten a pin (e.g., `==2.2.2`) or relax with a tested upper bound.

## FAIR Principles

**Findable:** Repository keywords, clear README, and optional Zenodo DOI (add once published).  
**Accessible:** Public repo, open-source license, data sample provided; instructions for requesting full data if restricted.  
**Interoperable:** Uses open formats (CSV), standard units documented in `data/raw/README.md`.  
**Reusable:** Clear license, provenance notes, and deterministic steps (fixed random seeds if used).

## How to publish to GitHub

1. Create a GitHub repo (e.g., `yourname/repro-workflow`).
2. Initialize and push:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: reproducible workflow"
   git branch -M main
   git remote add origin git@github.com:YOURNAME/repro-workflow.git
   git push -u origin main
   ```

## Citation
If you use this template, please cite via `CITATION.cff`.

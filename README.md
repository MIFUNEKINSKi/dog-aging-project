# Dog Aging Project (DAP) Research & Analysis Repository

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![DAP: 2024 CDR](https://img.shields.io/badge/DAP-2024%20CDR-green.svg)](https://dogagingproject.org)

An open-science research environment and data science toolkit for analyzing longitudinal data from the **Dog Aging Project (DAP)**.

---

## Overview

The [Dog Aging Project](https://dogagingproject.org) is an innovative, nationwide open-data initiative following tens of thousands of companion dogs across their lifespans. This repository provides:
* Automated tools to query, filter, and inspect the **2024 Curated Data Release (CDR)** codebooks (2,900+ variables).
* Pre-configured workflows for analyzing Health and Life Experience Surveys (HLES), physical activity, dietary patterns, and longevity/survival trajectories.
* Secure infrastructure respecting DAP Data Use Agreements (DUA) and privacy governance.

---

## Directory Layout

```text
dog-aging-project/
├── .gitignore                     # Enforces DUA compliance (ignores raw microdata)
├── README.md                      # Project documentation and citation guide
├── requirements.txt               # Data science and survival analysis dependencies
├── data/
│   ├── raw/                       # Downloaded cohort files (.gitignore protected)
│   ├── processed/                 # Feature-engineered analytical datasets
│   └── codebooks/                 # DAP 2024 variable codebooks and dictionaries
├── scripts/
│   ├── fetch_dap_public_data.py   # Ingestion script for public codebooks and cohorts
│   └── explore_codebook.py        # CLI search tool for DAP survey variables
├── notebooks/
│   └── 01_dap_overview_and_eda.ipynb # Initial data dictionary & cohort exploration
└── docs/
    └── terra_onboarding.md        # Step-by-step guide for full Terra platform access
```

---

## Quickstart

### 1. Installation
Clone this repository and install dependencies in a virtual environment:
```bash
git clone https://github.com/MIFUNEKINSKi/dog-aging-project.git
cd dog-aging-project

python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On Linux/macOS:
source .venv/bin/activate

pip install -r requirements.txt
```

### 2. Fetch Codebooks & Open Data
Download the official 2024 DAP Codebook:
```bash
python scripts/fetch_dap_public_data.py --codebooks-only
```
To also download the public 2024 Dog Overview and Survival cohorts (~45 MB):
```bash
python scripts/fetch_dap_public_data.py --all
```

### 3. Search the Codebook
Search across 2,900+ survey questions and variables directly from your terminal:
```bash
python scripts/explore_codebook.py "activity"
python scripts/explore_codebook.py "diet" --limit 10
python scripts/explore_codebook.py --data-file "Dog_Overview"
```

### 4. Interactive Notebooks
Launch Jupyter to explore the datasets:
```bash
jupyter lab
```
Open `notebooks/01_dap_overview_and_eda.ipynb`.

---

## Data Governance & Compliance

Access to full DAP longitudinal microdata is governed by the **Dog Aging Project Data Transfer and Use Agreement (DUA)**:
1. **No Re-identification:** Under no circumstances should users attempt to de-anonymize or contact participating dog owners or dogs.
2. **Data Distribution:** Raw microdata tables are excluded from version control via `.gitignore` and must never be pushed to public Git remotes.
3. **Citation:** In any academic papers, presentations, or software derived from DAP data, cite the Dog Aging Project according to consortium guidelines (see `docs/terra_onboarding.md`).

---

## Citation & Attribution

> Dog Aging Project Consortium. *Dog Aging Project Curated Data Release (2024)*. Supported by the National Institute on Aging (U19AG057377) and private philanthropy. URL: [https://dogagingproject.org](https://dogagingproject.org)

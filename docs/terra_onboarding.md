# Terra Platform Onboarding Guide

This guide outlines the protocol for accessing and syncing Curated Data Releases (CDR) from the Dog Aging Project (DAP) via the Broad Institute's **Terra** platform (`app.terra.bio`).

---

## 1. Compliance & Data Governance Standards

As stipulated in the **Dog Aging Project Data Transfer and Use Agreement (DUA)**:
1. **Never Re-Identify:** Never attempt to identify, unmask, or contact research participants (dog owners) or specific dogs.
2. **Access Control:** Do not redistribute, re-host, or share raw microdata files, derived restricted tables, or Terra credentials with third parties.
3. **Attribution & Citation:** All publications, public code, presentations, or posters derived from this data must properly cite the Dog Aging Project and specify the Curated Data Release version (e.g., 2024 CDR v1.0).
4. **No Commercial Misrepresentation:** DAP data cannot be used to make unvalidated commercial health claims or for discriminatory products.

---

## 2. Setting Up Your Terra Workspace

1. **Sign In:** Go to [app.terra.bio](https://app.terra.bio) and sign in with the Google account approved by DAP.
2. **Accept Consortium Workspace Invite:** Once the DAP Data Management team countersigns your DUA, you will receive an invitation email, and the Dog Aging Project Curated Data workspace will appear under your **Workspaces** dashboard.
3. **Clone Workspace (Recommended):**
   * Click the three dots on the top right of the DAP Workspace and select **Clone**.
   * Give your cloned workspace a descriptive name (e.g., `dap-longevity-analysis`).
   * Select your Google Cloud Billing Account (new Google Cloud users receive \$300 in free credits).

---

## 3. Data Ingestion Options

### Option A: Interactive Analysis inside Terra
* Launch cloud environments directly within Terra (JupyterLab, RStudio, or Hail).
* Benefit: Zero data egress costs, instantaneous access to all tables without downloading tens of gigabytes to your local drive.

### Option B: Local Sync via Google Cloud Storage CLI (`gcloud` / `gsutil`)
If you prefer running analyses locally:
1. Identify the Google Cloud Storage bucket associated with your workspace under the workspace dashboard (e.g., `gs://fc-dap-...`).
2. Download target tables to `data/raw/` using `gcloud storage`:
   ```bash
   gcloud storage cp gs://fc-dap-.../DAP_2024_HLES_dog_owner_v1.0.csv data/raw/
   ```
3. Ensure `.gitignore` remains active so that microdata is never accidentally committed to GitHub.

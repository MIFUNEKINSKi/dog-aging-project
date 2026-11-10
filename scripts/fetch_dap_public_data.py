"""
Dog Aging Project (DAP) - Public Data Ingestion Script

Fetches open-access codebooks and public reference data releases from the
official Dog Aging Project consortium repository.

Usage:
    python scripts/fetch_dap_public_data.py --all
    python scripts/fetch_dap_public_data.py --codebooks-only
"""

import os
import sys
import argparse
import urllib.request

BASE_URL = (
    "https://raw.githubusercontent.com/dogagingproject/"
    "Dog-Aging-Project-Publication-Resources/main/"
    "2026_chiu_factors_associated_with_longevity_in_companion_dog/data/"
)

FILES = {
    "codebooks": [
        (
            "DAP_2024_CODEBOOK_v1.0.csv",
            "data/codebooks/DAP_2024_CODEBOOK_v1.0.csv",
            "DAP 2024 Variable Codebook and Dictionary (~717 KB)"
        )
    ],
    "datasets": [
        (
            "DAP_2024_DogOverview_v1.0.csv",
            "data/raw/DAP_2024_DogOverview_v1.0.csv",
            "2024 Curated Dog Overview Cohort (~20 MB)"
        ),
        (
            "SurvivalData.csv",
            "data/raw/SurvivalData.csv",
            "Curated Longitudinal Survival Dataset (~24 MB)"
        ),
        (
            "U.S._State_Life_Expectancy_by_Sex__2021.csv",
            "data/raw/U.S._State_Life_Expectancy_by_Sex__2021.csv",
            "CDC / US State Life Expectancy Reference (~6 KB)"
        )
    ]
}


def download_file(file_name: str, target_rel_path: str, description: str, project_root: str):
    target_path = os.path.join(project_root, target_rel_path)
    os.makedirs(os.path.dirname(target_path), exist_ok=True)

    if os.path.exists(target_path) and os.path.getsize(target_path) > 0:
        print(f"[SKIP] Already exists: {target_rel_path} ({os.path.getsize(target_path):,} bytes)")
        return

    url = BASE_URL + file_name
    print(f"[DOWNLOADING] {description}...")
    print(f"  URL: {url}")
    print(f"  Destination: {target_rel_path}")

    def report_hook(block_num, block_size, total_size):
        downloaded = block_num * block_size
        if total_size > 0:
            percent = min(100.0, downloaded * 100.0 / total_size)
            sys.stdout.write(f"\r  Progress: {percent:.1f}% ({downloaded:,} / {total_size:,} bytes)")
        else:
            sys.stdout.write(f"\r  Downloaded: {downloaded:,} bytes")
        sys.stdout.flush()

    try:
        urllib.request.urlretrieve(url, target_path, reporthook=report_hook)
        print(f"\n[DONE] Saved to {target_rel_path} ({os.path.getsize(target_path):,} bytes)\n")
    except Exception as e:
        print(f"\n[ERROR] Failed to download {file_name}: {e}\n")
        if os.path.exists(target_path):
            os.remove(target_path)


def main():
    parser = argparse.ArgumentParser(description="Fetch Dog Aging Project open datasets.")
    parser.add_argument(
        "--all",
        action="store_true",
        help="Download both codebooks and datasets (including ~45 MB of CSVs)"
    )
    parser.add_argument(
        "--codebooks-only",
        action="store_true",
        help="Download only data dictionary and codebooks"
    )
    args = parser.parse_args()

    # Determine project root (parent directory of scripts/)
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    print("=" * 70)
    print("Dog Aging Project - Open Data Fetcher")
    print(f"Project Directory: {project_root}")
    print("=" * 70)

    # Always download codebooks
    for fname, rel_path, desc in FILES["codebooks"]:
        download_file(fname, rel_path, desc, project_root)

    # Download full cohorts if requested or defaulted
    if args.all or not args.codebooks_only:
        for fname, rel_path, desc in FILES["datasets"]:
            download_file(fname, rel_path, desc, project_root)

    print("Data ingestion complete!")
    print("Codebooks are available in: data/codebooks/")
    print("Raw cohorts are stored in:  data/raw/")


if __name__ == "__main__":
    main()

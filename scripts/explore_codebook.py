"""
DAP Codebook Explorer CLI

Quickly search variables, survey questions, and value labels in the
Dog Aging Project 2024 Codebook.

Usage:
    python scripts/explore_codebook.py "diet"
    python scripts/explore_codebook.py "activity"
    python scripts/explore_codebook.py --data-file "Dog_Overview"
"""

import os
import sys
import argparse
import csv


def search_codebook(query=None, data_file_filter=None, limit=25):
    codebook_path = os.path.join(
        os.path.dirname(__file__), "..", "data", "codebooks", "DAP_2024_CODEBOOK_v1.0.csv"
    )

    if not os.path.exists(codebook_path):
        print(f"[ERROR] Codebook not found at: {codebook_path}")
        print("Please run: python scripts/fetch_dap_public_data.py --codebooks-only")
        return

    matches = []
    total_rows = 0

    with open(codebook_path, mode="r", encoding="utf-8", errors="replace") as f:
        reader = csv.DictReader(f)
        for row in reader:
            total_rows += 1
            data_file = row.get("DataFile", "")
            var_name = row.get("Variable", "")
            survey_text = row.get("SurveyText", "")
            values = row.get("Values", "")
            labels = row.get("ValueLabels", "")

            if data_file_filter and data_file_filter.lower() not in data_file.lower():
                continue

            if query:
                q = query.lower()
                combined = f"{var_name} {survey_text} {values} {labels}".lower()
                if q not in combined:
                    continue

            matches.append(row)

    print(f"\n[DAP 2024 Codebook Search] Query: '{query or '*'}' | DataFile Filter: '{data_file_filter or '*'}'")
    print(f"Total matching variables: {len(matches)} (out of {total_rows} total variables)\n")

    for i, m in enumerate(matches[:limit]):
        print(f"{i+1:3d}. [{m.get('DataFile')}] {m.get('Variable')}")
        print(f"     Description: {m.get('SurveyText')}")
        if m.get('Values') and m.get('Values') != 'NA':
            print(f"     Values:      {m.get('Values')[:90]}")
        print()

    if len(matches) > limit:
        print(f"... and {len(matches) - limit} more. Use --limit to display more results.\n")


def main():
    parser = argparse.ArgumentParser(description="Search Dog Aging Project 2024 Codebook.")
    parser.add_argument("query", nargs="?", default="", help="Keyword to search in variable names and survey text")
    parser.add_argument("--data-file", help="Filter by data file name (e.g., Dog_Overview, HLES)")
    parser.add_argument("--limit", type=int, default=20, help="Max results to display")
    args = parser.parse_args()

    search_codebook(query=args.query, data_file_filter=args.data_file, limit=args.limit)


if __name__ == "__main__":
    main()

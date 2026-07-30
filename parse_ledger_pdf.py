#!/usr/bin/env python3
"""
parse_ledger_pdf.py
--------------------
Manual, one-off CLI version — useful for testing a new PDF locally before
it's committed. In the repo, this same logic runs automatically on every
push via scripts/auto_parse_jee.py, so you normally won't need to run
this by hand at all.

Usage:
  python3 parse_ledger_pdf.py <pdf_path> <exam_code> <subjects_csv> <max_per_subject> <out_json>

Example:
  python3 parse_ledger_pdf.py 1pujeeparttest1.pdf PT1 PHYSICS,CHEMISTRY,MATHS 100 results_1pujeeparttest1.json
"""
import sys, json
sys.path.insert(0, "scripts")
from ledger_parser_core import parse_pdf_to_results

def main():
    if len(sys.argv) != 6:
        print(__doc__)
        sys.exit(1)
    pdf_path, exam_code, subjects_csv, max_per_subject, out_path = sys.argv[1:]
    subjects = subjects_csv.split(",")
    data = parse_pdf_to_results(pdf_path, exam_code, subjects, max_per_subject)
    if not data["results"]:
        print("WARNING: no rows matched — check the PDF layout / subject count.")
    with open(out_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Wrote {len(data['results'])} student results to {out_path}")

if __name__ == "__main__":
    main()

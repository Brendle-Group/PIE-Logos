#!/usr/bin/env python3
import os
import argparse
import csv
from urllib.parse import quote

def main():
    parser = argparse.ArgumentParser(
        description="Scan a directory and output a CSV of filenames + URL-encoded filenames"
    )
    parser.add_argument(
        "directory",
        help="Path to the Windows directory to scan"
    )
    parser.add_argument(
        "-o", "--output",
        default="files.csv",
        help="Output CSV filename (default: files.csv)"
    )
    args = parser.parse_args()

    # Get only files in the top‐level of the directory
    try:
        entries = os.listdir(args.directory)
    except OSError as e:
        print(f"Error reading directory: {e}")
        return

    files = [
        f for f in entries
        if os.path.isfile(os.path.join(args.directory, f))
    ]

    # Write CSV
    with open(args.output, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["filename", "url_encoded"])
        for fname in files:
            writer.writerow([fname, quote(fname)])

    print(f"Wrote {len(files)} entries to {args.output}")

if __name__ == "__main__":
    main()

# py generate_url_names.py "C:\Users\BGDatabaseService\Documents\PIE-Logos\Colorado" -o output.csv

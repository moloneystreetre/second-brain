#!/usr/bin/env python3
"""Append one day's investing.com NGX screener tables to the master Excel files.

Usage:
    python3 tools/ngx_extract_append.py CAPTURE.json MASTER_DIR [--date YYYY-MM-DD] [--dry-run]

CAPTURE.json holds the three screener tabs as read from the page:
    {"date": "2026-11-24",
     "valuation":  {"headers": [...], "rows": [[...], ...]},
     "technical":  {"headers": [...], "rows": [[...], ...]},
     "financials": {"headers": [...], "rows": [[...], ...]}}

Headers and cells are the page text as shown (e.g. "NGN 79.40", "Upgrade to Pro+"),
which is what copy-and-paste from the screener produces. The "Company" column
(a repeat of the symbol) is dropped. Each row is written as:
    Date | <tab columns in page order> | Exchange (blank)

MASTER_DIR holds ngx_valuation.xlsx, ngx_technical.xlsx and ngx_financials.xlsx.
A timestamped .bak copy of each file is made before it is changed.

Checks (the script stops and changes nothing if any fail):
  - the date is not already in the master file
  - the page columns match the master's columns (blank master headers match anything)
  - row count is within 10% of the last day's count
  - no header rows mixed into the data, no blank names or symbols, no duplicate symbols
"""
import argparse
import datetime as dt
import json
import shutil
import sys
from pathlib import Path

import openpyxl

TABS = {
    "valuation": "ngx_valuation.xlsx",
    "technical": "ngx_technical.xlsx",
    "financials": "ngx_financials.xlsx",
}
NUMERIC_TEXT_KEEP = ("NGN", "₦", "x", "%", "Upgrade")


def clean(cell):
    """Turn page text into the same kind of value a paste into Excel gives."""
    if cell is None:
        return None
    s = str(cell).strip()
    if s in ("", "-", "--", "N/A"):
        return None
    if s.endswith("%") and not any(c.isalpha() for c in s):
        # A paste into Excel turns "5.8%" into 0.058; the master files hold these as numbers.
        try:
            return round(float(s[:-1].replace(",", "")) / 100, 10)
        except ValueError:
            return s
    if any(k in s for k in NUMERIC_TEXT_KEEP) or any(c.isalpha() for c in s):
        return s  # keep as text, like the existing files
    try:
        f = float(s.replace(",", ""))
        return int(f) if f.is_integer() else f
    except ValueError:
        return s


def check_and_build(name, tab, master_path, day):
    errors = []
    wb = openpyxl.load_workbook(master_path)
    ws = wb.worksheets[0]
    master_headers = [c.value for c in ws[1]]
    body_headers = master_headers[1:-1]  # drop Date and Exchange

    page_headers = [h.strip() for h in tab["headers"]]
    drop = page_headers.index("Company") if "Company" in page_headers else None
    if drop is not None:
        page_headers.pop(drop)
    if len(page_headers) != len(body_headers):
        errors.append(f"{name}: page has {len(page_headers)} columns, master expects {len(body_headers)}")
    else:
        for i, (p, m) in enumerate(zip(page_headers, body_headers)):
            if m is not None and p != m:
                errors.append(f"{name}: column {i + 2} is '{p}' on the page but '{m}' in the master")

    rows = []
    for r in tab["rows"]:
        r = list(r)
        if drop is not None:
            r.pop(drop)
        rows.append([day] + [clean(c) for c in r] + [None])

    # existing dates and last day's count
    counts = {}
    for (d,) in ws.iter_rows(min_row=2, max_col=1, values_only=True):
        if isinstance(d, dt.datetime):
            counts[d.date()] = counts.get(d.date(), 0) + 1
    if day.date() in counts:
        errors.append(f"{name}: {day.date()} is already in the master file")
    if counts:
        last = counts[max(counts)]
        if abs(len(rows) - last) > 0.1 * last:
            errors.append(f"{name}: {len(rows)} rows today vs {last} on {max(counts)} (more than 10% apart)")

    symbols = [r[2] for r in rows]
    if any(r[1] in ("Name", None) or r[2] in ("Symbol", None) for r in rows):
        errors.append(f"{name}: header row or blank name/symbol found in the data")
    dupes = {s for s in symbols if symbols.count(s) > 1}
    if dupes:
        errors.append(f"{name}: duplicate symbols {sorted(dupes)[:5]}")
    return wb, ws, rows, errors


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("capture")
    ap.add_argument("master_dir")
    ap.add_argument("--date")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    cap = json.loads(Path(a.capture).read_text(encoding="utf-8"))
    day = dt.datetime.strptime(a.date or cap["date"], "%Y-%m-%d")
    master_dir = Path(a.master_dir)

    built, all_errors = {}, []
    for name, fname in TABS.items():
        if name not in cap:
            all_errors.append(f"{name}: missing from capture")
            continue
        wb, ws, rows, errors = check_and_build(name, cap[name], master_dir / fname, day)
        built[name] = (wb, ws, rows, master_dir / fname)
        all_errors += errors

    if all_errors:
        print("STOPPED, nothing written:")
        print("\n".join("  - " + e for e in all_errors))
        sys.exit(1)

    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M")
    for name, (wb, ws, rows, path) in built.items():
        print(f"{name}: {len(rows)} rows for {day.date()}")
        if a.dry_run:
            continue
        shutil.copy2(path, path.with_suffix(f".{stamp}.bak"))
        for r in rows:
            ws.append(r)
            ws.cell(row=ws.max_row, column=1).number_format = "mm-dd-yy"  # Excel built-in short date: shows dd/mm/yyyy on a UK PC, same as earlier rows
        wb.save(path)
    print("DRY RUN, nothing written." if a.dry_run else "Saved.")


if __name__ == "__main__":
    main()

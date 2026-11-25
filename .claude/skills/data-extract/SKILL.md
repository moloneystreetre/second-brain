---
name: data-extract
description: Pull the day's NGX data from the investing.com stock screener (Valuation, Technical and Financials tabs) and append it to Yinka's three master Excel files. Use Monday to Friday 18:00-19:00 London time, or when Yinka says "data extract", "pull today's data" or "do the extract".
---

# NGX Data Extract

Pulls the investing.com stock screener for every NGX-listed stock and adds today's rows to the three master files that feed the ~21:30 moloneystreetre.com update. The later steps (platform update, social posts) all depend on this being right, so accuracy beats speed.

## When it runs
Monday to Friday, 18:00-19:00 London time, after the NGX close. Skip NGX public holidays (the screener will show the previous day's prices; flag it to Yinka rather than saving a duplicate day).

## Source
- Page: https://uk.investing.com/stock-screener
- Country filter: **NG** (Primary Listing: Nigeria, NGX). No other filters. Expect about **143 stocks** (141 until 24 Nov 2026; AIRTELAFRI and SEPLAT appeared on 25 Nov).
- Tabs, in this order: **Valuation**, **Technical**, **Financials**.
- Use the built-in browser on Yinka's computer (site already allowed). If a cookie banner appears, choose the option that declines non-essential cookies.

## Master files
| Tab | File | Sheet |
|---|---|---|
| Valuation | `ngx_valuation.xlsx` | NGX_Valuation |
| Technical | `ngx_technical.xlsx` | NGX_Technicals |
| Financials | `ngx_financials.xlsx` | NGX_Financials |

Folder on Yinka's computer: `C:\Users\odbal\MoloneyStreetRe\data\ngx` (approved for this project). The same folder holds the daily NGX exchange files (`NGX_DD_MM_YYYY.xlsx`), `ngx_companies.xlsx` and the `_cache/` used by the scanner; don't touch those. `scanner/scripts/ngx_composite_score.py` reads the three files below, so their columns and cell style must not change. One row per stock per day. Columns: **Date**, then the tab's columns in page order (Name, Symbol, ...), then **Exchange** (left blank, as in recent rows). Cells keep the page text exactly: `NGN 79.40`, `16x`, `Upgrade to Pro+`.

## Steps
1. Open the screener, set the country to NG, and confirm the stock count (about 141).
2. For each tab (Valuation, Technical, Financials):
   - Click the tab and wait for the table to load.
   - Load **every** row: the table is paged, 30 rows a page. Click page `1` in `[data-test=stocks-pagination]`, then `[data-test=companies-next-button]` until the first row stops changing.
   - Read the header cells and every row's cells from the table (JavaScript `innerText` on `thead th` and each `tbody tr`'s children; the first cell is a `th`), as text.
   - Switch views with the row "Overview | Insights | Valuation | Returns | Technical | Financials ..." (not the "Popular | Price | Valuation ..." filter chips). Wait ~5s after switching before reading, or values can be stale.
3. To get the capture off the page without retyping it, build the JSON in the page and trigger a Blob download (`ngx_capture_YYYY-MM-DD.json`); it lands in `C:\Users\odbal\Downloads` (request that folder once), then stage it. Save the capture as `projects/platform-enhancement/extracts/YYYY-MM-DD.json` in the format the script expects (see the top of `tools/ngx_extract_append.py`).
4. Check Excel isn't holding the files: if a fresh `~$ngx_*.xlsx` lock file is in the folder (today's date), ask Yinka to close Excel first. (An old one from 7 Nov is stale; ignore it.)
5. Stage the three master files into the container (`device_stage_files`, note each `mtimeMs`), then run a dry run first:
   `python3 tools/ngx_extract_append.py CAPTURE.json MASTER_DIR --dry-run`
6. If it passes, run it again without `--dry-run`, then copy the three updated files back with `device_commit_files`, passing each file's `expectedMtimeMs` so nothing Yinka changed in the meantime is overwritten. Before that, commit a dated copy of each original into `C:\Users\odbal\MoloneyStreetRe\data\ngx\_backups\` (an October technical file was corrupted once, so always keep the backup).
7. If the script stops, **do not force it**. Tell Yinka exactly which check failed (column change, wrong row count, duplicate date, header row in the data).
8. Post a short summary in the thread (format below).

## Quality checks (the script enforces these)
- Today's date is not already in the file (no double runs).
- Page columns match the master's columns. If investing.com renames, adds or drops a column, stop and ask.
- Row count within 10% of the previous day's count.
- No header rows pasted into the data, no blank names or symbols, no duplicate symbols.

Also eyeball before saving: prices actually changed from yesterday for most stocks (if nothing moved, the page may be stale or it was a holiday).

## Summary to Yinka (short)
```
Data extract done: 24 Nov 2026 (Tue), 141 stocks x 3 tabs, saved.
Market cap leaders: DANGCEM NGN 22.16T, MTNN NGN 17.54T, ...
Biggest movers vs yesterday: (top 3 up, top 3 down by Last Trade Price)
Flags: (anything odd, or "none")
```
This summary is also the figure check for the `daily-social-posts` skill later in the evening.

## Rules
- Data only: no commentary, no buy or sell views, in the summary or the files.
- Never invent or fill a missing value. Leave it blank exactly as the page shows it.
- Never edit or delete past rows. If an earlier day is wrong, tell Yinka and fix it only with a go-ahead.
- Percentages are stored as numbers, the way an Excel paste does it (`5.8%` -> 0.058); the script converts them.
- Fields marked `Upgrade to Pro+` are paywalled on the free account. Keep them as they are.

## Known history in the files
- Feb to Oct 2026 rows use `₦` and zeros for paywalled fields, and fill Exchange with `NGX`. From November 2026 rows use `NGN`, `Upgrade to Pro+` and a blank Exchange. New rows follow the newer style.
- 15 Oct 2026 in the Valuation file has a header row and a sector in the Exchange column, from a paste. Leave it; flag if a clean-up is wanted.

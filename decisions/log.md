# Decision Log

Append-only. When a meaningful decision is made, log it here.

Format: [YYYY-MM-DD] DECISION: ... | REASONING: ... | CONTEXT: ...

---
[2026-11-24] DECISION: Data extract reads the investing.com screener table (NG, Valuation/Technical/Financials) in the built-in browser and appends to the three master Excel files via tools/ngx_extract_append.py, keeping the current page-text cell style | REASONING: Matches Yinka's existing copy-paste files so the platform update isn't disturbed; the script blocks double runs, column changes and bad row counts | CONTEXT: data-extract skill build
[2026-11-24] DECISION: No AI voiceover for now; until Yinka records, videos are no-voice (text/card reels, captioned screen guides). | REASONING: These formats performed strongly in the competitor research and carry no trust risk with a finance audience. | CONTEXT: Competitor research thread; Yinka chose this on the decision card.

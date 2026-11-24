# Decision Log

Append-only. When a meaningful decision is made, log it here.

Format: [YYYY-MM-DD] DECISION: ... | REASONING: ... | CONTEXT: ...

---
[2026-11-24] DECISION: Data extract reads the investing.com screener table (NG, Valuation/Technical/Financials) in the built-in browser and appends to the three master Excel files via tools/ngx_extract_append.py, keeping the current page-text cell style | REASONING: Matches Yinka's existing copy-paste files so the platform update isn't disturbed; the script blocks double runs, column changes and bad row counts | CONTEXT: data-extract skill build
[2026-11-24] DECISION: Comment replies are drafted by the comment-replies skill and only posted after Yinka approves; YouTube replies are posted via vidIQ, other platforms are copy and paste. Advice-seeking comments ("should I buy X?") always get the method, never an answer. | REASONING: Education-only compliance (not FCA/SEC authorised); every reply nudges toward the free sign-up and every question feeds the video ideas bank | CONTEXT: comment-replies skill build

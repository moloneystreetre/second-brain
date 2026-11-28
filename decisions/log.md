# Decision Log

Append-only. When a meaningful decision is made, log it here.

Format: [YYYY-MM-DD] DECISION: ... | REASONING: ... | CONTEXT: ...

---
[2026-11-24] DECISION: Data extract reads the investing.com screener table (NG, Valuation/Technical/Financials) in the built-in browser and appends to the three master Excel files via tools/ngx_extract_append.py, keeping the current page-text cell style | REASONING: Matches Yinka's existing copy-paste files so the platform update isn't disturbed; the script blocks double runs, column changes and bad row counts | CONTEXT: data-extract skill build
[2026-11-24] DECISION: No AI voiceover for now; until Yinka records, videos are no-voice (text/card reels, captioned screen guides). | REASONING: These formats performed strongly in the competitor research and carry no trust risk with a finance audience. | CONTEXT: Competitor research thread; Yinka chose this on the decision card.
[2026-11-24] DECISION: Comment replies are drafted by the comment-replies skill and only posted after Yinka approves; YouTube replies are posted via vidIQ, other platforms are copy and paste. Advice-seeking comments ("should I buy X?") always get the method, never an answer. | REASONING: Education-only compliance (not FCA/SEC authorised); every reply nudges toward the free sign-up and every question feeds the video ideas bank | CONTEXT: comment-replies skill build
[2026-11-28] DECISION: Daily lesson reels are now voiced with Yinka's cloned vidIQ voice in the long-video brand style (picture per scene, slow zoom, captions, no level badges), via the voiced-reel skill and tools/voiced_reel.py; default 3 a week. Replaces the 2026-11-24 no-voice decision. | REASONING: The cloned voice went live on 28 Nov; about 180 vidIQ credits per reel caps a sustainable cadence on the Boost plan | CONTEXT: Yinka asked to revisit the daily videos waiting for the voice; batch 1 (text-only) had already posted 25-27 Nov
[2026-11-28] DECISION: Voiced reels go out every weekday (Mon-Fri, 22:15 London), replacing the 3-a-week default logged earlier today. | REASONING: Yinka upgraded vidIQ to Max (about 6,000 credits a month), which covers about 22 reels a month at ~200 credits each | CONTEXT: Yinka said "I have upgraded to Max" in project chat

---
name: daily-social-posts
description: Turn tonight's moloneystreetre.com platform update (today.html) into ready-to-approve posts for WhatsApp Status and Channels, Instagram, Threads, Facebook, LinkedIn, X, TikTok and YouTube. Use Monday to Friday after the ~21:30 update, or when Yinka says "do tonight's posts", "write the daily posts" or "post the update".
---

# Daily Social Posts

Turns the weekday platform update into one draft post per platform, all pointing people to www.moloneystreetre.com. Goal: drive subscribers toward 1,000 by March 2027.

## When it runs
Monday to Friday, after the ~21:30 platform update (London time). Never write posts from data older than today's update.

## Inputs
1. **Today's platform update** at https://moloneystreetre.com/today.html. Read the page; if it can't be fetched or still shows yesterday's date, ask Yinka to paste it. Needed: what changed on the platform tonight and the day's key NGX figures (index close and % move, top gainers and losers, volume, any notable news).
2. **Today's data extract** from investing.com (the 18:00-19:00 pull), if available, to check every figure.
3. **Day of the week**, which sets the theme (see below).

If a figure is missing, write `[NUMBER: what is needed]`. Never fill a number from memory.

## Weekday themes
| Day | Angle |
|---|---|
| Monday | Week ahead: what to watch on the NGX, plus a beginner tip |
| Tuesday | Explain one move from today's data in plain words |
| Wednesday | Midweek check: a chart or stat worth understanding |
| Thursday | Myth or rumour test: how to check a tip before acting on it |
| Friday | The week on the NGX in numbers, plus a pointer to the platform |

## Steps
1. Read the update and pull out **one** main idea for the day. One idea per post.
2. Check each figure against the data extract. Flag anything that doesn't match.
3. Write the five posts using the platform formats below.
4. Run the compliance check (below). Fix anything that fails.
5. Save to `projects/content-and-marketing/posts/YYYY-MM-DD.md` using the output format.
6. WhatsApp is posted as **cards**, not text. Write a spec JSON and run `python3 tools/make_whatsapp_cards.py SPEC.json OUTDIR` to make `YYYY-MM-DD_HHMM_status-card.png` (1080x1920, for Status) and `YYYY-MM-DD_HHMM_channel-card.png` (1080x1350, for both Channels). Save both, plus a short caption file `YYYY-MM-DD_HHMM_whatsapp.txt` (one line + link), to `C:\Users\odbal\OneDrive\PA MoloneyStreetRe\whatsapp\` (London time of the run).
7. Show Yinka the drafts and ask for the go-ahead with an Approve / Change something decision card (see `.claude/rules/approvals.md`), never by asking Yinka to type "go". If a Drive share is needed, ask for it on a card too ("I've shared it" / "Post it myself tonight"). **Never post without it.** The Drive files live in the odbalogun@gmail.com Google account, so Yinka must be signed into that account to see Share.
8. After approval: build the reel, schedule Instagram, Facebook and TikTok via Metricool, then **notify Yinka in the thread that posting is done**, with the planner links and the WhatsApp file name.

Runs automatically every weekday at 21:45 London time as a scheduled task.

## House card style
Yinka's posts use a branded card (see `references/examples/weekly-street-note-linkedin-2026-W47.png`). For each day, also draft the card text:
- Small label (e.g. DAILY STREET NOTE / WEEKLY STREET NOTE)
- Title with date (e.g. "The Daily Street Note · 23 Nov 2026"; weekly uses week number, "W47")
- One summary paragraph of 2-4 sentences: what moved, which sectors, why
- Signal chips: counts of **Strong**, **rising** and **falling** names from the platform
- Link to the relevant moloneystreetre.com page
- Hashtags: #NGX #NigerianStocks #MSReAnalytics #Investing
- Button line: "Subscribe for the full brief → moloneystreetre.com"
- Footer line: "Research and education, not personal advice."
Colours: forest green header (#1E3F11 to #122A0C), white title, cream/light body, gold accents (#D4A85A).

## Reel with music (Instagram, Facebook, TikTok)
Still images can't carry music, so each day's card also becomes a 15-second vertical reel:
1. Save the card image (e.g. `projects/content-and-marketing/posts/YYYY-MM-DD-card.png`).
2. Run `python3 tools/card_to_reel.py CARD.png OUT.mp4 references/music/msre-fusion-30s.mp3` (needs ffmpeg and Pillow). It puts the card on the forest-green background with a slow zoom, the site URL, the disclaimer line and the house Afrobeat fusion track.
3. Post it as an Instagram Reel, a Facebook Reel and a TikTok video. YouTube can take it as a Short.
4. Music is MoloneyStreetRe's own AI-generated track (vidIQ). For longer videos (up to about 2 min 50 s) use `references/music/msre-fusion-171s.mp3`. Never use platform "trending" commercial songs on a business account.

## Posting via Metricool
- Brand blogId 8233421, timezone Europe/London. Linked: Facebook, Instagram, TikTok, YouTube. Not linked: LinkedIn, X, Threads. WhatsApp is always copy and paste.
- Media must be a public URL. Upload the reel with Google Drive `create_file` into the Drive folder "MoloneyStreetRe - Metricool uploads" (id `1xfiMFZQB2WFhAtqv5btVqD-lXfAfaMhk`, parentId). Yinka shared that folder once as "Anyone with the link", so files inside should inherit it. On 24 Nov 2026 new uploads did not inherit it (Metricool could not read them), so after uploading, run Google Drive `share_file` with permissionId `anyoneWithLink`, role `reader` on each file before scheduling. If that share is blocked (a permission prompt or the classifier can refuse it, especially in scheduled runs), don't keep retrying. Tell Yinka in the thread which file needs sharing, with its Drive link, and ask them to set it to "Anyone with the link" (or to re-share the whole folder so new files inherit it). Schedule once that's done. Metricool copies the video when it schedules, so the Drive link only needs to work at that moment.
- TikTok posts need `tiktokData.title`. YouTube Shorts need `youtubeData` with title, type `short` and `madeForKids` false. Upload from /home/user (file reference needs a local path).
- Only schedule after Yinka approves the drafts. Schedule a few minutes ahead and share the planner links.

## Platform formats
Account links are in `references/social-accounts.md`.
- **WhatsApp Status:** 1-2 lines plus the card image. Short and punchy.
- **WhatsApp Channels (both):** 3-5 short lines, the key figure up front, link at the end. Conversational. Same text goes to both channels.
- **Instagram:** caption with a scroll-stopping first line, 80-150 words, line breaks, 5-8 hashtags at the end. Suggest the image or carousel text (max 2 lines per slide).
- **Facebook:** 60-120 words, a question at the end to invite comments, link in the body.
- **LinkedIn:** 120-200 words, more analytical, aimed at diaspora professionals. 3 hashtags max.
- **Threads:** 1-3 short sentences, a hook or question, link. No more than 2 hashtags.
- **X (@StreetMolo46005):** under 280 characters including link, 1-2 hashtags.
- **TikTok (@moloneystreet):** caption under 150 characters plus 3-5 hashtags, and a 15-30 second talking-point outline (hook, one point, call to action) Yinka can record.
- **YouTube:** a Shorts title (under 60 characters) and description (2-3 lines + link + hashtags), reusing the TikTok outline. Skip on days with no video.

Core hashtags: #NGX #NigerianStocks #MSReAnalytics #Investing. Rotate in #NigerianExchange #InvestingInNigeria #MoloneyStreetRe.

## Voice
Professional with some humour (see `.claude/rules/public-content.md`). Plain English a beginner can follow, explain any jargon, credible enough for experienced traders. Every post ends with a call to action to moloneystreetre.com.

## Compliance check (must pass before showing drafts)
MoloneyStreetRe is not authorised by the FCA (UK) or SEC Nigeria, so every post is education only.
- No buy, sell or hold calls. No price targets. No "guaranteed", "risk-free", "can't lose", "to the moon", "double your money".
- Any named stock is an example of the data or a method, never a recommendation.
- If a real stock or past performance appears, include: "Research and education, not personal advice." and, for past performance, "Past performance is not a reliable guide to future results." In the post body, not just a link.
- Any benefit mentioned is paired with its main risk.
- No promotion of brokers, apps, crypto or schemes.
- Every figure has a source (moloneystreetre.com data or investing.com), recorded internally only; never named in public text.

## Sources in public text (Yinka, 27 Nov 2026; replaces the 26 Nov logo rule)
- Follow "Sources in public content" in `.claude/rules/public-content.md`: no source names and no source logos anywhere public (card, WhatsApp cards, all captions). NGX information is stated as market data or MSRe data.
- Do not pass `sources=` to `tools/make_card.py` or `"sources"` in the WhatsApp spec. (The logo option is kept in the tools but switched off.)
- Every source still goes in the **Source figures** line of the posts file (internal only).

## Output format
```markdown
# Social posts: YYYY-MM-DD (Day)
**Main idea:**
**Source figures:** (each figure + source)
**Compliance:** PASS / notes

## Card text
## WhatsApp Status
## WhatsApp Channels
## Instagram
(caption) / Image or carousel text:
## Facebook
## LinkedIn
## Threads
## X
## TikTok
Caption: / Video outline:
## YouTube
Title: / Description:
```

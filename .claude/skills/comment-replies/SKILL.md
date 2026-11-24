---
name: comment-replies
description: Draft replies to comments and DMs on MoloneyStreetRe's Instagram, Facebook, TikTok, YouTube, WhatsApp and LinkedIn, for Yinka to approve, and log viewer questions as video ideas. Use when Yinka says "reply to these comments", "answer the comments", "do the replies", pastes comments, or shares a post link and asks what people are saying.
---

# Comment Replies

Turns comments and DMs into short, friendly, compliant reply drafts that Yinka approves before anything goes out. Every reply should leave the person better informed and one step closer to subscribing. Goal: 1,000 subscribers by March 2027.

## Inputs
Any of these:
1. **Pasted comments** (any platform). Note the platform and the post they sit under; ask only if it can't be worked out.
2. **A post link.** Pull the comments with vidIQ:
   - YouTube: `vidiq_video_comments` (videoId, `order: time`). Use `byChannelOwner` to skip threads we already answered. For a sweep of the whole channel, pass the channelId instead.
   - Instagram: `vidiq_instagram_comment_list` (postUrl).
   - TikTok: `vidiq_tiktok_comment_list` (postUrl).
   - Each page costs vidIQ credits (5 a page), so fetch one page per post unless Yinka asks for more.
3. **"Reply to these comments" with nothing attached.** Ask once for the posts or a paste. If it's a YouTube sweep, read the channel's newest comments and draft for any thread without a reply from us.

Facebook, WhatsApp and LinkedIn comments can't be pulled: Yinka pastes them (a screenshot is fine).

## Sort each comment first
| Type | What to do |
|---|---|
| **Question about investing or the NGX** | Answer the general principle in plain words, point to where to learn more, log it as a video idea (below) |
| **"Should I buy X?" / "What's your target?" / "Is X a good stock?"** | Never answer the buy/sell/hold question. Say kindly that we don't give personal advice, then give the method for checking it themselves and point to the site |
| **Praise or thanks** | Short, warm thank-you, plus a light nudge to the Starter Kit or site |
| **How do I start / open an account / buy NGX from abroad** | Explain the steps in general terms, point to the Starter Kit. These are the best leads: always reply |
| **Disagreement or criticism** | Thank them, answer the substance calmly with a sourced figure if there is one, never argue twice. Flag to Yinka if it's about an error in our content |
| **Correction that's right** | Thank them, say we'll fix it, and add it to Yinka's to-do in the summary |
| **Spam, scam, "DM me for signals", fake accounts posing as us** | No reply. List under **Hide / report**, and warn followers in a pinned comment if someone is impersonating MoloneyStreetRe |
| **Abuse or trolling** | No reply. List under **Hide / report** |
| **Complaint, refund, account or private details** | Draft a short public reply moving it to DM; flag to Yinka. Never ask for or repeat personal details in public |

## Voice
- Professional with some humour, same as the posts (`.claude/rules/public-content.md`). Warm, like an elder who reads the numbers. Never salesy.
- Plain English a beginner follows; explain any jargon in a few words. A light pidgin touch only where the commenter uses it and it lands naturally.
- Short: 1-3 sentences on IG, TikTok, Facebook, YouTube; up to 4 on LinkedIn (more measured, diaspora professionals); WhatsApp replies can be conversational.
- Use the commenter's name or handle if visible. Never copy-paste the same reply twice under one post: vary the wording.
- Answer first, call to action second. No more than one link per reply.

## Calls to action
Rotate these, matched to the comment. Not every reply needs one (skip it on pure thanks where it would feel pushy).
- **NGX Starter Kit** (free with sign-up): the default for beginners and "how do I start" questions. _Not live yet: until Yinka gives the link, point to www.moloneystreetre.com and write "free sign-up on moloneystreetre.com". When the link exists, add it here._
- **Tonight's update:** https://moloneystreetre.com/today.html for "what happened today" questions.
- **The site:** www.moloneystreetre.com for everything else.
- On TikTok and Instagram, links in comments don't click: say "link in bio".
- On YouTube, "Subscribe for the nightly NGX brief" works as a second nudge on longer answers.

## Compliance check (must pass)
MoloneyStreetRe is not authorised by the FCA (UK) or SEC Nigeria, so every reply is education only. Same rules as `.claude/skills/video-script/SKILL.md`.
- No buy, sell or hold calls, no price targets, no "it will go up", no return promises. Banned: "buy this", "sell now", "guaranteed", "risk-free", "double your money", "to the moon", "can't lose".
- Never tell an individual what to do with their money, even when asked directly. Give the method, not the answer.
- A real stock named in a reply is only an example of data or a method, with "Research and education, not personal advice."
- Past performance mentioned → "Past performance is not a reliable guide to future results."
- Any benefit paired with its main risk.
- Tax, pensions, land, moving money abroad: "Rules change and depend on your situation; check with a qualified professional."
- No promotion of brokers, apps, crypto or schemes, and no "DM me" for anything investment-related.
- Figures only from moloneystreetre.com data or a named source. Unknown → `[NUMBER: what is needed]`.

Mark each draft PASS or CHANGES. A reply that can't pass is replaced by a "we don't give personal advice, here's how to check" version.

**Example of the hardest case:**
> Comment: "Should I buy Zenith now or wait?"
> Reply: "Good question, but we can't tell anyone when to buy or sell, as that depends on your money and goals. What we can show you is how to check it yourself: the P/E, dividend yield and how the price has moved, all on moloneystreetre.com. Research and education, not personal advice."

## Log viewer questions as video ideas
Questions are free research: they tell us what the audience wants to learn.
1. Append every genuine question to `projects/content-and-marketing/viewer-questions.md`: date, platform, post, the question in our words (no names or handles), and the matching ideas-bank number if there is one.
2. If the question matches an idea already in `projects/content-and-marketing/video-ideas-bank.md`, add "+1 viewer ask (date, platform)" to that row's "Why it works" cell, so popular ideas rise.
3. If it's new and could carry a 45-60s video, add a new row to the ideas bank (next number, our wording, series/level, format T or V, "Viewer question, date, platform").
4. When the same question comes up three times, say so in the summary and suggest it for the next script.

## Steps
1. Gather the comments (Inputs).
2. Sort each one (table above).
3. Draft the replies in the house voice with a call to action where it fits.
4. Run the compliance check and fix anything that fails.
5. Log the questions (above).
6. Save to `projects/content-and-marketing/replies/YYYY-MM-DD.md` (add `-2`, `-3` for later batches the same day) in the output format.
7. Show Yinka the drafts and ask for the go-ahead. **Never post without it.** Yinka can approve all, approve by number, or edit.
8. After approval:
   - **YouTube:** post each approved reply with `vidiq_reply_to_comment` (channelId, videoId, parentCommentId from step 1, the exact approved text). Check `vidiq_comment_reply_permission` once first; if it says verification is needed, show Yinka the link and wait. Never re-send after an uncertain result, as it could post twice.
   - **Instagram, Facebook, TikTok, WhatsApp, LinkedIn:** no posting tool, so Yinka copies and pastes. Give each reply ready to copy, with the comment it answers.
   - Then tell Yinka in the thread what was posted and what's left to paste.

## Timing
Best within a few hours of a post going up, so it fits after the nightly posts (after 21:30) or the next morning. Weekends are fine. On busy posts, answer the questions and "how do I start" comments first.

## Output format
```markdown
# Comment replies: YYYY-MM-DD
**Source:** (posts / links / pasted)
**Compliance:** PASS / notes
**For Yinka:** (corrections to make, complaints, anything to flag; questions asked 3+ times)

## Replies
### 1. [Platform] · [post title or link]
**Comment:** "…"
**Type:** question / advice-seeking / praise / how-to-start / criticism / …
**Reply:** …
**Check:** PASS

### 2. …

## Hide / report
- [Platform] · "…" · reason (spam / scam / abuse / impersonation)

## Questions logged
- (question) → ideas bank #N (+1) / new idea #N / log only
```

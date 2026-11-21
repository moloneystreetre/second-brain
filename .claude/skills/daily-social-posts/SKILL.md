---
name: daily-social-posts
description: Turn tonight's moloneystreetre.com platform update into ready-to-approve posts for WhatsApp, Instagram, Facebook, LinkedIn and TikTok. Use Monday to Friday after the ~21:30 update, or when Yinka says "do tonight's posts", "write the daily posts" or "post the update".
---

# Daily Social Posts

Turns the weekday platform update into one draft post per platform, all pointing people to www.moloneystreetre.com. Goal: drive subscribers toward 1,000 by March 2027.

## When it runs
Monday to Friday, after the ~21:30 platform update (London time). Never write posts from data older than today's update.

## Inputs
1. **Today's platform update.** Ask Yinka to paste it, or read it from the file or page Yinka points to. Needed: what changed on the platform tonight and the day's key NGX figures (index close and % move, top gainers and losers, volume, any notable news).
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
6. Show Yinka the drafts. **Never post anything.** Yinka approves and posts.

## Platform formats
- **WhatsApp:** 3-5 short lines, the key figure up front, link at the end. Conversational.
- **Instagram:** caption with a scroll-stopping first line, 80-150 words, line breaks, 5-8 hashtags at the end. Suggest the image or carousel text (max 2 lines per slide).
- **Facebook:** 60-120 words, a question at the end to invite comments, link in the body.
- **LinkedIn:** 120-200 words, more analytical, aimed at diaspora professionals. 3 hashtags max.
- **TikTok:** caption under 150 characters plus 3-5 hashtags, and a 15-30 second talking-point outline (hook, one point, call to action) Yinka can record.

Core hashtags to rotate: #NGX #NigerianStocks #NigerianExchange #InvestingInNigeria #MoloneyStreetRe

## Voice
Professional with some humour (see `.claude/rules/public-content.md`). Plain English a beginner can follow, explain any jargon, credible enough for experienced traders. Every post ends with a call to action to moloneystreetre.com.

## Compliance check (must pass before showing drafts)
MoloneyStreetRe is not authorised by the FCA (UK) or SEC Nigeria, so every post is education only.
- No buy, sell or hold calls. No price targets. No "guaranteed", "risk-free", "can't lose", "to the moon", "double your money".
- Any named stock is an example of the data or a method, never a recommendation.
- If a real stock or past performance appears, include: "Research and education, not personal advice." and, for past performance, "Past performance is not a reliable guide to future results." In the post body, not just a link.
- Any benefit mentioned is paired with its main risk.
- No promotion of brokers, apps, crypto or schemes.
- Every figure has a source (moloneystreetre.com data or investing.com).

## Output format
```markdown
# Social posts: YYYY-MM-DD (Day)
**Main idea:**
**Source figures:** (each figure + source)
**Compliance:** PASS / notes

## WhatsApp
## Instagram
(caption) / Image or carousel text:
## Facebook
## LinkedIn
## TikTok
Caption: / Video outline:
```

---
name: video-script
description: Write a ready-to-record MoloneyStreetRe short-video script (45-60s) in Yinka's voice, with on-screen text, captions and a compliance check. Use when Yinka says "script a video", "write a video on X", "turn today's brief into a video", or names a topic for a short.
---

# Video Script

Turns a topic or the day's brief into a short video Yinka can record in one take, then edit into a reel with the house Afrobeat sound.

## Inputs
- **Topic**, or "today's brief" (read https://moloneystreetre.com/today.html via the built-in browser on Yinka's computer).
- Optional: **series** and **level** (defaults from the weekly rhythm below).
- Figures come only from moloneystreetre.com data or a named, linked source. Unknown figures stay as `[NUMBER: what is needed]`.

## Weekly rhythm (defaults)
| Day | Series | Level |
|---|---|---|
| Mon | The MoloneyStreetRe (one lesson) | Freshman |
| Tue | The MoloneyStreetRe | Freshman or Sophomore |
| Wed | The MoloneyStreetRe | Sophomore or Junior |
| Thu | Rumour Test (invented tip, tested on screen) | Junior |
| Fri | Friday on Moloney Street (week in 60s) | Senior |

## Voice
- Calm, sure, warm, a little humour. An elder who reads the numbers; never a salesman.
- Plain Nigerian English; a pidgin or Yoruba/Igbo/Hausa phrase only where it lands naturally.
- Short sentences, spoken rhythm. 110-150 spoken words for 45-60s. Read every line aloud.
- One idea per video. If it needs two, it's two videos.
- Openers to rotate: "Moloney Street, good morning." / "Sit down small, let's talk money."
- Sign-off every time: "Know the stock before you buy the story. See you on Moloney Street."

## Script template (five beats)
```
### [YYYY-MM-DD] · [Title]
Series: … | Level: … | Length: ~55s

HOOK (0-3s): one line that stops the scroll.
STORY (3-20s): a scene viewers recognise.
LESSON (20-45s): the one idea, in plain words, with its number and source.
TIE-IN (45-55s): the moloneystreetre.com page that goes deeper + call to action.
SIGN-OFF: "Know the stock before you buy the story. See you on Moloney Street."

ON SCREEN: caption text per beat (max 2 lines each) and any figure cards.
B-ROLL / VISUALS: list.
FIGURES & SOURCES: each figure with its source, or [NUMBER: …].
DISCLAIMER NEEDED: yes/no (yes whenever a real stock, fund or past performance appears).
CAPTIONS (.srt): timed captions for the spoken script.
POST CAPTIONS: Instagram/Facebook, TikTok, YouTube Shorts title + description.
```

## Compliance check (must pass)
MoloneyStreetRe is not authorised by the FCA (UK) or SEC Nigeria, so it is education only.
- No buy, sell or hold calls, no price targets, no return promises. Banned: "buy this", "sell now", "guaranteed", "risk-free", "double your money", "to the moon", "can't lose".
- Real stocks only as worked examples of a method, with on-screen "Research and education, not personal advice."
- Past performance → "Past performance is not a reliable guide to future results."
- Any benefit paired with its main risk in the same video.
- Rumour Test tips are invented; never quote or name a real person's post.
- Tax, pensions, land: "Rules change and depend on your situation; check with a qualified professional."
Mark the script PASS, CHANGES (list them) or BLOCK.

## Output
1. Save to `projects/content-and-marketing/scripts/YYYY-MM-DD-slug.md`.
2. Show Yinka the script and the compliance result. Nothing is posted from this skill.
3. After recording, the video can be edited with the house sound: `references/music/msre-fusion-30s.mp3` for shorts, `msre-fusion-171s.mp3` for longer videos.

## YouTube links from Yinka (inspiration queue)
Yinka drops links in `C:\Users\odbal\OneDrive\PA MoloneyStreetRe\video-ideas\1-inbox.txt`.
1. Before scripting, read `1-inbox.txt` and `2-treated.csv`. Skip any link already in the log.
2. For each new link: get the transcript and stats (vidIQ `vidiq_video_transcript`, `vidiq_video_stats`). Note the hook, the one idea and why it works.
3. Write our own script on the idea, in this skill's format, with Nigerian context (NGX names as examples, naira, CBN, local scenes). Never copy wording, footage or music; figures from our data only.
4. Remove the link from the inbox and append a row to `2-treated.csv`: date, link, original title, our script file, status (scripted / skipped), notes.
5. If the inbox is empty, take the next unused idea from `projects/content-and-marketing/video-ideas-bank.md` (from competitor research) and mark it used with the script file name. While Yinka's voice isn't recorded yet, prefer ideas marked **T** (text/card-led or captioned screen recording).

## Weekend long version (from the YouTube links)
Each linked idea can also become a longer video for the weekend.
- Length 5-8 minutes (about 700-1,100 spoken words). Chapters: Hook → The idea → Nigerian example(s) with our data → Common mistakes → What to check on moloneystreetre.com → Sign-off.
- Main home: YouTube (full video, with chapters and a thumbnail). Facebook gets the full video too. Cut one 60s teaser from it for IG, TikTok and Shorts.
- Music: `references/music/msre-fusion-171s.mp3`, looped under the voice at a low level.
- Timing: script on Thursday with the nightly drafts, Yinka approves by Friday, it posts Saturday around 11:00 London (12:00 Lagos).
- Save as `scripts/YYYY-MM-DD-long-slug.md` and log it in `2-treated.csv` (notes: "long version").

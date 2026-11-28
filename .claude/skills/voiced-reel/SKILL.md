---
name: voiced-reel
description: Make MoloneyStreetRe's daily voiced lesson reels (60-90s, vertical) with Yinka's cloned vidIQ voice, a picture per scene, captions and music, then send them for approval and schedule via Metricool. Use when Yinka says "voiced reels", "daily videos", "make this week's reels" or "turn this lesson into a reel".
---

# Voiced reel

A vertical lesson reel in the house long-video style, voiced with Yinka's cloned voice. Replaces the no-voice text reels of 24 Nov (batch 1). Example batch: `reels/2026-12-batch2-voiced/` in project files and OneDrive.

## Cadence and cost
- About 180 vidIQ credits per reel (6-7 pictures at 22, voiceover 28 per 1,000 characters). The Boost plan renews about 2,000 a month, so plan **3 reels a week** (default Mon, Tue, Wed at 22:15 London, after the nightly data post) unless Yinka asks for more. Check `vidiq_balance` before starting and say what the batch will cost.
- Make the week's reels in one batch (best Thursday to Saturday for the next week) so Yinka approves once.

## 1. Pick the topics
Next unused ideas from `projects/content-and-marketing/video-ideas-bank.md` (now that the voice exists, any format works), or Yinka's inbox (`OneDrive\PA MoloneyStreetRe\video-ideas\1-inbox.txt`, see the video-script skill). Mark each idea used with the reel's file name. One idea per reel.

## 2. Write the spec
Save `projects/content-and-marketing/reels/specs-voiced/YYYY-MM-DD-slug.json`:
```json
{"title": "…", "scenes": [{"head": "on-screen headline", "body": "one supporting line", "line": "what the voice says", "img": "picture prompt"}]}
```
- 6-7 scenes, about 180-200 spoken words in total (75-85 s). Keep the whole script under 1,200 characters.
- Write every `line` in Yinka's style: read `references/examples/yinka-script-style.md` first. Openers "Come sit down a minute for a quick money talk." or "Eh, have a seat and let's have our money talk, quickly." (never "Sit down small"); fuller sentences to "you"; light pidgin at a turn ("Patience now! We go get there."); spell out abbreviations in speech (Central Securities Clearing System, Bank Verification Number); amounts as words ("20,000 Naira").
- Last scene: head "Know the stock before you buy the story.", body "One plain-English money lesson every weekday at moloneystreetre.com", line ends "Know the stock before you buy the story. See you on Moloney Street."
- `img`: a Nigerian scene that fits the line, people or objects, no text. The builder adds the style suffix below.
- Public-content rules apply: no source, outlet or logo named for anything available on the NGX; illustrative numbers labelled; no buy/sell calls. No level badges (Freshman/Junior etc.) anywhere.

## 3. Voice and pictures (vidIQ)
- Voice: `vidiq_voiceover_generate` with voiceId `naGaNNEY3ODJuDIy4aEA` ("My Voice") and `scriptLines` = the scene lines in order. Save the joined `audioUrl` as `voice.mp3` and the `lines` list (startSeconds, durationSeconds) as `lines.json`. assets.vidiq.com is allowlisted for curl.
- Pictures: one `vidiq_image_generate` call per reel, aspectRatio `9:16`, one entry per scene, prompt = `img` + ". Photorealistic, rich forest green and warm gold colour grading, no text, no logos, no watermarks, vertical composition." Poll each job and save as `img_1.png` … `img_N.png` in the same folder. Look at every picture; regenerate one only if it shows text, a logo or something off-topic.

## 4. Build
`python3 tools/voiced_reel.py SPEC.json ASSET_DIR OUT.mp4 references/music/msre-fusion-171s.mp3`
Picture with slow zoom, dark-green fade, "The MoloneyStreetRe" wordmark, headline and body, progress bar, burned-in captions, site URL and disclaimer on every scene, music low under the voice. Also writes `OUT.srt` and `OUT_cover.png`. Check one frame per reel before sending.

## 5. Approval
1. Save the MP4s, covers and a captions file (IG/FB, TikTok, YouTube Shorts title, LinkedIn, compliance line) to project files `reels/YYYY-MM-batchN-voiced/` and to OneDrive `PA MoloneyStreetRe\reels\YYYY-MM-batchN-voiced\`.
2. Post them in one message, then an Approve / Change something card (`.claude/rules/approvals.md`). Never schedule without approval.

## 6. Schedule (after approval)
Metricool brand 8233421, timezone Europe/London. Upload each MP4 with `vidiq_video_upload` (localFile) and pass its videoUrl as media. Providers: Instagram Reel, Facebook Reel, TikTok, YouTube Short on @moloneystreetre, and LinkedIn (MoloneyStreetRe Analytics profile only, `linkedinData` `{"type":"post","previewIncluded":true}`). Then tell Yinka it's scheduled, with the times.

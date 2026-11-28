#!/usr/bin/env python3
"""Build a voiced vertical reel (1080x1920) in the house long-video style.

Usage: voiced_reel.py SPEC.json ASSET_DIR OUT.mp4 [MUSIC.mp3]

SPEC.json: {"title": "...", "scenes": [{"head": "...", "body": "...", "line": "spoken text", "img": "picture prompt"}, ...]}
ASSET_DIR must hold:
  img_1.png ... img_N.png   one picture per scene (vidiq_image_generate, 9:16)
  voice.mp3                 the whole narration (vidiq_voiceover_generate with scriptLines, voice "My Voice")
  lines.json                the `lines` list from that result (startSeconds, durationSeconds per scene)

Each scene: picture with a slow zoom, dark-green fade, "The MoloneyStreetRe" wordmark (no level badge),
headline and body text, burned-in captions of the spoken line, site URL and disclaimer.
Music sits low under the voice. Also writes OUT.srt and OUT_cover.png (scene 1 still).
"""
import json, os, subprocess, sys, tempfile
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1920
FOREST_DARK, GOLD, CREAM = (14, 36, 10), (212, 168, 90), (251, 248, 238)
F = "/usr/share/fonts/opentype/inter/Inter-%s.otf"
BRAND = "The MoloneyStreetRe"
TAIL = 0.8  # seconds held after the last word


def font(sz, w="Bold"):
    return ImageFont.truetype(F % w, sz)


def wrap(d, text, fnt, width):
    out = []
    for para in text.split("\n"):
        line = ""
        for w in para.split():
            t = (line + " " + w).strip()
            if d.textlength(t, font=fnt) <= width:
                line = t
            else:
                out.append(line); line = w
        out.append(line)
    return out


def overlay(scene, i, n, path):
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    # top fade for the wordmark
    for y in range(0, 260):
        a = int(235 * (1 - y / 260)); d.line([(0, y), (W, y)], fill=FOREST_DARK + (a,))
    # bottom fade for text, captions and footer
    top = 820
    for y in range(top, H):
        t = min(1, (y - top) / 380); d.line([(0, y), (W, y)], fill=FOREST_DARK + (int(235 * t),))
    d.text((60, 90), BRAND, font=font(46, "ExtraBold"), fill=GOLD)
    d.rectangle([60, 152, 60 + 120, 158], fill=GOLD)
    hf, bf = font(74, "ExtraBold"), font(44, "Medium")
    hl = wrap(d, scene["head"], hf, W - 140)
    bl = wrap(d, scene.get("body", ""), bf, W - 170) if scene.get("body") else []
    y = 1060
    for ln in hl:
        d.text((70, y), ln, font=hf, fill=CREAM); y += 88
    if bl:
        y += 22; d.rectangle([70, y + 4, 76, y + len(bl) * 58 - 10], fill=GOLD)
        for ln in bl:
            d.text((100, y), ln, font=bf, fill=GOLD); y += 58
    # progress bar
    seg = (W - 140) / n
    for k in range(n):
        d.rounded_rectangle([70 + k * seg + 4, 1700, 70 + (k + 1) * seg - 4, 1708], radius=4,
                            fill=GOLD if k <= i else (90, 110, 80, 255))
    d.text((W // 2, 1768), "moloneystreetre.com", font=font(48), fill=CREAM, anchor="mm")
    d.text((W // 2, 1840), "Research and education, not personal advice.", font=font(30, "Medium"),
           fill=CREAM, anchor="mm")
    im.save(path)


def ts(s):
    h, s = divmod(s, 3600); m, s = divmod(s, 60)
    return f"{int(h):02d}:{int(m):02d}:{int(s):02d},{int(round((s % 1) * 1000)) % 1000:03d}"


def captions(scenes, lines, srt_path):
    out, k = [], 1
    for sc, ln in zip(scenes, lines):
        words = sc["line"].split(); chunks, cur = [], []
        for w in words:
            cur.append(w)
            if len(cur) >= 5 or w[-1] in ".?!,:":
                if len(cur) >= 3 or w[-1] in ".?!": chunks.append(" ".join(cur)); cur = []
        if cur: chunks.append(" ".join(cur))
        total_chars = sum(len(c) for c in chunks); t = ln["startSeconds"] + 0.05
        span = ln["durationSeconds"] - 0.15
        for c in chunks:
            dt = span * len(c) / total_chars
            out.append(f"{k}\n{ts(t)} --> {ts(t + dt)}\n{c}\n"); k += 1; t += dt
    open(srt_path, "w").write("\n".join(out))


def main():
    spec_p, adir, out = sys.argv[1:4]; music = sys.argv[4] if len(sys.argv) > 4 else None
    spec = json.load(open(spec_p)); scenes = spec["scenes"]; n = len(scenes)
    lines = json.load(open(os.path.join(adir, "lines.json")))
    assert len(lines) == n, "one voice line per scene"
    voice = os.path.join(adir, "voice.mp3")
    vdur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                          "-of", "csv=p=0", voice]).decode().strip())
    total = vdur + TAIL
    tmp = tempfile.mkdtemp(); base = os.path.splitext(out)[0]
    starts = [l["startSeconds"] for l in lines] + [total]
    segs = []
    for i, sc in enumerate(scenes):
        dur = starts[i + 1] - starts[i]
        ov = os.path.join(tmp, f"ov{i}.png"); overlay(sc, i, n, ov)
        img = os.path.join(adir, f"img_{i + 1}.png"); seg = os.path.join(tmp, f"seg{i}.mp4")
        z = 0.07 / dur
        vf = (f"[0:v]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},"
              f"scale=w='trunc({W}*(1+{z}*t)/2)*2':h=-2:eval=frame,crop={W}:{H},setsar=1[bg];"
              f"[bg][1:v]overlay=0:0,format=yuv420p,fps=30[v]")
        subprocess.run(["ffmpeg", "-y", "-loop", "1", "-framerate", "30", "-t", f"{dur:.3f}", "-i", img,
                        "-i", ov, "-filter_complex", vf, "-map", "[v]", "-t", f"{dur:.3f}",
                        "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", seg],
                       check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        segs.append(seg)
        if i == 0:
            Image.alpha_composite(Image.open(img).convert("RGBA").resize((W, H)), Image.open(ov)).convert("RGB").save(base + "_cover.png")
    lst = os.path.join(tmp, "list.txt"); open(lst, "w").write("".join(f"file '{s}'\n" for s in segs))
    srt = base + ".srt"; captions(scenes, lines, srt)
    style = ("FontName=Inter,Fontsize=10,Bold=1,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,"
             "BorderStyle=1,Outline=2,Shadow=0,Alignment=2,MarginV=62")
    cmd = ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-i", voice]
    if music: cmd += ["-stream_loop", "-1", "-i", music]
    vf = f"[0:v]subtitles={srt}:fontsdir=/usr/share/fonts/opentype/inter:force_style='{style}'[v]"
    if music:
        af = (f"[1:a]apad,atrim=0:{total:.2f}[vo];[2:a]volume=0.10,atrim=0:{total:.2f},"
              f"afade=t=out:st={total - 1.5:.2f}:d=1.5[mu];[vo][mu]amix=inputs=2:duration=first:normalize=0[a]")
    else:
        af = f"[1:a]apad,atrim=0:{total:.2f}[a]"
    cmd += ["-filter_complex", vf + ";" + af, "-map", "[v]", "-map", "[a]", "-t", f"{total:.2f}",
            "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-c:a", "aac", "-b:a", "192k",
            "-movflags", "+faststart", out]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(out, f"{total:.1f}s")


if __name__ == "__main__":
    main()

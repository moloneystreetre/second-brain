#!/usr/bin/env python3
"""Build a no-voice, text-led lesson reel (1080x1920) in house style from a JSON spec.

Usage: lesson_reel.py SPEC.json OUT.mp4 [MUSIC.mp3]

Spec: {"series": "The MoloneyStreetRe · FRESHMAN",
       "slides": [{"head": "Big line", "body": "Smaller supporting text", "secs": 4}, ...]}
The last slide should be the sign-off/CTA. Every slide carries the disclaimer line.
Also writes OUT_slideN.png stills (handy as a carousel).
"""
import json, os, subprocess, sys, tempfile, textwrap
from PIL import Image, ImageDraw, ImageFont

FOREST, FOREST_DARK, GOLD, CREAM, INK = (30,63,17), (18,42,12), (212,168,90), (251,248,238), (40,40,40)
W, H = 1080, 1920
F = "/usr/share/fonts/opentype/inter/Inter-%s.otf"
def font(sz, w="Bold"): return ImageFont.truetype(F % w, sz)

def wrap(d, text, fnt, width):
    out = []
    for para in text.split("\n"):
        words, line = para.split(), ""
        for w in words:
            t = (line + " " + w).strip()
            if d.textlength(t, font=fnt) <= width: line = t
            else: out.append(line); line = w
        out.append(line)
    return out

def slide(spec, s, i, n, out):
    im = Image.new("RGB", (W, H)); d = ImageDraw.Draw(im)
    for y in range(H):
        t = y / H; d.line([(0,y),(W,y)], fill=tuple(int(FOREST[k]*(1-t)+FOREST_DARK[k]*t) for k in range(3)))
    d.text((W//2, 150), spec["series"], font=font(36), fill=GOLD, anchor="mm")
    # cream panel
    px, py0, py1 = 60, 300, 1500
    d.rounded_rectangle([px, py0, W-px, py1], radius=36, fill=CREAM)
    hf, bf = font(76, "ExtraBold"), font(48, "Medium")
    hl = wrap(d, s["head"], hf, W-2*px-120); bl = wrap(d, s.get("body",""), bf, W-2*px-120) if s.get("body") else []
    th = len(hl)*92 + (40 if bl else 0) + len(bl)*66
    y = py0 + (py1-py0-th)//2
    for ln in hl: d.text((px+60, y), ln, font=hf, fill=FOREST); y += 92
    if bl:
        y += 40; d.rectangle([px+60, y, px+66, y+len(bl)*66-14], fill=GOLD)
        for ln in bl: d.text((px+90, y), ln, font=bf, fill=INK); y += 66
    if s.get("note"): d.text((W//2, py1-50), s["note"], font=font(30, "Medium"), fill=(120,120,120), anchor="mm")
    # progress dots
    for k in range(n):
        x = W//2 + (k-(n-1)/2)*36; d.ellipse([x-9, 1580-9, x+9, 1580+9], fill=GOLD if k == i else (90,110,80))
    d.text((W//2, 1690), "moloneystreetre.com", font=font(52), fill=CREAM, anchor="mm")
    d.text((W//2, 1770), "Research and education, not personal advice.", font=font(32, "Medium"), fill=CREAM, anchor="mm")
    im.save(out)

def main():
    spec_p, out = sys.argv[1], sys.argv[2]; music = sys.argv[3] if len(sys.argv) > 3 else None
    spec = json.load(open(spec_p)); slides = spec["slides"]; n = len(slides)
    tmp = tempfile.mkdtemp(); base = os.path.splitext(out)[0]
    pngs = []
    for i, s in enumerate(slides):
        p = f"{base}_slide{i+1}.png"; slide(spec, s, i, n, p); pngs.append(p)
    fade = 0.4; durs = [s.get("secs", 4) for s in slides]; total = sum(durs) - fade*(n-1)
    cmd = ["ffmpeg", "-y"]
    for p, dsec in zip(pngs, durs): cmd += ["-loop", "1", "-t", str(dsec), "-i", p]
    if music: cmd += ["-i", music]
    fc, last, off = [], "0:v", 0
    for i in range(1, n):
        off += durs[i-1] - fade
        lab = f"v{i}"; fc.append(f"[{last}][{i}:v]xfade=transition=fade:duration={fade}:offset={off:.2f}[{lab}]"); last = lab
    fc.append(f"[{last}]format=yuv420p,fps=30[vout]")
    cmd += ["-filter_complex", ";".join(fc), "-map", "[vout]"]
    if music:
        cmd += ["-map", f"{n}:a", "-af", f"volume=0.8,afade=t=in:d=0.5,afade=t=out:st={total-1.5:.2f}:d=1.5", "-c:a", "aac", "-b:a", "192k"]
    cmd += ["-t", f"{total:.2f}", "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-movflags", "+faststart", out]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(out, f"{total:.1f}s")

if __name__ == "__main__": main()

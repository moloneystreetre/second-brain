#!/usr/bin/env python3
"""Turn a Street Note card image into a 15s 9:16 reel with optional music.
Usage: card_to_reel.py CARD.png OUT.mp4 [MUSIC.mp3] [--secs 15]
"""
import subprocess, sys, os, tempfile
from PIL import Image, ImageDraw, ImageFont

FOREST, FOREST_DARK, GOLD, CREAM = (30,63,17), (18,42,12), (212,168,90), (251,248,238)
W, H = 1080, 1920
FONT = "/usr/share/fonts/opentype/inter/Inter-Bold.otf"

def font(sz):
    try: return ImageFont.truetype(FONT, sz)
    except Exception: return ImageFont.load_default()

def background(card_path, out_png):
    bg = Image.new("RGB", (W, H))
    d = ImageDraw.Draw(bg)
    for y in range(H):  # forest -> forest-dark gradient
        t = y / H
        d.line([(0,y),(W,y)], fill=tuple(int(FOREST[i]*(1-t)+FOREST_DARK[i]*t) for i in range(3)))
    card = Image.open(card_path).convert("RGB")
    cw = W - 80
    card = card.resize((cw, int(cw*card.height/card.width)), Image.LANCZOS)
    top = (H - card.height)//2
    bg.paste(card, (40, top))
    d.text((W//2, top-110), "THE MOLONEYSTREETRE", font=font(56), fill=GOLD, anchor="mm")
    d.text((W//2, top+card.height+90), "moloneystreetre.com", font=font(52), fill=CREAM, anchor="mm")
    d.text((W//2, top+card.height+170), "Research and education, not personal advice.", font=font(34), fill=CREAM, anchor="mm")
    bg.save(out_png)

def main():
    a = [x for x in sys.argv[1:] if not x.startswith("--")]
    secs = 15
    if "--secs" in sys.argv: secs = int(sys.argv[sys.argv.index("--secs")+1]); a.remove(str(secs))
    card, out = a[0], a[1]; music = a[2] if len(a) > 2 else None
    tmp = os.path.join(tempfile.mkdtemp(), "bg.png"); background(card, tmp)
    fps = 30; n = secs*fps
    vf = (f"scale=2160:-1,zoompan=z='min(1+0.0006*on,1.08)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
          f":d={n}:s={W}x{H}:fps={fps},fade=t=in:st=0:d=0.5,format=yuv420p")
    cmd = ["ffmpeg","-y","-loop","1","-i",tmp]
    if music: cmd += ["-i", music]
    cmd += ["-vf", vf, "-t", str(secs), "-c:v","libx264","-preset","medium","-crf","20","-r",str(fps)]
    if music: cmd += ["-af", f"afade=t=in:d=0.5,afade=t=out:st={secs-1.5}:d=1.5", "-c:a","aac","-b:a","192k","-shortest"]
    else: cmd += ["-an"]
    cmd += ["-movflags","+faststart", out]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(out)

if __name__ == "__main__": main()

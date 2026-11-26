#!/usr/bin/env python3
"""Render a Daily Street Note card (1080 wide) in house style. Usage: make_card.py OUT.png"""
import sys, os, textwrap
from PIL import Image, ImageDraw, ImageFont
F="/usr/share/fonts/opentype/inter/Inter-%s.otf"
def f(s,w="Bold"): return ImageFont.truetype(F%w,s)
LOGOS=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","references","logos")
def source_logos(im,names,x_right,y,h=34):
    """Paste tiny source logos (references/logos/<name>.png), right-aligned. Never writes source names as text.
    Returns the names whose logo file is missing, so the run can flag them."""
    missing=[]; x=x_right
    for n in reversed(names or []):
        fp=os.path.join(LOGOS,n.lower()+".png")
        if not os.path.exists(fp): missing.append(n); continue
        lg=Image.open(fp).convert("RGBA"); lg=lg.resize((max(1,int(lg.width*h/lg.height)),h))
        x-=lg.width; im.paste(lg,(x,y),lg); x-=14
    return missing
def card(out,label,title,date,body,chips,link,tags,sources=None):
    W,H=1080,1080; im=Image.new("RGB",(W,H),(251,248,238)); d=ImageDraw.Draw(im)
    for y in range(300):
        t=y/300; d.line([(0,y),(W,y)],fill=tuple(int(a*(1-t)+b*t) for a,b in zip((30,63,17),(18,42,12))))
    d.text((60,60),label,font=f(28,"Bold"),fill=(212,168,90))
    d.text((60,110),title,font=f(54,"ExtraBold"),fill=(255,255,255))
    d.text((60,200),date,font=f(30,"Medium"),fill=(220,225,210))
    d.rectangle([60,340,66,340+len(textwrap.wrap(body,52))*44],fill=(212,168,90))
    y=340
    for ln in textwrap.wrap(body,52): d.text((86,y),ln,font=f(32,"Regular"),fill=(40,40,40)); y+=44
    y+=40; x=60
    for txt,col in chips:
        w=d.textlength(txt,font=f(30,"Bold"))+48; d.rounded_rectangle([x,y,x+w,y+60],radius=30,fill=col); d.text((x+w/2,y+30),txt,font=f(30,"Bold"),fill=(255,255,255),anchor="mm"); x+=w+20
    y+=110; d.text((60,y),link,font=f(30,"Bold"),fill=(30,63,17)); d.text((60,y+50),tags,font=f(26,"Medium"),fill=(110,110,110))
    d.rounded_rectangle([60,H-170,W-60,H-90],radius=14,fill=(30,63,17)); d.text((W/2,H-130),"Subscribe for the full brief → moloneystreetre.com",font=f(32,"Bold"),fill=(255,255,255),anchor="mm")
    d.text((W/2,H-45),"Research and education, not personal advice.",font=f(24,"Medium"),fill=(110,110,110),anchor="mm")
    miss=source_logos(im,sources,W-60,y+44)
    if miss: print("MISSING LOGO:",", ".join(miss),"- add references/logos/<name>.png")
    im.save(out)
if __name__=="__main__":
    card(sys.argv[1],"DAILY STREET NOTE","The Daily Street Note","Monday, 23 Nov 2026",
    "The NGX shed about ₦767bn today as banks led a retreat (Nairametrics). But not everything fell: AIICO (+9.9%), Africa Prudential (+8.8%) and FCMB (+7.3%) rose, and FCMB moved up into our Strong band while CWG dropped out.",
    [("8 Strong",(46,90,160)),("▲ 3 rising",(46,125,50)),("▼ 3 falling",(190,60,50))],
    "moloneystreetre.com/today.html","#NGX #NigerianStocks #MSReAnalytics #Investing")

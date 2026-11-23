#!/usr/bin/env python3
"""WhatsApp cards in house style. Usage: make_whatsapp_cards.py SPEC.json OUTDIR
SPEC keys: date, status_hook, status_sub, movers [[name,chg,up]], chips [[txt,colour]], channel_title, channel_points [..], tip"""
import json, sys, textwrap, os
from PIL import Image, ImageDraw, ImageFont
F="/usr/share/fonts/opentype/inter/Inter-%s.otf"
def f(s,w="Bold"): return ImageFont.truetype(F%w,s)
FOREST,DARK,GOLD,CREAM,RED,GREEN=(30,63,17),(14,34,10),(212,168,90),(251,248,238),(214,72,60),(110,190,90)
COL={"blue":(46,90,160),"green":(46,125,50),"red":(190,60,50)}
def grad(W,H):
    im=Image.new("RGB",(W,H)); d=ImageDraw.Draw(im)
    for y in range(H):
        t=y/H; d.line([(0,y),(W,y)],fill=tuple(int(FOREST[i]*(1-t)+DARK[i]*t) for i in range(3)))
    return im,d
def chips(d,W,y,cs,sz=34):
    ws=[d.textlength(t,font=f(sz))+50 for t,_ in cs]; x=(W-sum(ws)-20*(len(ws)-1))/2
    for (t,c),w in zip(cs,ws):
        d.rounded_rectangle([x,y,x+w,y+66],radius=33,fill=COL[c]); d.text((x+w/2,y+33),t,font=f(sz),fill="white",anchor="mm"); x+=w+20
def status(s,out):
    W,H=1080,1920; im,d=grad(W,H)
    d.text((W/2,170),"DAILY STREET NOTE",font=f(44,"ExtraBold"),fill=GOLD,anchor="mm"); d.text((W/2,235),s["date"],font=f(36,"Medium"),fill=CREAM,anchor="mm")
    y=420
    for ln in textwrap.wrap(s["status_hook"],16): d.text((W/2,y),ln,font=f(96,"Black"),fill="white",anchor="mm"); y+=115
    y+=30
    for ln in textwrap.wrap(s["status_sub"],30): d.text((W/2,y),ln,font=f(48,"Bold"),fill=GOLD,anchor="mm"); y+=64
    y+=60
    for n,c,up in s["movers"]:
        d.rounded_rectangle([140,y,W-140,y+110],radius=24,fill=(255,255,255,0) if False else (24,52,14))
        d.text((190,y+55),("▲ " if up else "▼ ")+n,font=f(52,"ExtraBold"),fill=GREEN if up else RED,anchor="lm"); d.text((W-190,y+55),c,font=f(52,"ExtraBold"),fill="white",anchor="rm"); y+=135
    chips(d,W,y+30,s["chips"])
    d.text((W/2,H-230),"moloneystreetre.com",font=f(58,"ExtraBold"),fill="white",anchor="mm")
    d.text((W/2,H-150),"Research and education, not personal advice.",font=f(30,"Medium"),fill=CREAM,anchor="mm")
    im.save(out)
def channel(s,out):
    W,H=1080,1350; im=Image.new("RGB",(W,H),CREAM); d=ImageDraw.Draw(im)
    g,_=grad(W,260); im.paste(g,(0,0)); d=ImageDraw.Draw(im)
    d.text((60,70),"DAILY STREET NOTE",font=f(30),fill=GOLD); d.text((60,120),s["channel_title"],font=f(52,"ExtraBold"),fill="white"); d.text((60,190),s["date"],font=f(30,"Medium"),fill=(220,225,210))
    y=320
    for p in s["channel_points"]:
        d.ellipse([60,y+12,80,y+32],fill=GOLD); 
        for ln in textwrap.wrap(p,44): d.text((105,y),ln,font=f(38,"Medium"),fill=(35,35,35)); y+=52
        y+=26
    chips(d,W,y+10,s["chips"]); y+=120
    d.rounded_rectangle([60,y,W-60,y+215],radius=20,fill=(240,232,205)); d.text((90,y+25),"💡 BEGINNER TIP".replace("💡 ",""),font=f(30,"ExtraBold"),fill=(140,100,30)); yy=y+75
    for ln in textwrap.wrap(s["tip"],52): d.text((90,yy),ln,font=f(32,"Medium"),fill=(50,50,50)); yy+=42
    d.rounded_rectangle([60,H-180,W-60,H-100],radius=14,fill=FOREST); d.text((W/2,H-140),"Full note → moloneystreetre.com",font=f(36),fill="white",anchor="mm")
    d.text((W/2,H-50),"Research and education, not personal advice. Past performance is not a reliable guide.",font=f(22,"Medium"),fill=(110,110,110),anchor="mm")
    im.save(out)
if __name__=="__main__":
    s=json.load(open(sys.argv[1])); o=sys.argv[2]; os.makedirs(o,exist_ok=True); p=s["file_prefix"]
    status(s,f"{o}/{p}_status-card.png"); channel(s,f"{o}/{p}_channel-card.png"); print("ok")

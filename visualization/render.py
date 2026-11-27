#!/usr/bin/env python3
"""Rotate a bar chart of the exact four-edge tropical path trace."""
from math import cos, sin, tau
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

N = 4
WEIGHTS = [3**(N-j) for j in range(N+1)]
COSTS = [sum(WEIGHTS[:j])+2*WEIGHTS[j] for j in range(N+1)]
BG, CARD, GRID = "#0b1523", "#132338", "#38516a"
INK, TEXT, GOLD, AQUA = "#eff8fe", "#bfd3e5", "#ffce79", "#76dfc7"


def font(size,bold=False):
    for root,regular,heavy in [
        ("/System/Library/Fonts/Supplemental","Arial.ttf","Arial Bold.ttf"),
        ("/usr/share/fonts/truetype/dejavu","DejaVuSans.ttf","DejaVuSans-Bold.ttf")]:
        path = Path(root) / (heavy if bold else regular)
        if path.is_file():
            return ImageFont.truetype(str(path),size)
    raise RuntimeError("Arial or DejaVu Sans is required")


TITLE, BODY, LABEL, BIG = font(31,True),font(20),font(20,True),font(35,True)


def draw_bars(draw, theta, active):
    def project(x,y,z):
        return 214+63*(x*cos(theta)+z*sin(theta)), 269-105*y+15*(-x*sin(theta)+z*cos(theta))
    for j in range(N+1):
        height = COSTS[j]/COSTS[0]
        x=j-2
        vertices=[(x-.32,-.31),(x+.32,-.31),(x+.32,.31),(x-.32,.31)]
        base=[project(vx,0,vz) for vx,vz in vertices]
        top=[project(vx,height,vz) for vx,vz in vertices]
        front,side,cap = ("#e09d58",GOLD,"#ffe4ab") if j==active else ("#418999","#65c7c2",AQUA)
        draw.polygon([base[3],base[2],top[2],top[3]],fill=front,outline=BG)
        draw.polygon([base[0],base[3],top[3],top[0]],fill=side,outline=BG)
        draw.polygon(top,fill=cap,outline=BG)
        tx,_ = project(x,0,0)
        draw.text((tx,304),str(j+2),font=LABEL,fill=GOLD if j==active else TEXT,anchor="mt")


def frame(i,n):
    active = i * (N+1) // n
    im=Image.new("RGB",(661,436),BG)
    draw=ImageDraw.Draw(im)
    draw.text((26,16),"Longer tropical proofs cost less",font=TITLE,fill=INK)
    draw.text((27,55),"Four-edge path with guard weights 81, 27, 9, 3, 1",font=BODY,fill=TEXT)
    for card in [(22,92,407,340),(420,92,639,340)]:
        draw.rounded_rectangle(card,14,fill=CARD,outline=GRID)
    draw.text((214,108),"Tropical cost at T(0)",font=LABEL,fill=INK,anchor="mt")
    draw_bars(draw,.18+.51*(1+sin(tau*i/n))/2,active)
    draw.text((214,328),"Round",font=BODY,fill=TEXT,anchor="mt")
    draw.text((530,114),f"Round {active+2}",font=LABEL,fill=GOLD,anchor="mt")
    draw.text((530,155),str(COSTS[active]),font=BIG,fill=INK,anchor="mt")
    draw.text((530,219),f"Stop at vertex {active}",font=BODY,fill=TEXT,anchor="mt")
    category="Final tropical cost" if active==N else "Tropical can improve"
    draw.text((530,275),category,font=LABEL,fill=AQUA,anchor="mt")
    draw.text((330,365),"Boolean: fixed at round 2  ·  Tropical: fixed at round 6",font=LABEL,fill=INK,anchor="mt")
    draw.text((330,404),"The general construction needs n + 2 rounds for n edges.",font=BODY,fill=TEXT,anchor="mt")
    return im


def main():
    frames=[frame(i,40) for i in range(40)]
    sample=Image.new("RGB",(661*2,436))
    sample.paste(frames[0],(0,0))
    sample.paste(frames[39],(661,0))
    palette=sample.quantize(colors=48)
    indexed=[im.quantize(palette=palette,dither=Image.Dither.NONE) for im in frames]
    target=Path(__file__).with_name("tropical-rounds.gif")
    indexed[0].save(target,save_all=True,append_images=indexed[1:],duration=135,loop=0,optimize=True)
    print(f"{target.name}: {len(frames)} source frames, {target.stat().st_size} bytes")


if __name__=="__main__":
    main()

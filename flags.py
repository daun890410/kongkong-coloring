# 국기 10개를 정확한 모양으로 직접 그린다 → img/x01.png (칠할 선 그림) · img/flagref/x01.png (정답 색 작은 그림)
import math
from pathlib import Path
from PIL import Image, ImageDraw
S=1024; FW,FH=900,600; OX,OY=(S-FW)//2,(S-FH)//2
def circ(cx,cy,r,a0=0,a1=360,n=120):
    return [(cx+r*math.cos(math.radians(a0+(a1-a0)*k/n)),cy+r*math.sin(math.radians(a0+(a1-a0)*k/n))) for k in range(n+1)]
def rect(x0,y0,x1,y1): return [(x0,y0),(x1,y0),(x1,y1),(x0,y1)]
def rot(pts,ang,cx,cy):
    c,s=math.cos(ang),math.sin(ang); return [(cx+(x-cx)*c-(y-cy)*s, cy+(x-cx)*s+(y-cy)*c) for x,y in pts]
def star(cx,cy,r):
    return [(cx+(r if k%2==0 else r*.4)*math.cos(-math.pi/2+k*math.pi/5),cy+(r if k%2==0 else r*.4)*math.sin(-math.pi/2+k*math.pi/5)) for k in range(10)]
R_,W_,B_,K_,Y_,G_='#cd2e3a','#ffffff','#0047a0','#111111','#ffce00','#009246'
def F(x,y): return (OX+x,OY+y)          # 깃발 안 좌표
def shp(pts): return [F(x,y) for x,y in pts]
def stripes(cols,vertical):
    n=len(cols); out=[]
    for i,c in enumerate(cols):
        out.append((shp(rect(FW*i/n,0,FW*(i+1)/n,FH) if vertical else rect(0,FH*i/n,FW,FH*(i+1)/n)),c))
    return out
def korea():
    o=[(shp(rect(0,0,FW,FH)),W_)]; cx,cy=FW/2,FH/2; Rr=FH/4; ang=math.atan2(2,3)
    blue=circ(cx,cy,Rr)
    red=circ(cx,cy,Rr,180,360)+circ(cx+Rr/2,cy,Rr/2,360,180)+circ(cx-Rr/2,cy,Rr/2,0,180)
    o+= [(shp(rot(blue,ang,cx,cy)),B_),(shp(rot(red,ang,cx,cy)),R_)]
    bw,bh,gap=FH/4*0.95/1, FH/24, FH/48
    def tri(pattern,d,a):   # pattern: 위에서부터 막대 3개 (True=통막대)
        x0=cx+d*math.cos(a); y0=cy+d*math.sin(a); res=[]
        for k,solid in enumerate(pattern):
            yy=-(1.5*bh+gap)+k*(bh+gap)
            parts=[(-bw/2,bw/2)] if solid else [(-bw/2,-bw/24),(bw/24,bw/2)]
            for a0,a1 in parts: res.append(rot([(x0+a0,y0+yy),(x0+a1,y0+yy),(x0+a1,y0+yy+bh),(x0+a0,y0+yy+bh)],a+math.pi/2,x0,y0))
        return res
    d=FH/4+FH/8+FH/12
    for pat,a in (([1,1,1],math.pi+ang),([0,0,0],ang),([0,1,0],-ang),([1,0,1],math.pi-ang)):
        for pts in tri(pat,d,a): o.append((shp(pts),K_))
    return o
def japan(): return [(shp(rect(0,0,FW,FH)),W_),(shp(circ(FW/2,FH/2,FH*.3)),'#bc002d')]
def usa():
    o=[]; n=13
    for i in range(n): o.append((shp(rect(0,FH*i/n,FW,FH*(i+1)/n)),'#b22234' if i%2==0 else W_))
    cw,ch=FW*.4,FH*7/13; o.append((shp(rect(0,0,cw,ch)),'#3c3b6e'))
    for r in range(9):
        cols=6 if r%2==0 else 5
        for c in range(cols):
            x=cw/12*(2*c+1+(0 if r%2==0 else 1)); y=ch/10*(r+1); o.append((shp(star(x,y,ch/22)),W_))
    return o
def uk():
    o=[(shp(rect(0,0,FW,FH)),'#012169')]; t=FH/5
    def diag(w,c):
        L=math.hypot(FW,FH); a=math.atan2(FH,FW)
        for aa in (a,-a): o.append((shp(rot(rect(FW/2-L/2,FH/2-w/2,FW/2+L/2,FH/2+w/2),aa,FW/2,FH/2)),c))
    diag(FH/5,W_); diag(FH/15,'#c8102e')
    o.append((shp(rect(FW/2-t/1.2,0,FW/2+t/1.2,FH)),W_)); o.append((shp(rect(0,FH/2-t/1.2,FW,FH/2+t/1.2)),W_))
    o.append((shp(rect(FW/2-t/2,0,FW/2+t/2,FH)),'#c8102e')); o.append((shp(rect(0,FH/2-t/2,FW,FH/2+t/2)),'#c8102e'))
    return o
def swiss():
    s=FH; x0=(FW-s)/2; o=[(shp(rect(x0,0,x0+s,s)),'#da291c')]; a=s*6/32; b=s*20/32; c=s/2
    o.append((shp(rect(x0+c-a/2,c-b/2,x0+c+a/2,c+b/2)),W_)); o.append((shp(rect(x0+c-b/2,c-a/2,x0+c+b/2,c+a/2)),W_)); return o
def sweden():
    o=[(shp(rect(0,0,FW,FH)),'#006aa7')]; u=FW/16
    o.append((shp(rect(5*u,0,7*u,FH)),'#fecc00')); o.append((shp(rect(0,FH*4/10,FW,FH*6/10)),'#fecc00')); return o
def greece():
    o=[]; n=9
    for i in range(n): o.append((shp(rect(0,FH*i/n,FW,FH*(i+1)/n)),'#0d5eaf' if i%2==0 else W_))
    s=FH*5/9; o.append((shp(rect(0,0,s,s)),'#0d5eaf')); w=FH/9
    o.append((shp(rect(s/2-w/2,0,s/2+w/2,s)),W_)); o.append((shp(rect(0,s/2-w/2,s,s/2+w/2)),W_)); return o
FLAGS={'x01':korea,'x02':japan,'x03':usa,'x04':uk,'x05':lambda:stripes(['#0055a4',W_,'#ef4135'],True),'x06':lambda:stripes([G_,W_,'#ce2b37'],True),
 'x07':lambda:stripes([K_,'#dd0000',Y_],False),'x08':swiss,'x09':sweden,'x10':greece}
Path('img/flagref').mkdir(parents=True,exist_ok=True)
for k,fn in FLAGS.items():
    shapes=fn()
    col=Image.new('RGB',(S,S),'white'); dc=ImageDraw.Draw(col)
    for pts,c in shapes: dc.polygon(pts,fill=c)
    line=Image.new('L',(S,S),255); dl=ImageDraw.Draw(line)
    for pts,c in shapes: dl.polygon(pts,fill=255)
    for pts,c in shapes: dl.line(pts+[pts[0]],fill=0,width=9,joint='curve')
    bx=(OX-6,OY-6,OX+FW+6,OY+FH+6) if k!='x08' else (OX+(FW-FH)//2-6,OY-6,OX+(FW+FH)//2+6,OY+FH+6)
    m=Image.new('L',(S,S),0);ImageDraw.Draw(m).rectangle((bx[0]+6,bx[1]+6,bx[2]-6,bx[3]-6),fill=255)
    line=Image.composite(line,Image.new('L',(S,S),255),m);col=Image.composite(col,Image.new('RGB',(S,S),'white'),m);dl=ImageDraw.Draw(line)
    dl.rectangle(bx,outline=0,width=12)
    line.save(f'img/{k}.png',optimize=True)
    col.crop((bx[0],bx[1],bx[2],bx[3])).resize((240,int(240*(bx[3]-bx[1])/(bx[2]-bx[0]))),Image.LANCZOS).save(f'img/flagref/{k}.png',optimize=True)
print('국기',len(FLAGS))

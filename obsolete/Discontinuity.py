# CrystallisR 2022
import math
import random
from PIL import Image, ImageDraw

# return coordinates of the 4 vertices of a rhombus and 2 vertices of its cutting line
# rhombus has 4 vertices which are a, b, c, d in anti-clockwise order
def rhombusPos2(size, margin=0.3, maxl=0.4, minl=0.3, factor=1.2):
    wsz, hsz = size
    ssz = min(wsz, hsz)
    l1, l2 = random.randint(ssz*minl, ssz*maxl), random.randint(ssz*minl, ssz*maxl)
    # center point of a rhombus
    ox, oy = random.randint(wsz*margin, wsz-wsz*margin), random.randint(hsz*margin, hsz-hsz*margin)
    theta = 0
    # cutting line
    l3 = ssz*maxl*factor
    ax, ay = ox - l3*math.cos(theta), oy - l3*math.sin(theta)*factor
    bx, by = ox + l3*math.cos(theta), oy + l3*math.sin(theta)*factor
    coords = [(l1/2.0, l1/2.0), (l2/2.0, l2/2.0), (l1/2.0, l1/2.0), (l2/2.0, l2/2.0)]
    return [(-coords[i][0]*math.cos(theta+i*math.pi/2) + ox, 
            -coords[i][1]*math.sin(theta+i*math.pi/2) + oy) for i in range(4)], [(ax, ay), (bx, by)]
    
def drawDis(path, size, colors=[(255, 255, 255), (0,0,0), (0,0,0)], width=3):
    bgColor, rhomColor, lineColor = colors
    rhomPos, linePos = rhombusPos2(size)
    bg = Image.new("RGB", size, bgColor)
    img = ImageDraw.Draw(bg)  
    img.line(linePos,fill=lineColor, width=width)
    img.polygon(rhomPos, fill=rhomColor)
    bg.show()
    bg.save(path)
    
def drawDis2(path, size, colors=[(255, 255, 255), (0,0,0), (0,0,0)], width=3):
    bgColor, rhomColor, lineColor = colors
    rhomPos, linePos = rhombusPos2(size)
    bg = Image.new("RGB", size, bgColor)
    img = ImageDraw.Draw(bg)  
    img.line(linePos,fill=lineColor, width=width)
    img.polygon(rhomPos, fill=rhomColor)
    # divide line
    per = 4/5
    ap, bp = linePos
    cp, dp = rhomPos[0], rhomPos[2]
    ep ,fp = ((ap[0]*(1-per)+cp[0]*per), (ap[1]*(1-per)+cp[1]*per)), ((bp[0]*(1-per)+dp[0]*per), (bp[1]*(1-per)+dp[1]*per))
    img.line([cp,ep],fill=bgColor, width=width)
    img.line([dp,fp],fill=bgColor, width=width)
    bg.show()
    bg.save(path)
# CrystallisR 2022
import math
import random
from PIL import Image, ImageDraw

# return 2 end points (A & B) of a line 
def linePos(size, margin=0.3, maxf=0.8, minf=0.6):
    wsz, hsz = size
    ssz = min(wsz, hsz)
    # center point of a line segment
    ox, oy = random.randint(wsz*margin, wsz-wsz*margin), random.randint(hsz*margin, hsz-hsz*margin)
    l = random.randint(ssz*minf, ssz*maxf)
    theta = random.randint(0, 180)*math.pi/180 # line angle
    ax, ay = ox - l*math.cos(theta)/2.0, oy + l*math.sin(theta)/2.0
    bx, by = ox + l*math.cos(theta)/2.0, oy - l*math.sin(theta)/2.0
    return [(ax, ay), (bx, by)]

# generate the center coordinate and radius of a circle
# return the top-left and bottom-right corners of the enclosing rectangle
def circlePos(size, margin=0.3, maxr=0.4, minr=0.2):
    wsz, hsz = size
    ssz = min(wsz, hsz)
    # center point of a circle
    ox, oy = random.randint(wsz*margin, wsz-wsz*margin), random.randint(hsz*margin, hsz-hsz*margin)
    radius = random.randint(ssz*minr, ssz*maxr)
    lx, ly = ox - radius*math.cos(math.pi/4), oy - radius*math.sin(math.pi/4)
    rx, ry = ox + radius*math.cos(math.pi/4), oy + radius*math.sin(math.pi/4)
    return (int(lx), int(ly), int(rx), int(ry))

# return the top-left and bottom-right corners of the enclosing rectangle (bounding box)
# and return the start and end angle of the arc
def arcPos(size, margin=0.3, maxr=0.6, minr=0.2, maxp=0.4, minp=0.1):
    wsz, hsz = size
    ssz = min(wsz, hsz)
    # center point of a circle
    ox, oy = random.randint(wsz*margin, wsz-wsz*margin), random.randint(hsz*margin, hsz-hsz*margin)
    radius = random.randint(ssz*minr, ssz*maxr)
    lx, ly = ox - radius*math.cos(math.pi/4), oy - radius*math.sin(math.pi/4)
    rx, ry = ox + radius*math.cos(math.pi/4), oy + radius*math.sin(math.pi/4)
    arclen = random.randint(360*minp, 360*maxp)
    start = random.randint(0, 360)
    end = (start + arclen)%360
    return (lx, ly, rx, ry), start, end

# draw varoius randomly scattered curves
'''
params:
path = where to save the generated figure
size = image size
curvenum = set numbers of desired curves-> from left to right: line, circle, arc
colors = set colors for desired curves-> from left to right: background color, line, circle, arc
'''
def drawCurves(path, size, curvenum=[2, 2, 2], colors=[(255, 255, 255), (0,0,0), (0,0,0), (0,0,0)], width=2):
    # background
    lines, circles, arcs = curvenum
    bgColor, lineColor, circleColor, arcColor = colors
    bg = Image.new("RGB", size, bgColor)
    # create rectangles
    img = ImageDraw.Draw(bg)  
    for i in range(lines):
        pos = linePos(size)
        img.line(pos, fill=lineColor, width=width)
    for i in range(circles):
        pos = circlePos(size)
        img.ellipse(pos, outline=circleColor, width=width)
    for i in range(arcs):
        pos, s, e = arcPos(size)
        img.arc(pos, start=s, end=e, fill=arcColor, width=width)
    bg.show()
    bg.save(path)
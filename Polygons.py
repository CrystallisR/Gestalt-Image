# CrystallisR 2022
import math
import random
from PIL import Image, ImageDraw

# return coordinates of the 4 vertices of a rectangle
# rectangle has 4 vertices which are a, b, c, d in anti-clockwise order
def rectanglePos(size, margin=0.3, wmaxf=0.8, wminf=0.5, hmaxf=0.3, hminf=0.1):
    wsz, hsz = size
    w, h = random.randint(wsz*wminf, wsz*wmaxf), random.randint(hsz*hminf, hsz*hmaxf)
    # center point of a rectangle
    ox, oy = random.randint(wsz*margin, wsz-wsz*margin), random.randint(hsz*margin, hsz-hsz*margin)
    theta = random.randint(0, 180)*math.pi/180 # center line angle
    ctheta, stheta = math.cos(theta), math.sin(theta)
    coords = [(-w/2.0, -h/2.0), (-w/2.0, h/2.0), (w/2.0, h/2.0), (w/2.0, -h/2.0)]
    return [(x*ctheta - y*stheta + ox, x*stheta + y*ctheta + oy) for (x, y) in coords]

# return coordinates of the 4 vertices of a rhombus
# rhombus has 4 vertices which are a, b, c, d in anti-clockwise order
def rhombusPos(size, margin=0.3, maxl=0.4, minl=0.2):
    wsz, hsz = size
    ssz = min(wsz, hsz)
    l1, l2 = random.randint(ssz*minl, ssz*maxl), random.randint(ssz*minl, ssz*maxl)
    # center point of a rhombus
    ox, oy = random.randint(wsz*margin, wsz-wsz*margin), random.randint(hsz*margin, hsz-hsz*margin)
    theta = random.randint(0, 180)*math.pi/180 # center line angle
    coords = [(l1/2.0, l1/2.0), (l2/2.0, l2/2.0), (l1/2.0, l1/2.0), (l2/2.0, l2/2.0)]
    return [(-coords[i][0]*math.cos(theta+i*math.pi/2) + ox, 
            -coords[i][1]*math.sin(theta+i*math.pi/2) + oy) for i in range(4)]

# return coordinates of the 3 vertices of a triangle
# triangle has 3 vertices which are a, b, c in anti-clockwise order
def trianglePos(size, margin=0.3, maxl=0.4, minl=0.2):
    wsz, hsz = size
    ssz = min(wsz, hsz)
    # center point of a triangle
    ox, oy = random.randint(wsz*margin, wsz-wsz*margin), random.randint(hsz*margin, hsz-hsz*margin)
    thetas = [random.randint(0, 360)*math.pi/180 for i in range(3)]
    while thetas[0] == thetas[1] or thetas[0] == thetas[2] or thetas[1] == thetas[2]:
        thetas[1] = random.randint(0, 360)*math.pi/180
        thetas[2] = random.randint(0, 360)*math.pi/180
    ls = [random.randint(ssz*minl, ssz*maxl) for i in range(3)]
    return [(ox + ls[i]*math.cos(thetas[i]), oy + ls[i]*math.sin(thetas[i])) for i in range(3)]

# draw varoius randomly scattered polygons
'''
params:
path = where to save the generated figure
size = image size
polynum = set numbers of desired polygons-> from left to right: rectangle, rhombus, triangle
colors = set colors for desired polygons-> from left to right: background color, rectangle, rhombus, triangle
'''
def drawPolys(path, size=(300, 300), polynum = [2,2,2],
            colors= [(255, 255, 255), (0,0,0), (0,0,0), (0,0,0)]):
    rect, rhom, tri = polynum
    bgColor, rectColor, rhomColor, triColor = colors
    # background
    bg = Image.new("RGB", size, bgColor)
    img = ImageDraw.Draw(bg)  
    if tri >= 2:
        for i in range(int(tri/2)):
            pos = trianglePos(size)
            img.polygon(pos, fill=triColor)
    for i in range(rect):
        pos = rectanglePos(size)
        img.polygon(pos, fill=rectColor)
    for i in range(rhom):
        pos = rhombusPos(size)
        img.polygon(pos, fill=rhomColor)
    for i in range(tri - int(tri/2) if tri >= 2 else tri):
        pos = trianglePos(size)
        img.polygon(pos, fill=triColor)
    bg.show()
    bg.save(path)
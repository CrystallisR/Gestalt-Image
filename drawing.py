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

# draw n randomly scattered rectangles
def drawRectangles(path, n=2, size=(300, 300), bgColor=(255, 255, 255), color=(0,0,0)):
    # background
    bg = Image.new("RGB", size, bgColor)
    # create rectangles
    img = ImageDraw.Draw(bg)  
    for i in range(n):
        pos = rectanglePos(size)
        img.polygon(pos, fill=color)
    bg.show()
    bg.save(path)
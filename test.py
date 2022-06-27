from Polygons import drawPolys
from Curves import drawCurves

SP1 = ('sample/s1.png')
SP2 = ('sample/s2.png')
# image size
W = 800
H = 800 
SIZE = (W, H)
# RGB color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (50, 220, 20)
YELLOW = (255, 255, 0)
RED = (255, 50, 0)

polyn = [2,2,2]
colors1 = [BLACK, GREEN, YELLOW, RED]
curven = [2,2,4]
colors2 = [BLACK, GREEN, YELLOW, RED]
  
# drawPolys(SP1, SIZE, polyn, colors1)
drawCurves(SP2, SIZE, curven, colors2)
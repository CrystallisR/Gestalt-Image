from Polygons import drawPolys
from Curves import drawCurves
from Discontinuity import drawDis, drawDis2

SP1 = ('sample/s1.png')
SP2 = ('sample/s2.png')
SPD1 = ('sample/d1.png')
SPD2 = ('sample/d2.png')
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
curven = [3,3,4]
colors2 = [BLACK, GREEN, YELLOW, RED]
c3 = [BLACK, RED, YELLOW]
c4 = [BLACK, RED, BLACK]
  
drawPolys(SP1, SIZE, polyn, colors1)
drawCurves(SP2, SIZE, curven, colors2)
# drawDis(SPD1, SIZE, c3)
# drawDis2(SPD2, SIZE, c3)
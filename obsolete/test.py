from obsolete.Polygons import drawPolys
from obsolete.Curves import drawCurves
from obsolete.Discontinuity import drawDis, drawDis2
from obsolete.Points import drawPoints
import random

SP1 = ('sample/s1.png')
SP2 = ('sample/s2.png')
SP3 = ('sample/d1.png')
SP4 = ('sample/d2.png')
SP5 = ('sample/m1.png')
# image size
W = 64
H = 64 
SIZE = (W, H)
# RGB color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (50, 220, 20)
YELLOW = (255, 255, 0)
RED = (255, 50, 0)

polyn = [2,2,2]
colors1 = [BLACK, GREEN, YELLOW, RED]
curven = [3,2,2]
colors2 = [BLACK, GREEN, YELLOW, RED]
c3 = [BLACK, RED, YELLOW]
c4 = [BLACK, RED, BLACK]
  
#drawPolys(SP1, SIZE, polyn, colors1)
#drawCurves(SP2, SIZE, curven, colors2)
#drawDis(SPD1, SIZE, c3)
#drawDis2(SPD2, SIZE, c3)
print(random.randint(0,1))
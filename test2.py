import numpy as np
from Points import drawPoints, drawPointsMul

SP1 = ('sample/s1.png')
SP2 = ('sample/s2.png')
SP3 = ('sample/d1.png')
SP4 = ('sample/d2.png')
SP5 = ('sample/m1.png')
SP6 = ('sample/m2.png')
# image size
SIZE = (1, 1)
DPI = 128 # combined with SIZE 128*128 pixels
NUM = 3
# RGB color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (50, 220, 20)
YELLOW = (255, 255, 0)
RED = (255, 50, 0)

colors = ["red","green"]
color_list = np.array(["red","green","blue","yellow","pink","black","orange","purple","brown","gray","cyan","magenta"])
  
#drawPoints(SP5, num=NUM, colors=color_list)
drawPointsMul(SP6, colors=color_list)
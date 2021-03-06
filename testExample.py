import numpy as np
from GestaltImg import Continuity

SP1 = ('sample/s1.png')
SP2 = ('sample/s2.png')
SP3 = ('sample/d1.png')
SP4 = ('sample/d2.png')
SP5 = ('sample/m1.png')
SP6 = ('sample/m2.png')
SP7 = ('sample/n1.png')
SP8 = ('sample/type3_mul_pos.png')
SP9 = ('sample/type3_mul_neg.png')
SPP1 = ('sample/type3_test_pos.png')
SPN1 = ('sample/type3_test_neg.png')
# default parameters
IMG_NUM = 10
RANGE = (2, 3)
SIZE = (1, 1)
DPI = 128 # combined with SIZE: 128*128 pixels
MSZ = 10
INTENSITY = 1.0
COLORS = ["red","green","blue","yellow","pink","black","orange","purple","brown","gray","cyan","magenta"]
COLORS2 = ["black"]
MARKERS = [".", "o", "v", "^", "1", "2", "s", "p", "*", "h", "+", "x", "X", "D"]
  
generator = Continuity(num_range=RANGE, img_sz=SIZE, dpi=DPI, intensity=0.5, colors=COLORS2, markers=MARKERS)
#generator.genPositiveImg(SP5)
#generator.genNegativeImg(SP7)
generator.genNegativeImg(SPN1, type=3)
generator.genPositiveImg(SPP1, type=3)
generator.genNegativeImgSamples(SP9, type=3)
generator.genPositiveImgSamples(SP8, type=3)
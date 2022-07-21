# CRYSTALLISR 2022
from GestaltImg import Continuity
import argparse

# default parameters
PPATH = "positive/p_con_img"
NPATH = "negative/n_con_img"
IMG_NUM = 10
RANGE = (2, 3)
SIZE = (1, 1)
DPI = 128 # combined with SIZE: 128*128 pixels
MSZ = 10
INTENSITY = 0.8
TYPE = 1
COLORS = ["red","green","blue","yellow","pink","black","orange","purple","brown","gray","cyan","magenta"]
COLORS2 = ["black"]
MARKERS = [".", "o", "v", "^", "1", "2", "s", "p", "*", "h", "+", "x", "X", "D"]

parser = argparse.ArgumentParser(description="Generate images which satisfy or dissatisfy Gestalt principle")
parser.add_argument("quantity", type=int, help="the quantity of images you want to generate")
parser.add_argument("-n", "--negative", help="generate negative images", action="store_true")
parser.add_argument("-p", "--path", help="the destination folder and file name of images; images share the same name but different id")
parser.add_argument("-r", "--range", type=int, nargs=2, help="range of curve/line numbers, (2, 5) as default")
parser.add_argument("-s", "--size", type=int, nargs=2, help="image size and w/h ratio, (1, 1) as default")
parser.add_argument("-d", "--dpi", type=int, help="dots per inch, 128 as default")
parser.add_argument("--msz", type=int, help="marker size")
parser.add_argument("-i", "--intensity", type=float, help="noise intensity, 1.0 as default")
parser.add_argument("-c", "--colors", type=str, nargs="+", help="set color list")
parser.add_argument("-m", "--markers", type=str, nargs="+", help="set marker list")
parser.add_argument("-t", "--type", type=int, choices=[1,2,3], help="choose the type of the image")
args = parser.parse_args()

# set arguments
isN = args.negative
q = args.quantity
img_path = args.path if args.path else (NPATH if isN else PPATH)
num_range = tuple(args.range) if args.range else RANGE
img_sz = tuple(args.size) if args.size else SIZE
dpi = args.dpi if args.dpi else DPI
msz = args.msz if args.msz else MSZ
intensity = args.intensity if args.intensity else INTENSITY
colors = list(args.colors) if args.colors else COLORS2
markers = list(args.markers) if args.markers else MARKERS
itype = args.type if args.type else TYPE

generator = Continuity(num_range=num_range, img_sz=img_sz, dpi=dpi, 
                    msz=msz, intensity=intensity, colors=colors, markers=markers)

for i in range(1, q+1):
    print("generating image %d"% i)
    path = (img_path + str(i) + ".png")
    generator.genNegativeImg(path, itype) if isN else generator.genPositiveImg(path, itype)
    
print("Image generation finished")

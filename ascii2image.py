# Name of File  : ascii2image.py
# Type of File  : python 3.6 source file
# Author        : Hannah Leitheiser
# Date          : 2017SEP11
# Description   :
#  Turns an ASCII file back into an image. Expects some header information.
#  requires python3 and PIL, and UbuntuMono-R.ttf 
#  (you will have to change the font for different operating systems.)
import argparse
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

parser = argparse.ArgumentParser(description='Convert an image to ASCII')
parser.add_argument('filename', help='ascii filename to convert')
parser.add_argument('output',help='output filename')
args = parser.parse_args()

asciiFile = open( args.filename )

# ---------------- read the header --------------------------------------

# Example header:
# Rendering Data:
#  White on black background.
#  Image Size: 1000 793
#  Font Size : 24

asciiFile.readline()
invert = False
if asciiFile.readline()[1] == 'W':
	invert = True
widthandheight = asciiFile.readline()[13:-1].split(' ')
width = int(widthandheight[0])
height = int(widthandheight[1])
fontSize = int(asciiFile.readline()[13:-1])

if invert:
   textBackgroundColor = "black"
   textColor = (255,255,255,255)
else:
   textBackgroundColor = "white"
   textColor = (0,0,0,255)

# -------------------- create the image --------------------------------

txtImage = Image.new( 'RGB', (width,height), textBackgroundColor)
draw = ImageDraw.Draw(txtImage)
font = ImageFont.truetype("UbuntuMono-R.ttf", fontSize)
position = 0
line = asciiFile.readline()
while(line != ''):
	draw.text( (0,(position*fontSize)), line,textColor,font=font)
	position=position+1
	line = asciiFile.readline()

txtImage.save( args.output )

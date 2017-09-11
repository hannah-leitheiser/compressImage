# Name of File  : image2glyph.py
# Type of File  : python 3.6 source file
# Author        : Hannah Leitheiser
# Date          : 2017SEP11
# Description   :
#  Turns glyph file into an image.

import argparse
from PIL import Image
import struct

parser = argparse.ArgumentParser(description='Convert an image to ASCII', prog="python image2ascii.py")
parser.add_argument('filename', help='image filename to convert')
parser.add_argument('output',help='output filename')

args = parser.parse_args()

# glyphs for encoding.  Inverses will be used as well.

glyphs = [ ( "00000000",
             "00000000",
             "00000000",
             "00000000",
				 "00000000",
				 "00000000",
				 "00000000",
				 "00000000"), 
     
				("00001111",
				 "00001111",
				 "00001111",
				 "00001111",
				 "11110000",
				 "11110000",
				 "11110000",
				 "11110000"),

				("01010101",
				 "01010101",
				 "01010101",
				 "01010101",
				 "01010101",
				 "01010101",
				 "01010101",
				 "01010101"),
				 
				("00110011",
				 "00110011",
				 "00110011",
				 "00110011",
				 "00110011",
				 "00110011",
				 "00110011",
				 "00110011"),
				 
				("00001111",
				 "00001111",
				 "00001111",
				 "00001111",
				 "00001111",
				 "00001111",
				 "00001111",
				 "00001111"),

				("00000000",
				 "11111111",
				 "00000000",
				 "11111111",
				 "00000000",
				 "11111111",
				 "00000000",
				 "11111111" ),

				("00000000",
				 "00000000",
				 "11111111",
				 "11111111",
				 "00000000",
				 "00000000",
				 "11111111",
				 "11111111" ),

			   ("00000000",
				 "00000000",
				 "00000000",
				 "00000000",
				 "11111111",
				 "11111111",
				 "11111111",
				 "11111111") ]


imageFileName = args.filename
glyphFile = open( args.filename, 'rb')


# get the image size in pixels.
width, height =  struct.unpack('HH', glyphFile.read(4))

image = Image.new( 'RGB', (width,height), "white")
pixels = image.load()

firstNibble = True
for y in range(height//8):
	for x in range(width//8):
		# Again, we have to do some extra work to read nibbles rather
		# than bytes.
		if firstNibble:
			byte = struct.unpack( "B", glyphFile.read(1))[0]
			glyph = byte // 16
			firstNibble = False
		else:
			glyph = byte % 16
			firstNibble = True
		if glyph < 8:
			for blockx in range(8):
				for blocky in range(8):
					color = int(glyphs[glyph][blockx][blocky]) * 255
					pixels[x*(8) + blockx,y * 8 + blocky] =  (color, color, color)
		else:
			for blockx in range(8):
				for blocky in range(8):
					color = (1-int(glyphs[glyph-8][blockx][blocky])) * 255
					pixels[x*(8) + blockx,y * 8 + blocky] =  (color, color, color)

image.save( args.output )
	
glyphFile.close()

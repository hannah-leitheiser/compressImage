# Name of File  : image2glyph.py
# Type of File  : python 3.6 source file
# Author        : Hannah Leitheiser
# Date          : 2017SEP11
# Description   : Turns an image into a binary file for 8x8 pixel glyphs.

import argparse
import struct
from PIL import Image

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

outputFile = open( args.output, 'wb')

image = Image.open(imageFileName)
width, height = image.size

# Write the size of the image

outputFile.write( struct.pack('H', image.size[0]))
outputFile.write( struct.pack('H', image.size[1]))



firstNibble = True
byteToWrite = 0
for y in range(height//8):
	for x in range(width//8):
		deviationMin=1e308

		# The goal here is to look at the glyphs and compare the 8 of them
		# and their inverses to each 8x8 block on the image and see which 
		# fits best (minimizing square of deviations).
		for glyph in range(8):
			for invert in (0, 1):
				deviationSum=0
				for blockx in range(8):
					for blocky in range(8):
						if invert == 0:
							deviationSum += ( int(glyphs[glyph][blockx][blocky]) * 255 -          
                                               (pixelsImage[x*8 + blockx,y * 8 + blocky][0] +
                                                pixelsImage[x*8 + blockx,y * 8 + blocky][1] + 
                                                pixelsImage[x*8 + blockx,y * 8 + blocky][2])                                                
                                                   )**2
						else:
							deviationSum += ( (1-int(glyphs[glyph][blockx][blocky])) * 255 -          
                                               (pixelsImage[x*8 + blockx,y * 8 + blocky][0] +
                                                pixelsImage[x*8 + blockx,y * 8 + blocky][1] + 
                                                pixelsImage[x*8 + blockx,y * 8 + blocky][2])                                                
                                                   )**2
				if deviationSum < deviationMin:
					newChar=glyph+(invert*8)
					deviationMin = deviationSum;
		# This gets a little complicated since I'm trying to pack nibbles (4 bits), not bytes.
		if firstNibble:
			byteToWrite = newChar*16
			firstNibble = False;
		else:
			byteToWrite = byteToWrite + newChar
			outputFile.write( struct.pack("B", byteToWrite));
			firstNibble = True

# write the last nibble if need be.
if not firstNibble:
	byteToWrite = newChar*16
	outputFile.write( struct.pack("B", byteToWrite));

outputFile.close()

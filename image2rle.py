# Name of File  : image2rle.py
# Type of File  : python 3.6 source file
# Author        : Hannah Leitheiser
# Date          : 2017SEP11
# Description of software: Converts an image to a made-up file formate that compresses
#	an image using Run Length Encoding.  All images will be converted to black and white.
#	Ideally the .rle file will be converted back with rle2image.py.
# Invokation example:
#  python rle2image.py myimage.png myimage.rle

from PIL import Image
import struct
import argparse

# ------------------------- parse command line arguments ----------------------------------
# usage: rle2image.py [-h] filename output
#
# Compress an image with Run Length Encoding
#
# positional arguments:
#  filename    image filename to compress
#  output      filename of output
#
# optional arguments:
#   -h, --help  show this help message and exit

parser = argparse.ArgumentParser(description='Compress an imageage with Run Length Encoding')
parser.add_argument('filename', help='image filename to compress')
parser.add_argument('output', help='filename of output', default="output.rle")
args = parser.parse_args()

# ------------------------ open files / create header -------------------------------------

image = Image.open(args.filename)
pixels = image.load()

rleCompressedFile = open( args.output,'wb')

# Save imageage size in first 4 bytes.

rleCompressedFile.write( struct.pack('H', image.size[0]))
rleCompressedFile.write( struct.pack('H', image.size[1]))

# ------------------------------ compress image -------------------------------------------

# Run Length Encoding: Scans the imageage, records the iterations of black or white
# in bytes of the file.  Each consecutive byte represents the opposite color of the last.

black=True
count=0
for x in range(image.size[0]):
	for y in range(image.size[1]):
		# if we fill a byte, we'll have to record 0 for the 
		# opposite color and go back to filling.
		if count == 256:
				rleCompressedFile.write( struct.pack('B', 255));
				rleCompressedFile.write( struct.pack('B', 0));
				count = 1
		color = pixels[x,y]
		if (color[0] + color[1] + color[2]) // 3 < 128:
			if black:
				count = count + 1
			else:
				rleCompressedFile.write( struct.pack('B', count) )
				count = 1
				black = True;
		else:
			if black:
				rleCompressedFile.write( struct.pack('B', count) )
				count = 1
				black = False;
			else:
				count = count + 1

rleCompressedFile.write( struct.pack('B', count) )
rleCompressedFile.close()


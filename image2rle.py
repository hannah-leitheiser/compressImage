# Name of file: rle2image.py
# Author:       Hannah Leitheiser
# Date:         2017SEP10
# Description of software: Converts an image to a made-up RLE (Run Length Encoding) file format.
#	Ideally the .rle file will be converted back with rle2image.py.
# Invokation example:
#  python rle2image.py myimage.png myimage.rle

from PIL import Image
import struct
import argparse

parser = argparse.ArgumentParser(description='Compress an imageage with Run Length Encoding')
parser.add_argument('filename', help='imageage filename to compress')
parser.add_argument('output', help='filename of output', default="output.rle")
args = parser.parse_args()

image = Image.open(args.filename)
pixels = image.load()

rleCompressedFile = open( args.output,'wb')

# Save imageage size in first 4 bytes.

rleCompressedFile.write( struct.pack('H', image.size[0]))
rleCompressedFile.write( struct.pack('H', image.size[1]))

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


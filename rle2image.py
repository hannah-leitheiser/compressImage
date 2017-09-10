# Name of file: rle2image.py
# Author:       Hannah Leitheiser
# Date:         2017SEP10
# Description of software: Converts a made-up RLE (Run Length Encoding) file to a specified image.
#	Ideally the .rle file was created using image2rle.py.
# Invokation example:
#  python rle2image.py myimage.rle myimage.png

from PIL import Image
import struct
import argparse

# ------------------------- parse command line arguments ----------------------------------

#usage: rle2image.py [-h] filename output

# Compress an image with Run Length Encoding
#
# positional arguments:
#   filename    rle filename to decompress
#   output      filename of output image
#
# optional arguments:
#   -h, --help  show this help message and exit


parser = argparse.ArgumentParser(description='Compress an image with Run Length Encoding')
parser.add_argument('filename', help='rle filename to decompress')
parser.add_argument('output', help='filename of output image', default="output.rle")

args = parser.parse_args()

# ------------------------ open files / read header -------------------------------------

rleCompressedFile = open(args.filename, 'rb')

# Read image size from first 4 bytes.

image = Image.new('RGB', struct.unpack('HH', rleCompressedFile.read(4)))

pixels = image.load()

# ------------------------------ decode image -------------------------------------------

# Run Length Encoding: Scans the image, records the iterations of black or white
# in bytes of the file.  Each consecutive byte represents the opposite color of the last.

black=True
count = struct.unpack('B', rleCompressedFile.read(1))[0]

for x in range(image.size[0]):
	for y in range(image.size[1]):
		while count == 0:
			black = not black
			count = struct.unpack('B', rleCompressedFile.read(1))[0]
		if black:
			pixels[x,y] = (0,0,0)
		else:
			pixels[x,y] = (255,255,255)
		count = count - 1

image.save(args.output)



Image Compression Programs
============

This repository contains some examples of simple image compression ideas.  It is created as a programming exercise rather than an attempt to create any competitive image formats.

## Run Length Encoding
### image2rle.py and rle2image.py
Python Scripts to convert images in any format that can be read by Python Imaging Library (PIL) (JPG, PNG, BMP) into a run length encoded file.  Images will be converted to 1-bit monochrome during encoding.  Two two-byte unsigned integers represent the width and height of the image in pixels, the remainder of the file is run lengths in byte-sized unsigned integers.

Usage: 

`python image2rle.py myimage.png myimage.rle`

`python rle2image.py myimage.rle output.png`

## ASCII Encoding
### image2ascii.py and ascii2image.py
Python Scripts turna an image to (extended) ASCII art and back again.  Uses one byte for characters -- no unicode and prints some header information at the beginning so the file can be recreated. 

Usage: 

`python image2rle.py myimage.png myimage.txt`

`python rle2image.py myimage.txt output.png`

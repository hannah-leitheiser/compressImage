Image Compression Programs
============

This repository contains some examples of simple image compression ideas.  It is created as a programming exercise rather than an attempt to create any competitive image formats.

## Run Length Encoding
### image2rle.py and rle2image.py
Python Scripts to convert images in any format that can be read by Python Imaging Library (PIL) (JPG, PNG, BMP) into a run length encoded file.  Images will be converted to 1-bit monochrome during encoding.  Two two-byte unsigned integers represent the width and height of the image in pixels, the remainder of the file is run lengths in byte-sized unsigned integers.

Usage: 

`python image2rle.py images/aceofclubs.bmp images/aceofclubs.rle`

`python rle2image.py images/aceofclubs.rle aceofclubs_rle.png`

aceofclubs_rle.png

![Image of the Ace of Clubs after RLE Compression](https://github.com/hannah-leitheiser/compressImage/blob/master/images/aceofclubs_rle.png)

## ASCII Encoding
### image2ascii.py and ascii2image.py
Python Scripts turn an image to (extended) ASCII art and back again.  Uses one byte for characters -- no unicode and prints some header information at the beginning so the file can be recreated. 

Usage: 

Using font size 12.

`python image2ascii.py -f 12 images/aceofclubs.bmp images/aceofclubs_ascii.txt`

`python rle2image.py images/aceofclubs_ascii.txt images/aceofclubs_ascii.png`

aceofclubs_ascii.png

![Image of the Ace of Clubs after ASCII Compression](https://github.com/hannah-leitheiser/compressImage/blob/master/images/aceofclubs_ascii.png)


## Glyph Encoding
### image2glyph.py and glyph2image.py
Python Scripts turn an image to a binary glyph file and back again.  There are 16 predefined black-and-white glyphs of 8x8 pixels in lengh, and the file encodes the best match for each block in the given image.  Lossy compression method.

Usage: 

`python image2glyph.py myimage.png myimage.glyph`

`python glyph2image.py myimage.glyph output.png`

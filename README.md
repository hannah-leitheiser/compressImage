Image Compression Programs
============

This repository contains some examples of simple image compression ideas.  It is created as a programming exercise rather than an attempt to create any competitive image formats.

## image2rle.py and rle2image.py
Python Scripts to convert images in any format that can be read by Python Imaging Library (PIL) (JPG, PNG, BMP) into a run length encoded file.  Images will be converted to 1-bit monochrome during encoding.  Two two-byte unsigned integers represent the width and height of the image in pixels, the remainder of the file is run lengths in byte-sized unsigned integers.

Usage: 
'python image2rle.py test.png test.rle'
'python rle2image test.rle output.png'

import numpy as np
from PIL import Image
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import math
import struct
import random


image = Image.open("fs.jpg")
width, height = image.size
pixels = image.load()


def encode(data):
	encodedData = [0.0]*len(data)
	for x in range(len(data)):
		for y in range(len(data)):
			encodedData[x]+=data[y]*math.cos(math.pi*x*(y+0.5)/(len(data)))*(2/len(data))
	return encodedData

def decode(data):
	encodedData = [0.0]*len(data)

	for r in range(len(data)):
		for x in range(len(data)):
			if x==0: encodedData[r]+=data[x]*0.5
			else: encodedData[r]+=data[x]*math.cos(math.pi*x*(r+0.5)/len(data))
	return encodedData


pixeldata= [0]*3
for x in range(3):
	pixeldata[x]= [0]*height
for c in range(3):
	for x in range(height):
		pixeldata[c][x] = [0.0]*width

length=width

a = [0]*length
b = [0]*length
c=  [0]*length

for color in range(3):
	print(color)
	for h in range(height):
		for x in range(width):
			pixeldata[color][h][x]=int(pixels[x, h][color])

	for h in range(height):
		print(" h: ", h)
		pixeldata[color][h]=list(encode(tuple(pixeldata[color][h])))

	for x in range(width):
		print(" w: ", x)
		column = [0.0]*height
		for h in range(height):
			column[h]=pixeldata[color][h][x]
		column = encode(column)
		for h in range(height):
			pixeldata[color][h][x]=column[h]


pixeldata2= [0]*3
for x in range(3):
	pixeldata2[x]= [0]*height
for c in range(3):
	for x in range(height):
		pixeldata2[c][x] = [0.0]*width


frames = 200
for frame in range(frames):

	for h in range(height):
		for x in range(width):
			for color in range(3):
				if x < width * (frame/frames) and h < width * (frame/frames):
					pixeldata2[color][h][x] = pixeldata[color][h][x]
				else:
					pixeldata2[color][h][x] = 0
				
	for color in range(3):
		for x in range(width):
			column = [0.0]*height
			for h in range(height):
				column[h]=pixeldata2[color][h][x]
			column = decode(column)
			for h in range(height):
				pixeldata2[color][h][x]=column[h]

	for color in range(3):
		for h in range(height):
			pixeldata2[color][h]=list(decode(tuple(pixeldata2[color][h])))
	
	for color in range(3):
		for h in range(height):
			for r in range(length):
				if(color == 0):
					pixels[r,h]=(int(pixeldata2[color][h][r]),pixels[r,h][1], pixels[r,h][2],255)
				if(color == 1):
					pixels[r,h]=(pixels[r,h][0], int(pixeldata2[color][h][r]),pixels[r,h][2],255)
				if(color == 2):
					pixels[r,h]=(pixels[r,h][0], pixels[r,h][1],int(pixeldata2[color][h][r]),255)


	image.save('out{:04}.png'.format(frame));


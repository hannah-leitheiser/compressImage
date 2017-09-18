import numpy as np
from PIL import Image
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import math
import struct
import random
import numpy

chunkSize=8

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


def encode2DArea(area):
	height=len(area)
	width=len(area[0])
	for h in range(len(area) ):
		area[h]=encode(area[h])

	for x in range(width):
		column = [0.0]*height
		for h in range(height):
			column[h]=area[h][x]
		column = encode(column)
		for h in range(height):
			area[h][x]=column[h]
	return area

	

pixeldata= [0]*3
for x in range(3):
	pixeldata[x]= [0]*height
for c in range(3):
	for x in range(height):
		pixeldata[c][x] = [0.0]*width

length=width

numbers = []

for color in range(3):
	for blockx in range(width//chunkSize):
		for blocky in range(height//chunkSize):
			chunk = numpy.zeros([chunkSize,chunkSize])
			for h in range(chunkSize):
				for x in range(chunkSize):
					chunk[h][x]=pixels[x + blockx*chunkSize, h + blocky*chunkSize][color]

			encode2DArea(chunk)

			#if blockx == 0 and blocky == 0:
			#	print( chunk )
			for x in range(chunkSize):
				for y in range(chunkSize):
					anum=chunk[x][y]
					anum=(anum//3) + 3
					if anum > 255: anum = 255
					if anum < 0: anum = 0
					numbers.append(int(anum))
					chunk[x][y]=(anum-3)*3

					


			for x in range(chunkSize):
				column = [0.0]*chunkSize
				for h in range(chunkSize):
					column[h]=chunk[h][x]
				column = decode(column)
				for h in range(chunkSize):
					chunk[h][x]=column[h]

			for h in range(chunkSize):
				chunk[h]=list(decode(tuple(chunk[h])))
	
			for h1 in range(chunkSize):
				for r1 in range(chunkSize):
					h=h1+blocky*chunkSize
					r=r1+blockx*chunkSize
					if(color == 0):
						pixels[r,h]=(int(chunk[h1][r1]),pixels[r,h][1], pixels[r,h][2],255)
					if(color == 1):
						pixels[r,h]=(pixels[r,h][0], int(chunk[h1][r1]),pixels[r,h][2],255)
					if(color == 2):
						pixels[r,h]=(pixels[r,h][0], pixels[r,h][1],int(chunk[h1][r1]),255)

image.save('fsout.png');

#import matplotlib.pyplot as plt
#plt.hist(numbers[:1000],32)
print( numpy.histogram( numbers[:1000], bins=256) )
#plt.title('Histogram of 8-bit quantized values.')
#plt.show()

saveFile = open('output.hpg', 'wb')



saveNum = 0
for x in range( len(numbers) ):
		saveNum = numbers[x]
		saveFile.write ( struct.pack( 'B', saveNum ) )
saveFile.close()


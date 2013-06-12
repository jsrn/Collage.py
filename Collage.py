from __future__ import division
import os
from PIL import Image
import math

outputdir = 'out/'

imagelist = os.listdir("images")
count = len(imagelist)

heighttotal = 0
for imagename in imagelist:
	im = Image.open("images/" + imagename)
	width, height = im.size
	heighttotal += height


newheight = heighttotal / count

for imagename in imagelist:
	im = Image.open("images/" + imagename)
	width, height = im.size
	newwidth = (height / newheight) * width
	newsize = newwidth, newheight
	im = im.resize((int(newwidth), int(newheight)), Image.ANTIALIAS)
	im.save(outputdir + imagename, "JPEG")

# That mostly works, but with some bizzare aspect ratio issues

# Calculate how much space we need
maxwidth = 800
row = 0
xoffset = 0

for imagename in imagelist:
	im = Image.open("out/" + imagename)
	width, height = im.size
	if xoffset + width > maxwidth:
		row += 1
		xoffset = 0
	else:
		xoffset += width

requiredheight = math.ceil(row * newheight)
print "Required height: " + str(requiredheight) 

blank_image = Image.new("RGB", (maxwidth, int(requiredheight)))

row = 0
xoffset = 0

for imagename in imagelist:
	im = Image.open("out/" + imagename)
	width, height = im.size
	if xoffset + width > maxwidth:
		row += 1
		xoffset = 0
	print "Pasting to: " + str(xoffset) + "," + str(int(row*newheight))
	blank_image.paste(im, ( xoffset, int(row*newheight) ))
	xoffset += width

blank_image.save(outputdir + 'collage.jpg', "JPEG")
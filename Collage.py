from __future__ import division
import os
from PIL import Image
import math

outputdir = 'out/'
backgroundcolour = (209, 175, 121)
borderwidth = 2;

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
	modifier = newheight / height
	newwidth = width * modifier
	newsize = newwidth, newheight
	im = im.resize((int(newwidth), int(newheight)), Image.ANTIALIAS)
	im.save(outputdir + imagename, "JPEG")

# That mostly works, but with some bizzare aspect ratio issues

# Calculate how much space we need
maxwidth = 800
row = 0
xoffset = borderwidth

for imagename in imagelist:
	im = Image.open("out/" + imagename)
	width, height = im.size
	if xoffset + width + borderwidth > maxwidth:
		row += 1
		xoffset = 0
	xoffset += width + borderwidth

requiredheight = math.ceil((row+1) * newheight + (row+1)*borderwidth)
print "Required height: " + str(requiredheight) 

blank_image = Image.new("RGB", (maxwidth, int(requiredheight)), backgroundcolour)

row = 0
xoffset = borderwidth

for imagename in imagelist:
	im = Image.open("out/" + imagename)
	width, height = im.size
	if xoffset + width + borderwidth > maxwidth:
		row += 1
		xoffset = 0
	print "Pasting to: " + str(xoffset) + "," + str(int(row*newheight) + (row+1)*borderwidth )
	blank_image.paste(im, ( xoffset + borderwidth, int(row*newheight + (row+1)*borderwidth) ))
	xoffset += width + borderwidth

blank_image.save(outputdir + 'collage.jpg', "JPEG")
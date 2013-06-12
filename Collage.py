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

maxwidth = 800

blank_image = Image.new("RGB", (maxwidth, 200), backgroundcolour)

row = 0
xoffset = borderwidth

for imagename in imagelist:
	im = Image.open("out/" + imagename)
	width, height = im.size

	if xoffset + width + borderwidth > maxwidth:
		row += 1
		xoffset = 0

	requiredheight = int(math.ceil((row+1) * newheight + (row+1)*borderwidth))
	if blank_image.size[1] < requiredheight:
		new_blank_image = Image.new("RGB", (maxwidth, requiredheight), backgroundcolour)
		new_blank_image.paste(blank_image, (0,0));
		blank_image = new_blank_image

	blank_image.paste(im, ( xoffset + borderwidth, int(row*newheight + (row+1)*borderwidth) ))
	xoffset += width + borderwidth

blank_image.save(outputdir + 'collage.jpg', "JPEG")

print str(count) + " images processed."
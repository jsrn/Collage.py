from __future__ import division
import os
from PIL import Image
import math

def trim( image ):
	width, height = image.size
	clearRow = True
	for i in xrange( height ):
		r, g, b = image.getpixel( ( width - 3, i ) )
		if r is not 209 or g is not 175 or b is not 121:
			clearRow = False
	if clearRow is True:
		return trim ( image.crop( ( 0, 0, width - 1, height ) ) )
	else:
		return image

def get_mean_height( images ):
	total = 0
	for im in images:
		total += im.size[1]
	return int(total / len(images))

backgroundcolour = (209, 175, 121)
borderwidth = 2
maxwidth = 1200

imagelist = os.listdir("images")

oldimages = []
newimages = []

for imagename in imagelist:
	oldimages.append( Image.open("images/" + imagename) )

newheight = get_mean_height( oldimages )

for im in oldimages:
	width, height = im.size
	modifier = newheight / height
	newwidth = width * modifier
	newsize = newwidth, newheight
	im = im.resize((int(newwidth), int(newheight)), Image.ANTIALIAS)
	newimages.append(im)

blank_image = Image.new("RGB", (maxwidth, 200), backgroundcolour)

row = 0
xoffset = 0

for im in newimages:
	width, height = im.size

	if xoffset + width + borderwidth > maxwidth:
		row += 1
		xoffset = 0

	requiredheight = int(math.ceil((row+1) * newheight + (row+1)*borderwidth + borderwidth))
	if blank_image.size[1] < requiredheight:
		new_blank_image = Image.new("RGB", (maxwidth, requiredheight), backgroundcolour)
		new_blank_image.paste(blank_image, (0,0));
		blank_image = new_blank_image

	blank_image.paste(im, ( xoffset + borderwidth, int(row*newheight + (row+1)*borderwidth) ))
	xoffset += width + borderwidth

blank_image = trim( blank_image )

blank_image.save( 'collage.png', "PNG" )

print str( len( oldimages ) ) + " images processed."
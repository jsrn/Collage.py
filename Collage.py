from __future__ import division
import os
from PIL import Image

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


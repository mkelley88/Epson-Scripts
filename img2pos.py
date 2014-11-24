#!/usr/bin/python
'''
@author: Matthew T. Kelley
@organization: http://www.mkelley.info
@copyright: Copyright (c) 2014 Matthew T Kelley
@license: GPL

 Using Pillow to provide the Python Imaging Library (PIL)
 Written and tested under Python 2.7
 Code requires modifications to escpos/constants.py
 Python-ESCPOS may be obtained from these sources:
     Original: https://code.google.com/p/python-escpos/
     My fork: https://github.com/mkelley88/python-escpos
 My fork is highly recommended and may be requried to use my scripts.
'''

from __future__ import print_function
from escpos import *
from PIL import Image
import sys

# Setup serial object. Set your port and baudrate here!
Epson = printer.Serial("/dev/ttyUSB0",38400)

#Epson.setPrintSpeed("57600")
#Epson = printer.Serial("/dev/ttyUSB1",57600)

# Try to open image file provided at command line:
for infile in sys.argv[1:]:
    try:
        im = Image.open(infile)
    except IOError:
        pass

# If image width is higher than 512 pixels, the image will be resized 
# to 512px while keeping the original aspect ratio using calculations.
# This calculates the new image size to be sent to the function printIt()
if im.size[0] > 512:
    imgWidth = 512
    if im.size[1] > im.size[0]:
        imgHeight = int(imgWidth * (im.size[0] / float(im.size[1])))
    else:
        imgHeight = int(imgWidth * (im.size[1] / float(im.size[0])))

else:
    imgWidth = im.size[0]
    imgHeight = im.size[1]

# Uses new width and height, resizes image, then prints the image in 255px (height) chunks until complete.
def printIt(width, height):
    y = 0
    brk = 0
    if  im.size[0] > 500:
        out = im.resize((width, height))
    else:
        out = im.resize((im.size[0],im.size[1]))

    print ("Height = %d" % height)
    for y in range(0, height): 
        if (y*255+255) > height:
            box = (0, y*255, width, height)
            brk = 1
    	else: 
            box = (0, y*255, width, y*255+255 )
	print (box)    
	out1 = out.crop(box)
    	out1.save("out1.png", "PNG")
    	Epson.image("out1.png")
	y += 255
        if brk != 0:
            break
                     
    Epson.cut()

print(im.size[0],"x",im.size[1])  # DEBUG #
print(imgWidth,"x",imgHeight)     # DEBUG #
printIt(imgWidth,imgHeight)

# TO DO #
'''
    Possible text based progress bar
    Clean up messy code
    Make usable as a library?
'''
 

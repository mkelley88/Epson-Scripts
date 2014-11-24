Epson-Scripts
=============

Scripts for using python-escpos, pillow, and various linux based software with the Epson TM-T88 model POS themal receipt printers.

Development Tools Used
  Software: 
    Raspbian (debian varient)
  Hardware: 
    Raspberry Pi 512MB Rev B
    TM-T88IV, TM-T88III, TM-T88II
    Prolific USB -> Serial Adapter (Configure your port settings in the scripts)

Img2pos.py
----------

This script will take an image provided at the command line and print it on a escpos compatable printer.
  - Tested on TM-T88 III,IV

Usage: python img2pos.py yourImageHere.png

It is configured for 512px wide max, for the TM-T88IV prints that wide.

It may be possible to use this on Adafruit / Sparkfun thermal printers?
  Although modifications for print width would have to be made.

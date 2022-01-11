#!/usr/bin/env python3
#
# fontcontains.py: a utility to determine whether a font contains a series of glyphs
#
# fontcontains.py <font file> <glyphs>

import sys
import os.path
from fontTools.ttLib import TTFont

if 2 > len(sys.argv) > 3:
	print(sys.argv[0], "<font file>", "<glyphs>")
	exit()

if not os.path.exists(sys.argv[1]):
	print("can't read font file", sys.argv[1])
	exit()

argv2='ĈĜĤĴŜŬĉĝĥĵŝŭ'
if len(sys.argv) == 3:
	argv2 = sys.argv[2]
if os.path.exists(argv2):
	# assume that if the text is a file name, then the text in the file is meant
	with open(argv2, 'r') as f:
		argv2=f.read()

# this is a sorted list of ord values for the glyphs present in the text
glyphs=sorted(list(set([ord(x) for x in argv2])))
MAX=glyphs[-1]

# This uses fonttools to determine the list of glyphs defined. Could be one-lined, but wanted to
# show the APIs used
f = TTFont(sys.argv[1])
g = f.getGlyphSet()
c = f['cmap']
t = c.tables
chars = []
for table in t:
    chars += table.cmap.keys()
chars = sorted(list(set(chars)))

for g in glyphs:
	if g < 32:
		continue
	if g not in chars:
		print(chr(g), g, "is not contained")

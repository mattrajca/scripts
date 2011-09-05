#!/usr/bin/env python

# A script which ejects any disc image files passed as arguments

import string, os, sys

lines = os.popen("hdiutil info").readlines()
should_eject = False

for line in lines:
	if line.startswith("image-alias"):
		path = line.split(":")[1]
		image_path = path.lstrip().rstrip()
		
		if image_path in sys.argv:
			should_eject = True
	
	elif line.startswith("/dev/") and should_eject is True:
		os.popen("hdiutil eject %s" % line.split()[0])
		should_eject = False
	
	elif line.startswith("###"):
		should_eject = False


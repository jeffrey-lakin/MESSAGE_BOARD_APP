#!/usr/bin/env python

import EXIF
import os
import sys

f = open(sys.argv[1], 'rb')
tags = EXIF.process_file(f, details=False)
dateTime = tags['EXIF DateTimeOriginal']
print str(dateTime)

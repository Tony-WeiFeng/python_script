#/usr/bin/env python
import re

'''readTextFile.py -- read and display text file'''

#attempt to open file for reading

fname = 'C:\\A\\test.txt'
lineList = []
try:
	fobj = open(fname, 'r')
except IOError, e:
	print "File open error:", e
else:
	#display contents to the screen
	for eachLine in fobj:
		if (re.match(r'\d{2}:\d{2}:\d{2}',eachLine)):
			lineList.append(eachLine)
	fobj.close()
print lineList
#!/usr/bin/env python

"""
skua is a tool to download data, such as pictures or videos, from websites.

Usage information is shown by running: ./skua.py

More information is available at https://github.com/THLO/skua.
"""

import urllib2, requests, time, random,sys
import argparse
from collections import OrderedDict

# Version number
version = '0.0.4'

# Default values for certain parameters:

# The prefix is prepended to the original filename, resulting in the filename
# that is used when storing the downloaded file.
# By default, the prefix is the emtpy string.
defaultDestination = ''

# Only files are downloaded with a certain extension.
# By default, the allowed extension is 'jpg'.
defaultExtension = 'jpg'

# A random timeout chosen uniformly at random from the range
# [minimumTimeout,maximumTimeout] occurs between downloads.
#By default, this range is [0.5,5.0] in seconds.
defaultMinimumTimeout = 0.5
defaultMaximumTimeout = 5.0

# Site-specific parameters can be added in the form of key-value pairs.
# By default, there are no such parameters.
defaultParameter = ''

""" Helper function to test if a string is an integer. """
def isInt(string):
    try: 
        int(string)
        return True
    except ValueError:
        return False

"""
An example for a filter:
File containing [int]x[int] are dropped because they (often) refer to
rescaled images.
"""
def filterRescaled(items):
	filteredList = []
	for item in items:
		pos = item.rfind('x')
		if not(pos >= 0 and pos < len(item)-1 and isInt(item[pos-1]) and isInt(item[pos+1])):
			filteredList.append(item)
	return filteredList

"""
A simple usage message is printed by this method.
This will be replaced by argparse.
"""
def printUsage():
	print "Usage: skua [URL] {prefix} {extension}"
	print "* URL (mandatory): Website from which files should be downloaded."
	print "* Prefix (optional): Prefix added to the files that are downloaded."
	print "  Default: Empty"
	print "* Extension (optional): Only files with the given extension are downloaded."
	print "  Default: jpg"

# The first parameter is the URL
if len(sys.argv) < 2:
	printUsage()
else:
	url = sys.argv[1]
	prefix = defaultDestination if len(sys.argv) < 3 else sys.argv[2]
	extension = defaultExtension if len(sys.argv) < 4 else sys.argv[3]
	minimumTimeout = defaultMinimumTimeout
	maximumTimeout = defaultMaximumTimeout

	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
	req = urllib2.Request(url, headers=hdr)
	response = urllib2.urlopen(req)
	html = response.read()
	pieces = html.split("\"")
	items = [piece for piece in pieces if piece.endswith(extension)]
	itemsNoDuplicates = list(OrderedDict.fromkeys(items))
	filteredList = filterRescaled(itemsNoDuplicates)
	for item in filteredList:
		if item.startswith("//"):
			item = "https:"+item
		print "Downloading "+item+"..."
		try:
			data = requests.get(item)
			itemNameParts = item.split("/")
			f = open(prefix+itemNameParts[-1], "wb")
			f.write(data.content)
			f.close()
			time.sleep(random.uniform(minimumTimeout,maximumTimeout))
		except:
			pass

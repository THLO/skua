"""
Created on Mon March 2 11:05:00 2016

@author: THLO
"""

import urllib2, requests, time, random,sys
from collections import OrderedDict

# Version number
version = '0.0.2'

# Default values for certain parameters:

# The prefix is prepended to the original filename, resulting in the filename
# that is used when storing the downloaded file.
# By default, the prefix is the emtpy string.
defaultPrefix = ''

# Only files are downloaded with a certain extension.
# By default, the allowed extension is 'jpg'.
defaultExtension = 'jpg'

# A random timeout chosen uniformly at random from the range
# [minimumTimeout,maximumTimeout] occurs between downloads.
#By default, this range is [0.5,5.0] in seconds.
defaultMinimumTimeout = 0.5
defaultMaximumTimeout = 5.0

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
	prefix = defaultPrefix if len(sys.argv) < 3 else sys.argv[2]
	extension = defaultExtension if len(sys.argv) < 4 else sys.argv[3]
	minimumTimeout = defaultMinimumTimeout
	maximumTimeout = defaultMaximumTimeout

	#hdr = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
	req = urllib2.Request(url, headers=hdr)
	response = urllib2.urlopen(req)
	html = response.read()
	pieces = html.split("\"")
	items = [piece for piece in pieces if piece.endswith(extension)]
	itemsNoDuplicates = list(OrderedDict.fromkeys(items))
	for item in itemsNoDuplicates:
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
		

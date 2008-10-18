#!/usr/bin/env python

import sys
import os
import re

def main(argv):
	dirList = open(argv[1], "r")
	filename = ".gitignore"
	for dirPath in dirList:
		# create empty directory
		if "+empty_dir:" in dirPath:
			try:
				emptyPath=re.sub("^.*\+empty_dir:\strunk/","",dirPath)
				print emptyPath
				os.makedirs(emptyPath.strip())
			except OSError: # directory already exists
					pass
				# create placeholder file if not present yet
			f = open(emptyPath.strip()+os.sep+filename, "a+")
			f.close()
	dirList.close()

if __name__ == "__main__":
	sys.exit(main(sys.argv))

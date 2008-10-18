#!/usr/bin/env python
"""
This script parses the 'git svn' "unhandled.log" file for
all empty directories that have been created and are ignored
by git. It then creates _all_ of those directories and places
a ".gitignore" file into them. That way one can make sure that
his 'git svn' checkout will behave just like a svn checkout would
(e.g., some badly written Makefile might rely on empty dirs during
buil process).

Usage: python batchCreateDirsGitignore.py /path/to/trunk/unhandled.log

Shortcommings:
	* This is hardcoded for use on "unhandled.log" files from the
		tunk branch of svn.
	* It will create _all_ empty directories that have ever been
		during the subversion history (also those that have been
		removed a a later time). Although this is does not brake
		it will leave you with more empty dirs in your git checkout
		than are actually present in the current svn repo.
	* It is probably worth checking the current state of the svn repo
		and then simply remove empty dirs which were removed during
		svn history.
"""
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

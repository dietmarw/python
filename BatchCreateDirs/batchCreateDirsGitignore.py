#!/usr/bin/env python

import os

dirList = open("list.txt", "r")
filename = ".gitignore"

for dirPath in dirList:
    # create empty directory
    try:
        os.makedirs(dirPath.strip())
    except OSError: # directory already exists
        pass
    # create placeholder file if not present yet
    f = open(dirPath.strip()+os.sep+filename, "a+")
    f.close()

dirList.close()
import os
for line in open("list.txt").readlines():
    directory = line.strip()
    os.makedirs(directory)
    f = open(directory+"/.gitignore","w");f.close()

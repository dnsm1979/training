import os, sys, fnmatch

root = "D:\\1"
pattern = "*.txt"
for folder, subdirs, files in os.walk(root):
    print(folder)
    for filename in fnmatch.filter(files, pattern):
        fullname = os.path.join(folder, filename)
        print(fullname)

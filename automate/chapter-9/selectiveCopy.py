#! python3
# selectiveCopy.py - copies every file with a certain extension and
# moves them to a new folder
# selectiveCopy.py [folder to copy] [folder to copy to]

import os, sys, shutil

## TODO get arguments 
## TODO Walk folder, get list
## TODO copy from A to B

print(sys.argv)

if len(sys.argv) != 3:
    print('Requires 2 arguments:\n selectiveCopy.py <copy folder> <destination folder>')

else:
    source = sys.argv[1]
    dest = sys.argv[2]
    for folder, subfolder, filenames in os.walk(source):
        print(folder)
        shutil.copy(folder, dest)
        print(subfolder)
        print(filenames)

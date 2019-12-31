#! python3
# madLib.py - a mad-lib based program, run from command line

import os, sys, re

# Generate mad lib regex
madLibRegex = re.compile(r'(\WNOUN\W)|(\WADJECTIVE\W)|(\WVERB\W)|(\WADVERB\W)')

# Get the data from the file
if len(sys.argv) != 2:
    print('Usage: madLib.py [file] - start your mad lib!')
    sys.exit()
else:
    mlPath = os.path.split(sys.argv[1])
    mlFile = open(sys.argv[1])
    ml = mlFile.read()

# TODO Regex search the file for CAPS text


# TODO Get input from user

# TODO Replace using Regex

# TODO Save to new file

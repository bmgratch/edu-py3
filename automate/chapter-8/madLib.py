#! python3
# madLib.py - a mad-lib based program, run from command line

import os, sys, re

# Generate mad lib regex
madLibRegex = re.compile(r'((NOUN)|(ADJECTIVE)|(VERB)|(ADVERB))')
nounRegex = re.compile(r'\WNOUN')
adjRegex = re.compile(r'\WADJECTIVE')
verbRegex = re.compile(r'\WVERB')
advRegex = re.compile(r'\WADVERB')

# Get the data from the file
if len(sys.argv) != 2:
    print('Usage: madLib.py [file] - start your mad lib!')
    sys.exit()
else:
    mlPath = os.path.split(sys.argv[1])
    mlFile = open(sys.argv[1])
    ml = mlFile.read()

# TODO Regex search the file for CAPS text
while True:
    libRep = madLibRegex.search(ml)
    if 
    print("Enter a " + libRep.group().lower())
    rep = input()
    ml = madLibRegex.sub(rep, ml, 1)
    print(ml)
    
# TODO Save to new file

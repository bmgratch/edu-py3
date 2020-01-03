#! python3
# madLib.py - a mad-lib based program, run from command line

import os, sys, re

# Generate mad lib regex
madLibRegex = re.compile(r'((NOUN)|(ADJECTIVE)|(VERB)|(ADVERB))')

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
    #try/except here to break when completed
    try:
        print("Enter a " + libRep.group().lower())
        rep = input()
        ml = madLibRegex.sub(rep, ml, 1)
        print(ml)
    except AttributeError:
        break
    
# Save to new file, madlib_FILE.txt
madLibComplete = open(f'madlib_{str(sys.argv[1])}' , 'w') #makes the file
madLibComplete.write(ml)            # this should be done!
madLibComplete.close()              #close file
mlFile.close()

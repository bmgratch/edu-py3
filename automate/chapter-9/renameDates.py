#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY.

import shutil, os, re

# create a regex for matching American date format.

datePatter= re.compile(r"""^(.*?)
                ((0|1)?\d)-
                ((0/1/2/3)?\d)-
                ((19/20)\d\d)
                (.*?)$
                """, re.VERBOSE)

# Loop over the files in the working directory
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)
    # Skip files without a date
    if mo == None:
        continue
    # Get the differnt parts of the filename
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)
    
    # Form the european style filename!
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
    # get the full, absolute filepath
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absworkingDir, euroFilename)

    # rename the files
    print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
    #shutil.move(amerFilename, euroFilename)    # uncomment after testing

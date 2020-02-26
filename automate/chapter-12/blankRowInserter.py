#! python3
# blankRowInserter.py - inserts blank rows into a spreadsheet
# usage: python blankRowInserter.py <row> <blanks> <file.xlsx>

import sys, openpyxl

# Get parameters from command line
if len(sys.argv) == 4:
    startRow = sys.argv[1]
    blankRow = sys.argv[2]
    file = sys.argv[3]
else:
    print("Proper Usage: blankRowInserter.py (row) (blanks) (file.xlsx)")
    sys.exit()

# TODO Open file

# TODO add blanks

# TODO save file

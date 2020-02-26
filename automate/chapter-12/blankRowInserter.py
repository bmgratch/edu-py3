#! python3
# blankRowInserter.py - inserts blank rows into a spreadsheet
# usage: python blankRowInserter.py <row> <blanks> <file.xlsx>

import sys, openpyxl

if len(sys.argv) == 4:
    pass
else:
    print("Proper Usage: blankRowInserter.py (row) (blanks) (file.xlsx)")
    sys.exit()

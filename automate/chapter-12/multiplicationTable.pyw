#! python3
# multiplicationTable.py - creates a spreadsheet multiplication table in Excel
# py multiplicationTable.py (N) - creates a spreadsheet N by N

import openpyxl, sys

# get N from command line
if len(sys.argv) == 2:
    n = sys.argv[1]

# Open a sheet
mTable = openpyxl.load_workbook('multipliation-table-%s.xlsx' % n)
sheet = wb.active

# TODO create the table
# TODO N wide by N down
for col in range(2, n):
    pass

# saving:
wb.save('multiplication-table-%s.xlsx' % n)

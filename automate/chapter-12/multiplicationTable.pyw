#! python3
# multiplicationTable.py - creates a spreadsheet multiplication table in Excel
# py multiplicationTable.py (N) - creates a spreadsheet N by N

import openpyxl, sys

# get N from command line
if len(sys.argv) == 2:
    n = sys.argv[1]
else:
    n = 0

# Open a sheet
mTable = openpyxl.Workbook()
sheet = mTable.active
sheet.title = 'Multiplication %s' % n

# TODO create the table
# TODO N wide by N down
for val in range(1, n):
    sheet.cell(row = 1, column = val + 1).value = val

# saving:
mTable.save('multiplication-table-%s.xlsx' % n)

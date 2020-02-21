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
mTable = openpyxl.load_workbook('multipliation-table-%s.xlsx' % n, 'w')
sheet = wb.active

# TODO create the table
# TODO N wide by N down
for val in range(1, n):
    sheet.cell(row = 1, column = val + 1).value = val

# saving:
wb.save('multiplication-table-%s.xlsx' % n)

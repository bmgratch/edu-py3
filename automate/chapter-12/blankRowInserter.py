#! python3
# blankRowInserter.py - inserts blank rows into a spreadsheet
# usage: python blankRowInserter.py <row> <blanks> <file.xlsx>

import sys, openpyxl

# Get parameters from command line
if len(sys.argv) == 4:
    startRow = int(sys.argv[1])
    blankRow = int(sys.argv[2])
    file = sys.argv[3]
else:
    print("Proper Usage: blankRowInserter.py (row) (blanks) (file.xlsx)")
    #sys.exit()
    #for testing
    startRow = 4
    blankRow = 2
    file = 'multiplication-table-10.xlsx'
    

# Open file
wb = openpyxl.load_workbook(file)
sheet = wb.active
wb2 = openpyxl.Workbook()
sheet2 = wb2.active
sheet2.title = sheet.title #copy sheet title, why not

# TODO copy rows, add blanks
for row in range(1, sheet.max_row):
    if row < startRow:
        #copy to row
        pass
    else:
        #copy to row + blankRow
        pass

# Save file as file_new.xlsx

wb2.save('new_%s' % file)

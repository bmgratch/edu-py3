#! python3
#
# Chapter 6 practice project 1

def printTable(lString):
    colWidths = [0] * len(lString)  # create a column width list
    for x in range(0, len(lString)):
        for l in lString[x]:
            if colWidths[x] < len(l):
                colWidths[x] = len(l)

    for iL in range(0, len(lString[0])):
        for iC in range(0, len(lString)):
            print(lString[iC][iL].rjust(colWidths[iC]), end=' ')
        print('\n')

# assigned sample data from 
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)

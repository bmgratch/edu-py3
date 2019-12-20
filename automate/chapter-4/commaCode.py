def commaCode(anyList):
    strList = ''
    for a in range(0, len(anyList)):
        if a == len(anyList) - 1:
            strList += ' and '
        elif a != 0:
            strList += ', '            
        strList += anyList[a]
    return strList

spam = ['apples', 'bananas', 'tofu', 'cats']

print(commaCode(spam))

#! python3
# brute-force.py is a brute force pdf-password checker.

import PyPDF2, sys
pwDict = 'dictionary.txt'

#get .pdf from command line
if len(sys.argv) == 2:
    pdfFile = sys.argv[1]
else:
    #some kind of error
    pass

# First load the dictionary of passwords
pwFile = open(pwDict)

# second, load the PDF
pdfReader = PyPDF2.PdfFileReader(open(pdfFile), rb)
if not pdfReader.isEncrypted:
    print('Not an encrypted file')
    sys.exit()

#third, loop through and check every word until succeeded.

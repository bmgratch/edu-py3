#! python3
# brute-force.py is a brute force pdf-password checker.

import PyPDF2, sys
pwDict = 'dictionary.txt'
password = None

#get .pdf from command line
if len(sys.argv) == 2:
    pdfFile = sys.argv[1]
else:
    #some kind of error
    pass

# First load the dictionary of passwords
pwFile = open(pwDict)
passwords = pwFile.readlines()

# second, load the PDF
pdfReader = PyPDF2.PdfFileReader(open(pdfFile), rb)
if not pdfReader.isEncrypted:
    print('Not an encrypted file')
    sys.exit()

#third, loop through and check every word until succeeded.
for pw in passwords:
    if pdfReader.decrypt(pw.upper()) == 1:
        password = pw
        break
    if pdfReader.decrypt(pw.lower()) == 1:
        password = pw
        break
if password != None:
    print(password)

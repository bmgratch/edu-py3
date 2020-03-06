#! python3
# combinePdfs.py - combines all the PDFs in the current directory into
# an single PDF.

import PyPDF2, os

# get all PDF filenames
pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort(key=str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

# Loop through all the PDF files
for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    
    # Loop through all the pages (except first) and add them
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

# Save the resulting PDF file
pdfOutput = open('allMinutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()

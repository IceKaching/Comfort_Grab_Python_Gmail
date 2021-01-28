import ezgmail # for Gmail integration "pip install ezgmail"
import csv # for CSV writing
import os # for file operations
import re # for regular expressions
from pdfminer.high_level import extract_text # for PDF text extraction (pip install pdfminer.six)

# Go to directory that has GMAIL credentials.json and token.json and run init script: 

os.chdir(r'C:\tmp')
ezgmail.init()

# Search GMAIL for emails from CDG Taxi and then download all attachments:

resultThreads = ezgmail.search('from:noreply@cdgtaxi.com.sg', maxResults=250)

try:
        for i in range (0, 250):
                try:
                        for j in range (0, 4):
                                resultThreads[(i)].messages[(j)].downloadAllAttachments()
                except IndexError:
                        pass
except IndexError:
        pass

# Come up with a list of all the PDF files downloaded and then sort them:

pdfFiles = []
for filename in os.listdir(r'C:\tmp'):
    if filename.endswith('.pdf'):
                         pdfFiles.append(filename)
pdfFiles.sort(key = str.lower)

# Create a new CSV file, extract the text from all the PDF files and then remove all whitespace before writing into the new CSV file:

with open (r'C:\tmp\output14jan.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='|')
    for filename in pdfFiles:
        text = extract_text(filename)
        print(text) # not required but looks like something cool is happening.
#        newtext = str.split(text) #original way
        newtext = re.split(r'\s{2,}', text) #splits string when 2 or more spaces are detected - https://stackoverflow.com/questions/12866631/python-split-a-string-with-at-least-2-whitespaces
        writer.writerow(newtext)

# EOF

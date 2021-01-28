import ezgmail # for Gmail integration "pip install ezgmail"
import csv # for CSV writing
import os # for file operations
import re # for regular expressions

# Go to directory that has GMAIL credentials.json and token.json and run init script: 

os.chdir(r'C:\tmp')
ezgmail.init()

# Search GMAIL for emails from CDG Taxi and then download all attachments:

resultThreads = ezgmail.search('from:no-reply@grab.com subject:Your GRAB E-Receipt)', maxResults=300)
print('results found ' + str(len(resultThreads)))

with open (r'C:\tmp\output6.csv', 'w', newline='') as csvfile:
        try:
                for i in range (0, 300):
                        writer = csv.writer(csvfile, delimiter=',')
                        writer.writerow(resultThreads[(i)].messages)
                        print('row ' +str(i)+ ' done')
        except IndexError:
                pass

print('done')



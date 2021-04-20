import os
import csv

# Path to collect data from the Resources folder
poll_csv = os.path.join('..', 'Resources', 'election_data.csv')
# #02-Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv
   
# Read in the CSV file
with open(poll_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    print(header)
    


    
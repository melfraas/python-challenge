import os
import csv


# Path to collect data from the Resources folder
poll_csv = os.path.join('..', 'Resources', 'election_data.csv')
# #02-Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv





#   * The winner of the election based on popular vote.   

# Read in the CSV file
with open(poll_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    print(header)

#create empty lists to store values of each column
    CandName=[]
    County = []
    voterID = []
    
    #create empty lists to hold vote count for each candidate

    for row in csvreader:
#   * A complete list of candidates who received votes
        voterID.append(row[0])
        County.append(row[1])
        CandName.append(row[2])
    totalvotecount=len(voterID)
print(totalvotecount)

#print out list of individual candidate names by converting list to set
NameList = set(CandName)      
print(NameList)

#initialize vote counter for each candidate name

for name in NameList:
    votecount=0
    for cand in CandName:
        if name == cand:
            votecount+=1
    print(f'{name}: {votecount}')





#   * The total number of votes each candidate won
    
#   * The percentage of votes each candidate won

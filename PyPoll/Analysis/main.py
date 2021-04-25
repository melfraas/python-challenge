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
    #print(header)


    #create empty lists to store values of each column
    CandName=[]
    County = []
    voterID = []

    for row in csvreader:

        voterID.append(row[0])
        County.append(row[1])
        CandName.append(row[2])
    totalvotecount=len(voterID)
#print(totalvotecount)

#print out list of individual candidate names by converting list to set
NameList = set(CandName)

#initialize vote counter for each candidate name
#name is each unique candidate name
#cand in candlist is column to check against name list to find matches and add votes




print("Election Results: ")
print("---------------------------------------")
print(f'Candidates who received votes: {NameList}')
print(f'Total Votes: {totalvotecount}')
print('---------------------------------------')
resultlist = [] 
 

def VoteSummary():
    for name in NameList:
        votecount=0
        for cand in CandName:
            if name == cand:
                votecount+=1
                votepercent= round((votecount/totalvotecount)*100)
                resultlist.append(votepercent)

        print(f'{name}: {votecount} ({votepercent}%)')
        

    
VoteSummary()

# Specify the file to write to
output_path = os.path.join("..", "Analysis", "new.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')


    csvfile.write("Election Results: ")
    csvfile.write("---------------------------------------")
    csvfile.write(f'Candidates who received votes: {NameList}')
    csvfile.write(f'Total Votes: {totalvotecount}')
    csvfile.write('---------------------------------------')


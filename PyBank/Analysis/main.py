import os
import csv

# Path to collect data from the Resources folder
bankdata = os.path.join('..', 'Resources', 'budget_data.csv')

# Read in the CSV file
with open(bankdata, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    print(header)

    #create lists to hold column data
    Date=[]
    ProfitLosses=[]
    MonthlyChange = []
    
    for row in csvreader:
        Date.append(row[0])
        ProfitLosses.append(int(row[1]))
        for currentmonth in ProfitLosses:
            #start by subtracting first month from second month entry 
            currentmonth = 2 
            prevmonth = currentmonth-1
            change= currentmonth - prevmonth
            MonthlyChange.append(change)
            



    

#total number of months in the dataset
    monthCount= len(Date)
    print(monthCount)

    
  
    


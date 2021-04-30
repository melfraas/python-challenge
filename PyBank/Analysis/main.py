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
   
    # Initialize variables
    num_months = 0
    total_profit = 0
    sum_change = 0
    greatest_profit = 0
    greatest_loss = 0
    profit_month = 0
    loss_month = 0
    for row in csvreader:
        # Calculate number of months
        num_months += 1
        # Calculate total profit
        total_profit = total_profit+ int(row[1])
        # Calculate the change from previous month to this month
        if num_months == 1:
            # Remember first month profit/loss
            prev_month = int(row[1])
        else:
            # Calculate change from last month to this month
            change = int(row[1]) - prev_month
            # "Remember" previous month
            prev_month = int(row[1])
            # Keep cumulative sum of changes
            sum_change = sum_change + change
            # Calculate greatest profit/loss
            if change > greatest_profit:
                greatest_profit = change
                profit_month = row[0]
            elif change < greatest_loss:
                greatest_loss = change
                loss_month= row[0]
    average_change=round(sum_change/(num_months-1))
    
    print(f'The greatest loss is {greatest_loss} and occurred in {loss_month}') 
    print(f'The greatest profit is {greatest_profit} and occurred in {profit_month}') 
    print(f'The average change in profit is {average_change} per month')
  
# Save results to a txt file.
# Specify the file to write to
output_path = os.path.join("..", "Analysis", "new.txt")
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as txtfile:
    txtfile.write(f'The greatest loss is {greatest_loss} and occurred in {loss_month}' + ('')) 
    txtfile.write('')
    txtfile.write("---------------------------------------")
    txtfile.write(f'The greatest profit is {greatest_profit} and occurred in {profit_month}') 
    txtfile.write(' ')
    txtfile.write(f'The average change in profit is {average_change} per month')
    txtfile.write('________________________________________')   

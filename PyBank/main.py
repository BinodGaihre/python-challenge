import csv
import os
absolute_path = os.path.dirname(__file__) #path to the folder where your python file exsits
file_to_load = os.path.join(absolute_path,"Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join(absolute_path,"analysis", "budget_analysis.txt")  # Output file path
# Defining variables to track the financial data
output = {} # dictionary for the output
sum_change_total = 0 # sum of all the changes occured
greatest_increase = 0 
greatest_decrease = 0
# Opening the input csv file in read mode
with open(file_to_load, "r") as financial_data:
    reader = csv.reader(financial_data, delimiter=",")
     # Skip the header row
    header = next(reader)
    # Extract first row 
    first_row = next(reader)
    # assigning the total of profil/loss to a variable
    total_profit_loss = int(first_row[1])  
    #count of month for first row
    total_months = 1
    # Processing through each row of data
    for row in reader:
        #updating the number of months in the file
        total_months = total_months + 1 
        total_profit_loss = (total_profit_loss + int (row[1]))
        # tracking the change in profit/loss
        change_profit_loss = int(row[1]) - int(first_row[1]) 
        # changing the first in order to track next change in profit/loss
        first_row = row
        # updating the net change in profit/loss
        sum_change_total = sum_change_total + change_profit_loss
        # Calculate the greatest increase in profits (month and amount)
        if change_profit_loss>greatest_increase:
            #tracking the greatest increase to a variable based on the condition
            greatest_increase = change_profit_loss
            #racking the row with greatest increase
            greatest_inc = row
        # Calculate the greatest decrease in losses (month and amount)    
        elif change_profit_loss<greatest_decrease:
            greatest_decrease = change_profit_loss
            greatest_dec = row
        
# Calculating the average net change across the months
average ="${:.2f}".format((sum_change_total/(total_months-1)), 2) # subtracted one because change start from next month 
# Generating the output summary
print(f'Financial Analysis\n--------------------------')
#updating the output dictionary
output.update({"Total Months ":total_months, "Total ": "${}".format(total_profit_loss), "Average Change ": average})
for key,value in output.items():
    print(f'{key} : {value}')
print (f'Greatest Increase In Profits: {greatest_inc[0]} ({"${}".format(greatest_increase)})\nGreatest Decrease in Profits: {greatest_dec[0]} ({"${}".format(greatest_decrease)})')
# opening the output file in writing mode
with open(file_to_output, "w") as txt_file:
    txt_file.write(f'Financial Analysis\n--------------------------\n')
    output_writer = csv.writer(txt_file)
    for key, value in output.items():
        txt_file.write(f"{key}: {value}\n")
    txt_file.write(f'Greatest Increase In Profits: {greatest_inc[0]} ({"${}".format(greatest_increase)})\nGreatest Decrease in Profits: {greatest_dec[0]} ({"${}".format(greatest_decrease)})')

# PyBank Python Program written by Radha Mahlingam 2-28-19

# Import the libraries

import os
import csv

#Expected results
        #Financial Analysis
        #----------------------------
        #Total Months: 86
        #Total: $38382578
        #Average  Change: $-2315.12
        #Greatest Increase in Profits: Feb-2012 ($1926159)
        #Greatest Decrease in Profits: Sep-2013 ($-2196167)

# Path to collect data from the Resources folder

PybankCSV = os.path.join( 'Resources', 'budget_data.csv')

# Read in the CSV file
with open(PybankCSV, 'r') as csvfile:

    # Split the data on commas

    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip the header record

    header = next(csvreader)

    # Initialize the variables

    current_value = 0
    prior_value = 0
    total_value = 0
    count_mths = 0
    greatest_profit = 0
    greatest_loss = 0
    cur_difference = 0
    cum_difference = 0
    avg_changes = 0.0


    # Loop through the data
    for rec in csvreader:

        # The total number of months included in the dataset
        count_mths += 1
       
        # The net total amount of "Profit/Losses" over the entire period
        total_value += int(rec[1])
        current_value = int(rec[1])

        if count_mths==1:
           prior_value = int(rec[1])
           greatest_profit_dt = rec[0]
           greatest_profit = int(rec[1])
           greatest_loss_dt = rec[0]
           greatest_loss = int(rec[1])
        
        cur_difference = current_value - prior_value
        cum_difference += cur_difference

        # The greatest increase in profits (date and amount) over the entire period

        if cur_difference > greatest_profit:

            greatest_profit = cur_difference
            greatest_profit_dt = rec[0]

        # The greatest decrease in losses (date and amount) over the entire period

        elif cur_difference < greatest_loss:

             greatest_loss= cur_difference
             greatest_loss_dt = rec[0]

        prior_value = current_value

    # The average of the changes in "Profit/Losses" over the entire period

    avg_changes = cum_difference / (count_mths - 1)
    avg_changes = float("{:.2f}".format(avg_changes))

    print("\nFinancial Analysis") 
    print("------------------\n")
    print("Total Months: " + str(count_mths)+"\n")
    print("Total: $ " + str(total_value)+"\n")
    print("Average Change:  $ " + str(avg_changes)+"\n")
    print("Greatest increase in Profits:  " + str(greatest_profit_dt) + "  ($" + str(greatest_profit) + ")\n")
    print("Greatest decrease in Profits:  " + str(greatest_loss_dt) + "  ($" + str(greatest_loss) + ")\n")
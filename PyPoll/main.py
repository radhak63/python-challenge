# Pypoll Python Program written by Radha Mahlingam 2-28-19

# Import the libraries

import os
import csv

#This will both print the analysis to the terminal and export a text file with the results.

#This program will create a folder 'output' under the current working directory and 
#write the analysis to a file named 'Pypoll results.txt'

# As an example, this analysis will look similar to the one below:

#  Election Results
#  -------------------------
#  Total Votes: 3521001
#  -------------------------
#  Khan: 63.000% (2218231)
#  Correy: 20.000% (704200)
#  Li: 14.000% (492940)
#  O'Tooley: 3.000% (105630)
#  -------------------------
#  Winner: Khan
#  -------------------------

# Path to collect the election data from the 'Resources' folder

PypollCSV = os.path.join('Resources', 'election_data.csv')

# Read in the CSV file
with open(PypollCSV, 'r') as csvfile:

    # Split the data on commas

    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip the header record

    header = next(csvreader)

    # Initiaize the nested dictionary.  The first dict key will correspond to a unique candidate id
    # the nested dictionary will hold for each candidate, their name and total vote cast to them.

    Cand_dict = {1: {'name': '', 'vote cast': 0}}

    # Initialize the variables

    total_vote_cast = 0
    candidate_counter = 0
    winner_vote_cast=0

    # Loop through the data
    for rec in csvreader:
  
        if candidate_counter==0:
            candidate_counter += 1
            Cand_dict[candidate_counter]['name'] = rec[2]
            Cand_dict[candidate_counter]['vote cast'] = 0
          
        # The total number of votes cast in the election
        total_vote_cast += 1

        found=False
        for c_id, c_info in Cand_dict.items():
            if Cand_dict[c_id]['name']==rec[2]:
                Cand_dict[c_id]['vote cast'] += 1
                found=True

        if found==False:
            candidate_counter += 1
            Cand_dict[candidate_counter]={}
            Cand_dict[candidate_counter]['name'] = rec[2]
            Cand_dict[candidate_counter]['vote cast'] = 1

# printing the results and writing the results to a .txt file

# Creates an 'output' folder in the PWD, if it is not already existing

    path = "output"
    if not os.path.exists(path):
        os.makedirs(path)
    PypollTXT = os.path.join(path, 'Pypoll results.txt')

# Open the file using "write+" mode. This will create the file and write to it.

    with open(PypollTXT, 'w+') as f:
        line_to_print="\nElection Results\n"
        f.write(line_to_print)
        print(line_to_print) 
        line_to_print="--------------------------\n"
        f.write(line_to_print)
        print(line_to_print)
        line_to_print="Total Votes: "+ str(total_vote_cast)+"\n"
        f.write(line_to_print)
        print(line_to_print)
        line_to_print="--------------------------\n"
        f.write(line_to_print)
        print(line_to_print)

        for c_id, c_info in Cand_dict.items():

            # code to decide the winner of the election

            if (Cand_dict[c_id]['vote cast']> winner_vote_cast):
                candidate_counter=c_id
                winner_vote_cast = Cand_dict[c_id]['vote cast']

            #printing a line for each candidate with their name, % vote and total vote cast

            percentage_vote_cast=Cand_dict[c_id]['vote cast']/total_vote_cast
            line_to_print=Cand_dict[c_id]['name']+"    "+str("{0:.2%}".format(percentage_vote_cast))+"  ("+str(Cand_dict[c_id]['vote cast'])+")\n"
            f.write(line_to_print)
            print(line_to_print)

        #code to print the winner
        line_to_print="--------------------------\n"
        f.write(line_to_print)
        print(line_to_print)    
        line_to_print="Winner: "+Cand_dict[candidate_counter]['name']+"\n"
        f.write(line_to_print)
        print(line_to_print)
        line_to_print="--------------------------\n"
        f.write(line_to_print)
        print(line_to_print)    
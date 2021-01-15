# The data we need to retrieve.

import csv
import os
# Assign a variable for the file to load and the path.

file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# open the election results and read the file

with open(file_to_load) as election_data :

    # To do : read and analyze the data.
    file_reader = csv.reader(election_data) # file-reader is a variable pointing to election_data
    

    # Print the header row.
    headers = next(file_reader)
    print(headers)    
    first_row = next(file_reader)
    print(first_row)
    
# use 'with' statement to open an output file
with open(file_to_save,"w") as txt_file:
    # Write some data to the file.
    
    # Write three counties to the file.
    txt_file.write("Counties in the Election\n")
    txt_file.write("-------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")
    







#1. the total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentages of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote

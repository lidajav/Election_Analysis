# The data we need to retrieve.

import csv
import os
# Assign a variable for the file to load and the path.

file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Declare a new list 
candidate_options = []
candidate_votes={}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# open the election results and read the file
with open(file_to_load) as election_data :
    total_votes = 0 # Initial an accumulator to count votes
    # To do : read and analyze the data.
    file_reader = csv.reader(election_data) # file-reader is a variable pointing to election_data
    # Test

    # Read the header row.
    headers = next(file_reader)
   
    #1. the total number of votes cast
    for row in file_reader :
        total_votes += 1
        candidate_name= row[2]
       
        #2. A complete list of candidates who received votes
        
        if candidate_name not in candidate_options:
            # Add it to the list of candidates
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        
        #4. The total number of votes each candidate won
        candidate_votes[candidate_name] += 1
    
    #3. The percentages of votes each candidate won
    for candidate_name in candidate_votes: 
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        if (votes > winning_count) and (vote_percentage > winning_percentage) :
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
        

    #print out the winning candidate, vote count and percentage to terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
  
    print(f"The total votes are {total_votes}\n")

    

    




    
    

    











#5. The winner of the election based on popular vote

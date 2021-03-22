# The data we need to retrive.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources","election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis","election_analysis.txt")

# 1. Initialize a total vote counter
total_votes = 0

# Candidate Options
candidate_options = []

# Declare the empty Candidate Votes Dictionary
candidate_votes = {}

# Declrare string variable to record winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
        
    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count. 
        total_votes += 1

        # Print tha candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            
            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        
        candidate_votes[candidate_name] += 1

    for candidate_name in candidate_votes:
        # Retrive vote count of a candidate
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of the votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # print out each candidate's name, vote count, and percentage of votes to the terminal.       
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

        


# Using the open() function with the "w" mode we will write data to the file.
with open(file_to_save,'w') as txt_file:
    # Write some data to the file.
    txt_file.write("Counties in the Election\n------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")
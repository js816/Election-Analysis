# The data we need to retrieve:
# 1 - Total number of votes cast
# 2 - Complete list of candidates who received votes
# 3 - Total number of votes each candidate received
# 4 - Percentage of votes each candidate won
# 5 - Winner of the election based upon popular vote

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize total_votes
total_votes = 0

# Declaring candidate_options list
candidate_options = []

# Declaring candidates_votes dictionary
candidate_votes = {}

# Declaring winning_candidate, winning_count, and winning_percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:

        # Print the candidate name from each row
        candidate_name = row[2]

        # If candidate_name not in candidate_list, 
        if candidate_name not in candidate_options:

            # Add candidate_name to candidate_options list
            candidate_options.append(candidate_name)
            
            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Increment total votes by 1 for each vote
        total_votes += 1

        # Increment that candidate's votes by 1 for each vote
        candidate_votes[candidate_name] += 1
# Calculate the percentage of votes for each candidate by looping through the candidates_votes
# Iterate through the candidate list.
for candidate_name in candidate_votes:
        # Retrieve vote count of the candidate
        votes = candidate_votes[candidate_name]
        
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

        # Print the candidate name and percentage of votes.
        print(f"{candidate_name}:  {vote_percentage:.1f}% ({votes:,})\n")

        # Determine if the current vote count is greater than the winning_count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # if so, make winning_count equal to the current votes
            winning_count = votes
            winning_percentage = vote_percentage
            # Set the winning_candidate's name equal to the current candidate's name
            winning_candidate = candidate_name

# To do:  print out the winning candidate, vote count, and percentage to terminal
winning_candidate_summary = (
        f"----------------------\n"
        f"Winner:  {winning_candidate}\n"
        f"Winning Vote Count:  {winning_count:,}\n"
        f"Winning Percentage:  {winning_percentage:.1f}%\n"
        f"----------------------\n")
print(winning_candidate_summary)



# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")
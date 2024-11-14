# Importing necessary modules
import csv
import os
absolute_path = os.path.dirname(__file__) #path to the folder where your python file exsits
file_to_load = os.path.join(absolute_path,"Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join(absolute_path,"analysis", "election_analysis.txt")  # Output file path

# Initializing variables to track the election data
total_votes = 0  # Tracking the total number of votes cast
winner_count = 0    # Tracking the count of winner
# Defining lists and dictionaries to track candidate names and vote counts
candidate_name_list = [] 
candidate_vote_count_list = {}
# creating a set to add unique names in the data
seen_candidate = set() 

# Opening the CSV file and process it
with open(file_to_load, 'r', newline='', encoding='utf-8') as election_data:
    reader = csv.reader(election_data)
    # Skip the header row
    header = next(reader)
    # Loop through each row of the dataset and process it
    for row in reader:
        #updating the total votes cast 
        total_votes += 1 
        #Geting the candidate's name from the row
        candidate_name = row[2]
        # updating the candidate list if the name is not seen before
        if row[2] not in seen_candidate:
            candidate_name_list.append(row[2])
            seen_candidate.add(row[2])

        # Adding a vote to the candidate's count and updating the count of the individual candidate
        if candidate_name in candidate_vote_count_list:
            candidate_vote_count_list[candidate_name] += 1
        else:
            # initializing next candidate vote count to 1 in the vote count list 
            candidate_vote_count_list[candidate_name] = 1
print("Election Results \n----------------------")

print(f'Total Votes:{total_votes}')    
# Opening a text file to save the output
with open(file_to_output, "w") as txt_file:
    output_writer = csv.writer(txt_file)
    txt_file.write(f"Election Results\n")
    txt_file.write(f'--------------------\n')
    txt_file.write(f'Total Votes: {total_votes}\n')
    # In the dictionay candidate vote count list candidate name as key and count as value and looping through it
    for candidate_name, count in candidate_vote_count_list.items():
        percent = "${:.3f}".format((count/total_votes)*100)
        #finding out the candidate with highest vote counts
        if count > winner_count:
           winner_candidate = candidate_name
           winner_count = count
        print(f"{candidate_name}: {percent}% ({count})")
        txt_file.write(f'{candidate_name} : {percent}% ({count})\n')
    print(f'----------------------\n Winner : {winner_candidate}\n----------------------')
    txt_file.write(f'-----------------------\nWinner :{winner_candidate}\n-----------------------')
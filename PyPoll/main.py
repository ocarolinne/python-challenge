# Import dependencies
import os
import csv

#read_dir = 'PyPoll/Resources/'
#filename = 'election_data.csv'
#csv_path = os.path.join(read_dir, filename)

csv_path = r'PyPoll/Resources/election_data.csv'

# Declare variables and lists  

total_votes = 0
unique_candidate = []
current_candidate = ()
candidates_list = []
votes_candidates = {}
winner = ()

# Open File
 
with open(csv_path) as csv_file:
    #csv_reader = csv.DictReader(csv_file)   #// Read de file and interacted with the header
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csv_file)
  
 # Read the file, sum the total votes and create a list of candidates 
    for line in csv_reader:
        total_votes = total_votes + 1
        
        candidates_list.append(line[2])    
        
        current_candidate = (line[2])    
    
    # Use the candidate list to create a single data  dictionary containing candidate names and vote totals
        if current_candidate not in unique_candidate:      
            unique_candidate.append(current_candidate)
            votes_candidates[current_candidate] = 1    
        else:
            votes_candidates[current_candidate] += 1  
    
    # Calculate the percentage of votes        
    for candidate, votes in votes_candidates.items():
        percentage_votes = (votes / total_votes) * 100
    
        winner = max(votes_candidates, key=votes_candidates.get)
        
# Print the analysis to the terminal:
        
print("Election Results")   
print("-------------------------")        
print(f'Total Votes: {total_votes}')
print("-------------------------") 
for candidate, votes in votes_candidates.items():
        percentage_votes = (votes / total_votes) * 100
        winner = max(votes_candidates, key=votes_candidates.get)
        print(f"{candidate}: {percentage_votes:.3f}% % ({votes})")
print("-------------------------") 
print(f'Winner: {winner}')
print("-------------------------")  

#Export result to text file

txt_directory = "PyPoll/analysis"
txt_path = os.path.join(txt_directory, "election_analysis.txt")
os.makedirs(txt_directory, exist_ok=True)   

with open(txt_path, "w") as outfile:
    
    outfile.write("Election Results\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Votes: {total_votes}\n")
    outfile.write("----------------------------\n")
    for candidate, votes in votes_candidates.items():
        percentage_votes = (votes / total_votes) * 100
        winner = max(votes_candidates, key=votes_candidates.get)
        outfile.write(f"{candidate}: {percentage_votes:.3f}% % ({votes})\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Winner: {winner}\n")
    outfile.write("----------------------------\n") 

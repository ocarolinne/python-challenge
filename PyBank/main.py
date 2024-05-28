# Import dependencies
import os
import csv

#read_dir = 'PyBank/Resources/'
#filename = 'budget_data.csv'
#csv_path = os.path.join(read_dir, filename)

csv_path= r'PyBank/Resources/budget_data.csv'

# Open File

with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csv_file)
    
 # Declare variables and lists   
    changes_values = []
    profit = []  
    previous_value = 0
    budget_data = []

 # Read the file and create a numeric index to calculate differences between months  
    for index, line in enumerate(csv_reader):
       # Total months included in dataset
        budget_data.append(line)   
        
        # The profit information to calculate the total profit
        profit.append(int(line[1]))  
        
        # CCalculate changes in profit/loss over the entire period
        if index == 0: 
            previous_value = int(line[1]) 
        
        else:   
            changes_values.append(int(line[1])-previous_value)       
            previous_value = int(line[1])

 # # Calculate the sum of profits, the maximum and minimum value and the average profit variation                             
    total_profit = sum(profit)    
    max_change = max(changes_values)
    min_change = min(changes_values)
    mean_change = (sum(changes_values) / len(changes_values))   
    
    index_max_change = changes_values.index(max(changes_values))
    index_max_loss = changes_values.index(min(changes_values))
    data_max_change = budget_data[index_max_change][0]
    data_min_change = budget_data[index_max_loss][0]
 
    
# Print the analysis to the terminal:

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(budget_data)}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${mean_change:.2f}")
print(f"Greatest Increase in Profits: {data_max_change} (${max_change})")
print(f"Greatest Decrease in Profits: {data_min_change} (${min_change})")   

#Export result to text file

txt_directory = "PyBank/analysis"
txt_path = os.path.join(txt_directory, "budget_analysis.txt")
os.makedirs(txt_directory, exist_ok=True)

with open(txt_path, "w") as outfile:
    
    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months: {len(budget_data)}\n")
    outfile.write(f"Total: ${total_profit}\n")
    outfile.write(f"Average Change: ${mean_change:.2f}\n")
    outfile.write(f"Greatest Increase in Profits: {data_max_change} (${max_change})\n")
    outfile.write(f"Greatest Decrease in Profits: {data_min_change} (${min_change})\n")  
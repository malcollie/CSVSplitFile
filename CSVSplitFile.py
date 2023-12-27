import csv
import os

def split_csv(input_file, output_prefix, max_entries_per_file=99):
    with open(input_file, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        
        file_number = 1
        current_entries = 0
        output_file = f"{output_prefix}{file_number}.csv"
        
        with open(output_file, 'w', newline='', encoding='utf-8') as output_csv:
            writer = csv.writer(output_csv)
            writer.writerow(header)
            
            for row in reader:
                writer.writerow(row)
                current_entries += 1
                
                if current_entries == max_entries_per_file:
                    current_entries = 0
                    file_number += 1
                    output_file = f"{output_prefix}{file_number}.csv"
                    
                    with open(output_file, 'w', newline='', encoding='utf-8') as new_output_csv:
                        writer = csv.writer(new_output_csv)
                        writer.writerow(header)

# Example usage
input_csv_file = 'your_input_file.csv'
output_file_prefix = 'output'
split_csv(input_csv_file, output_file_prefix)
import csv
import os

def split_csv(input_file, output_prefix, max_entries_per_file=99):
    with open(input_file, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        
        file_number = 1
        current_entries = 0

        while True:
            output_file = f"{output_prefix}{file_number}.csv"
            
            with open(output_file, 'w', newline='', encoding='utf-8') as output_csv:
                writer = csv.writer(output_csv)
                writer.writerow(header)
                
                for _ in range(max_entries_per_file):
                    try:
                        row = next(reader)
                        writer.writerow(row)
                        current_entries += 1
                    except StopIteration:
                        # End of file reached
                        break

                if current_entries == 0:
                    # No more entries, break the loop
                    break

                file_number += 1

# Example usage
input_csv_file = 'path/to/your/input_file.csv'
output_file_prefix = 'output'
split_csv(input_csv_file, output_file_prefix)

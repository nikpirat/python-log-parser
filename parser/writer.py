from config import CSV_FIELDS
import csv
import os

def write_to_csv(log_entries, output_file):
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=CSV_FIELDS)
        writer.writeheader()
        for entry in log_entries:
            writer.writerow(entry)
# Objective: This code checks the CSV files contained in the "csv_directory" path, analyzes the "ID" column,
# and for each value in this column, it creates a new CSV file in the "output_directory" folder with only the data of the analyzed "ID",
# already removing those that are UNDEFINED, those with yield less than or equal to zero, and the condditions indicated in line 45.
# Step 1

import csv
import os

# Set the directory where your CSV files are located
csv_directory = r" "
# Set the directory where you want to save the filtered CSV files
output_directory = r" "

# Set the condition column
condition_column = "ID"

# Dictionary to hold filtered rows for each unique value in the condition column
filtered_data = {}

# Loop through each CSV file in the directory
for filename in os.listdir(csv_directory):
    if filename.endswith(".csv"):
        filepath = os.path.join(csv_directory, filename)

        # Open the CSV file and read its contents
        with open(filepath, "r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")

            # Check if the condition column exists in the CSV file
            if condition_column not in reader.fieldnames:
                print(f"Column '{condition_column}' not found in '{filename}'")
                continue

            # Iterate through rows and collect data for each unique value in the condition column
            for row in reader:
                value = row[condition_column]
                area = float(row["area"])
                maquina = row["maquina"]
                # Exclude rows where the value is "*NAO_DEFINIDO*" or area is not greater than 0
                if value != "*NAO_DEFINIDO*" and area > 0 and maquina not in (
                '1', '2', '3', '4', '5', '6', '7', '8'):

                    if value not in filtered_data:
                        filtered_data[value] = []
                    filtered_data[value].append(row)

# Write filtered data to separate CSV files for each unique value in the condition column
for value, rows in filtered_data.items():
    output_file = os.path.join(output_directory, f"{value}.csv")  # Set output file path with value as filename
    with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = rows[0].keys() if rows else []
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")

        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    print(f"Filtered data for value '{value}' saved to '{output_file}'")
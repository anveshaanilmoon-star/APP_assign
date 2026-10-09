import csv
import json

input_file = input("Enter CSV file name: ")
output_file = input("Enter JSON file name: ")

try:
    data = []

    with open(input_file, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            data.append(row)

    with open(output_file, "w") as file:
        json.dump(data, file, indent=4)

    print("CSV data converted to JSON successfully.")

except FileNotFoundError:
    print("Error: CSV file not found.")

except Exception as e:
    print("Error:", e)
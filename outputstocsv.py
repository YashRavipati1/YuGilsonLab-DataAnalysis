import csv
import re
import os

input_directory = "/Users/yashravipati/Downloads/VinaOutputs/"
output_file = "output.csv"


with open(output_file, "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["File", "Result"])

    for filename in os.listdir(input_directory):
        file_path = os.path.join(input_directory, filename)
        if(filename == ".DS_Store"):
            continue

        with open(file_path, "r") as file:
            print(file_path)
            text = file.read()

            # Use regular expressions to extract the desired value
            match = re.search(r"REMARK VINA RESULT:\s+(-?\d+\.\d+)", text)
            if match:
                result = match.group(1)
            else:
                result = "N/A"

            writer.writerow([filename, result])
# with open(input_file, "r") as file, open(output_file, "w", newline="") as csv_file:
#     text = file.read()
#     match = re.search(r"REMARK VINA RESULT:\s+(-?\d+\.\d+)", text)
#     if match:
#         result = match.group(1)
#     else:
#         result = "N/A"

#     data = [result]
#     writer = csv.writer(csv_file)
#     writer.writerow(data)
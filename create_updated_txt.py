import os
import csv

# Define the directory containing the folders
TARGET_DIR = "./resemble"

# Define the input CSV file
INPUT_CSV = "440ead1e-dd9b-4d68-be23-6ebb9289159f.csv"

# Read the CSV file
with open(INPUT_CSV, mode='r', newline='') as file:
    reader = csv.DictReader(file)
    
    # Iterate over each row in the CSV
    for row in reader:
        tag_name = row['Tag Name']
        update_transcript = row['Updated Transcript']
        
        # Construct the path to the folder
        folder_path = os.path.join(TARGET_DIR, tag_name)
        
        # Check if the folder exists
        if os.path.exists(folder_path):
            # Construct the path to the updated.txt file
            updated_txt_path = os.path.join(folder_path, 'updated.txt')
            
            # Append the UpdateTranscript to updated.txt
            with open(updated_txt_path, mode='a') as updated_file:
                updated_file.write(update_transcript + "\n")
        else:
            print(f"Folder for tag '{tag_name}' does not exist.")
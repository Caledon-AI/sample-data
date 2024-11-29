import os

# Define the directory containing the folders
TARGET_DIR = "./resemble"

# Iterate over each directory in the target directory
for dir_name in os.listdir(TARGET_DIR):
    dir_path = os.path.join(TARGET_DIR, dir_name)
    
    # Ensure it's a directory
    if os.path.isdir(dir_path):
        original_txt_path = os.path.join(dir_path, 'original.txt')
        updated_txt_path = os.path.join(dir_path, 'updated.txt')
        new_original_txt_path = os.path.join(dir_path, 'new_original.txt')
        
        # Read the precursor content from original.txt
        precursor_content = ""
        if os.path.exists(original_txt_path):
            with open(original_txt_path, 'r') as original_file:
                line = original_file.readline()
                precursor_content = line.split('~~')[0].strip()
        
        # Read the content from updated.txt
        updated_content = ""
        if os.path.exists(updated_txt_path):
            with open(updated_txt_path, 'r') as updated_file:
                updated_content = updated_file.read().strip()
        
        # Combine the contents and write to new_original.txt
        combined_content = f"{precursor_content}~~{updated_content}"
        with open(new_original_txt_path, 'w') as new_original_file:
            new_original_file.write(combined_content)
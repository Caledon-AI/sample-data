import os

# Define the directory containing the folders and the index file
TARGET_DIR = "./resemble"
INDEX_FILE = "index.txt"
NEW_INDEX_FILE = "new_index.txt"

# Read the order of tags from index.txt
with open(INDEX_FILE, 'r') as index_file:
    # Extract the tag name from each line (substring before the first '~')
    tags_order = [line.split('~')[0].strip() for line in index_file.readlines()]

# Prepare to write to new_index.txt
with open(NEW_INDEX_FILE, 'w') as new_index_file:
    # Iterate over each tag in the order specified by index.txt
    for tag in tags_order:
        # Construct the path to the new_original.txt file
        new_original_txt_path = os.path.join(TARGET_DIR, tag, 'new_original.txt')
        
        # Debug: Print the path being checked
        print(f"Checking path: {new_original_txt_path}")
        
        # Check if the new_original.txt file exists
        if os.path.exists(new_original_txt_path):
            # Read the content of new_original.txt
            with open(new_original_txt_path, 'r') as new_original_file:
                content = new_original_file.read().strip()
            
            # Debug: Print the content being written
            print(f"Writing content for tag '{tag}': {content[:50]}...")  # Print first 50 chars for brevity
            
            # Write the content to new_index.txt
            new_index_file.write(content + "\n")
        else:
            print(f"new_original.txt not found for tag '{tag}'")
import json

# Read the JSON file
with open('new_data.json', 'r') as f:
    data = json.load(f)

# Write to JSONL file
with open('output.jsonl', 'w') as f:
    for item in data:
        json_line = json.dumps(item)
        f.write(json_line + '\n') 
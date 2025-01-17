import csv
import json

def csv_to_jsonl(input_csv, output_jsonl):
    with open(input_csv, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        
        with open(output_jsonl, 'w', encoding='utf-8') as jsonl_file:
            for row in reader:
                # Create the JSON structure
                entry = {
                    "company": row['Company'].strip().upper(),
                    "question_type": row['Question Type'].strip(),
                    "question": row['Question'].strip(),
                    "answer": row['Answer'].strip(),
                    "justification": row['Justification'].strip(),
                    "evidence": []  # Empty evidence list
                }
                
                # Write the JSON object as a line
                jsonl_file.write(json.dumps(entry, ensure_ascii=False) + '\n')

if __name__ == "__main__":
    input_file = "10K_Questions_2.csv"
    output_file = "10K_QUESTIONS_2.jsonl"
    csv_to_jsonl(input_file, output_file)
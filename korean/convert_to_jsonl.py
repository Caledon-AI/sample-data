import csv
import json

def csv_to_jsonl(input_csv, output_jsonl):
    with open(input_csv, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        
        with open(output_jsonl, 'w', encoding='utf-8') as jsonl_file:
            for row in reader:
                # Create evidence objects
                evidence_pages = [
                    {
                        "source": "/files/SAMSUNG_2023_4Q_Interim_Business_Report_vF_kr.pdf",
                        "page_number": int(page.strip()),
                        "full_page_text": ""
                    }
                    for page in row['Evidence Page Number'].split(',')
                    if page.strip()
                ]

                # Create the JSON structure
                entry = {
                    "company": row['Company Name'].strip().upper(),
                    "question_type": row['Question Type'].strip(),
                    "question_kr": row['Question Korean Translated'].strip(),
                    "question_en": row['Question'].strip(),
                    "answer_kr": row['Answer in Korean'].strip(),
                    "evidence": evidence_pages
                }
                
                # Write the JSON object as a line
                jsonl_file.write(json.dumps(entry, ensure_ascii=False) + '\n')

if __name__ == "__main__":
    input_file = "KR_SAMSUNG_QA.csv"
    output_file = "KR_SAMSUNG_QA.jsonl"
    csv_to_jsonl(input_file, output_file)
import json
import PyPDF2
import os

def extract_page_text(pdf_path, page_number):
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            # Page number in PDF reader is 0-based and we need to add 1 to the page number in evidence
            # since the page in footer is 1 less than actual page
            actual_page = page_number  # The page number already accounts for the offset
            if actual_page <= len(pdf_reader.pages):
                page = pdf_reader.pages[actual_page - 1]
                return page.extract_text()
            else:
                return ""
    except Exception as e:
        print(f"Error extracting text from {pdf_path} page {page_number}: {str(e)}")
        return ""

def process_json():
    # Read the input JSON
    with open('data.json', 'r') as file:
        data = json.load(file)

    # Process each question
    for question in data:
        if 'evidence' in question:
            for evidence in question['evidence']:
                if 'source' in evidence and 'page_number' in evidence:
                    pdf_path = os.path.join('10-K Filings', f"{evidence['source']}.pdf")
                    if os.path.exists(pdf_path):
                        page_text = extract_page_text(pdf_path, evidence['page_number'])
                        evidence['full_page_text'] = page_text
                    else:
                        print(f"PDF file not found: {pdf_path}")

    # Write the updated JSON
    with open('new_data.json', 'w') as file:
        json.dump(data, file, indent=2)

if __name__ == "__main__":
    process_json()
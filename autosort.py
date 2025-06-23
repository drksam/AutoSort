import os
import time
import shutil
import glob
import yaml
from datetime import datetime
import PyPDF2
from difflib import SequenceMatcher

# Load configuration
def load_config(path='config.yaml'):
    with open(path, 'r') as f:
        return yaml.safe_load(f)

def log(message, log_file):
    with open(log_file, 'a') as f:
        f.write(f"{datetime.now()} - {message}\n")

def extract_pdf_text(pdf_path):
    try:
        with open(pdf_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            text = ''
            for page in reader.pages:
                text += page.extract_text() or ''
            return text
    except Exception as e:
        return ''

# Compare PDF files (placeholder for actual comparison logic)
def compare_pdfs(new_pdf, directories):
    new_text = extract_pdf_text(new_pdf)
    best_dir = None
    best_score = 0
    for d in directories:
        pdfs = glob.glob(os.path.join(d, '*.pdf'))
        for pdf in pdfs:
            existing_text = extract_pdf_text(pdf)
            score = SequenceMatcher(None, new_text, existing_text).ratio()
            if score > best_score:
                best_score = score
                best_dir = d
    # If no match found, default to first directory
    return best_dir if best_dir else directories[0]

def rename_and_move(file_path, target_dir, log_file):
    base_dir = os.path.basename(target_dir)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    new_name = f"{base_dir}_{timestamp}.pdf"
    new_path = os.path.join(target_dir, new_name)
    shutil.move(file_path, new_path)
    log(f"Moved and renamed {file_path} to {new_path}", log_file)

def monitor():
    config = load_config()
    watch_dir = config['watch_directory']
    directories = config['directories']
    log_file = config.get('log_file', 'buildlog.md')
    processed = set()
    log("Starting AutoSort monitor", log_file)
    while True:
        pdfs = glob.glob(os.path.join(watch_dir, '*.pdf'))
        for pdf in pdfs:
            if pdf not in processed:
                try:
                    target_dir = compare_pdfs(pdf, directories)
                    rename_and_move(pdf, target_dir, log_file)
                    processed.add(pdf)
                except Exception as e:
                    log(f"Error processing {pdf}: {e}", log_file)
        time.sleep(5)

if __name__ == '__main__':
    monitor()

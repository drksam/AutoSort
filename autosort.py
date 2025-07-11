import os
import time
import shutil
import glob
import yaml
from datetime import datetime
import PyPDF2
from difflib import SequenceMatcher
import sys

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

def extract_top_half_first_page(pdf_path):
    try:
        with open(pdf_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            if not reader.pages:
                return ''
            page = reader.pages[0]
            text = page.extract_text() or ''
            lines = text.splitlines()
            half = max(1, len(lines) // 2)
            return '\n'.join(lines[:half])
    except Exception as e:
        return ''

def directory_name_in_text(text, directories):
    text_lower = text.lower()
    for d in directories:
        dir_name = os.path.basename(d).lower()
        if dir_name in text_lower:
            return d
    return None

def ensure_unknown_dir_exists(directories):
    unknown_dir = None
    for d in directories:
        if os.path.basename(d).lower() == 'unknown':
            unknown_dir = d
            break
    if not unknown_dir:
        unknown_dir = os.path.join(os.path.dirname(directories[0]), 'unknown')
        os.makedirs(unknown_dir, exist_ok=True)
        directories.append(unknown_dir)
    return unknown_dir

def build_index(directories):
    index = {}
    for d in directories:
        pdfs = glob.glob(os.path.join(d, '*.pdf'))
        index[d] = []
        for pdf in pdfs:
            top_half = extract_top_half_first_page(pdf)
            full_text = extract_pdf_text(pdf)
            index[d].append({'file': pdf, 'top_half': top_half, 'full_text': full_text})
    return index

# Compare PDF files (placeholder for actual comparison logic)
def compare_pdfs(new_pdf, directories):
    # Step 1: Extract top half of first page
    print_step("Step 1: Extracting top half of first page", os.path.basename(new_pdf))
    top_half = extract_top_half_first_page(new_pdf)
    # Step 2: Check for directory name in text
    print_step("Step 2: Checking for directory name in text", os.path.basename(new_pdf))
    dir_found = directory_name_in_text(top_half, directories)
    if dir_found:
        print_step("Directory name found in text, selecting directory", os.path.basename(new_pdf), dir_found)
        return dir_found
    # Step 3: Build index (top half and full text)
    print_step("Step 3: Building index for directories", os.path.basename(new_pdf))
    index = build_index(directories)
    # Step 4: Compare top half to index top halves
    print_step("Step 4: Comparing top half to index", os.path.basename(new_pdf))
    best_dir = None
    best_score = 0.0
    for d, files in index.items():
        for entry in files:
            score = SequenceMatcher(None, top_half, entry['top_half']).ratio()
            if score > best_score:
                best_score = score
                best_dir = d
    if best_score > 0.8:
        print_step("Top half match found", os.path.basename(new_pdf), best_dir)
        return best_dir
    # Step 5: Full file search if still unclear
    print_step("Step 5: Full file search", os.path.basename(new_pdf))
    new_full = extract_pdf_text(new_pdf)
    best_dir = None
    best_score = 0.0
    for d, files in index.items():
        for entry in files:
            score = SequenceMatcher(None, new_full, entry['full_text']).ratio()
            if score > best_score:
                best_score = score
                best_dir = d
    if best_score > 0.8:
        print_step("Full file match found", os.path.basename(new_pdf), best_dir)
        return best_dir
    # Step 6: Unknown folder
    print_step("Step 6: No match found, moving to unknown folder", os.path.basename(new_pdf))
    unknown_dir = ensure_unknown_dir_exists(directories)
    return unknown_dir

def rename_and_move(file_path, target_dir, log_file):
    base_dir = os.path.basename(target_dir)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    new_name = f"{base_dir}_{timestamp}.pdf"
    new_path = os.path.join(target_dir, new_name)
    shutil.move(file_path, new_path)
    log(f"Moved and renamed {file_path} to {new_path}", log_file)

def print_progress(current, total, filename):
    bar_length = 40
    filled_length = int(bar_length * current // total) if total else 0
    bar = '█' * filled_length + '-' * (bar_length - filled_length)
    print(f'Processing: |{bar}| {current}/{total} files - {filename}', end='\r', flush=True)

def print_step(step, filename=None, directory=None):
    msg = f"[STEP] {step}"
    if filename:
        msg += f" | File: {filename}"
    if directory:
        msg += f" | Directory: {directory}"
    print(msg, flush=True)

def get_directories_and_index(parent_dir):
    dirs = [os.path.join(parent_dir, d) for d in os.listdir(parent_dir)
            if os.path.isdir(os.path.join(parent_dir, d))]
    print("Directories found for indexing:")
    for d in dirs:
        print(f" - {d}")
    return dirs

def monitor():
    config = load_config()
    watch_dir = config['watch_directory']
    # Get parent directory from config or infer from first directory
    parent_dir = config.get('parent_directory')
    if not parent_dir:
        # Infer from first directory in list if not set
        if 'directories' in config and config['directories']:
            parent_dir = os.path.dirname(config['directories'][0])
        else:
            print("No parent directory or directories specified in config.")
            return
    directories = get_directories_and_index(parent_dir)
    log_file = config.get('log_file', 'buildlog.md')
    processed = set()
    log("Starting AutoSort monitor", log_file)
    while True:
        pdfs = glob.glob(os.path.join(watch_dir, '*.pdf'))
        unprocessed_pdfs = [pdf for pdf in pdfs if pdf not in processed]
        total = len(unprocessed_pdfs)
        for idx, pdf in enumerate(unprocessed_pdfs, 1):
            try:
                print_step("Extracting text", os.path.basename(pdf))
                print_progress(idx, total, os.path.basename(pdf))
                print_step("Comparing to directories", os.path.basename(pdf))
                target_dir = compare_pdfs(pdf, directories)
                print_step("Moving file", os.path.basename(pdf), target_dir)
                rename_and_move(pdf, target_dir, log_file)
                print_step("Done", os.path.basename(pdf), target_dir)
                processed.add(pdf)
            except Exception as e:
                log(f"Error processing {pdf}: {e}", log_file)
        if total:
            print()  # Newline after progress bar
        time.sleep(5)

if __name__ == '__main__':
    monitor()

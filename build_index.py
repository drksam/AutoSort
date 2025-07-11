import os
import glob
import yaml
import PyPDF2
import json

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

def build_and_save_index(parent_dir, index_dir):
    index = {}
    for d in os.listdir(parent_dir):
        dir_path = os.path.join(parent_dir, d)
        if os.path.isdir(dir_path) and d.lower() != 'unknown':
            pdfs = glob.glob(os.path.join(dir_path, '*.pdf'))
            index[d] = []
            for pdf in pdfs:
                top_half = extract_top_half_first_page(pdf)
                full_text = extract_pdf_text(pdf)
                index[d].append({'file': os.path.basename(pdf), 'top_half': top_half, 'full_text': full_text})
            # Save per-directory index
            with open(os.path.join(index_dir, f'{d}_index.json'), 'w', encoding='utf-8') as f:
                json.dump(index[d], f, ensure_ascii=False, indent=2)
    # Save master index
    with open(os.path.join(index_dir, 'master_index.json'), 'w', encoding='utf-8') as f:
        json.dump(index, f, ensure_ascii=False, indent=2)
    print(f"Index built and saved to {index_dir}")

if __name__ == '__main__':
    with open('config.yaml', 'r') as f:
        config = yaml.safe_load(f)
    parent_dir = config.get('parent_directory')
    index_dir = os.path.join(os.path.dirname(__file__), 'index')
    os.makedirs(index_dir, exist_ok=True)
    build_and_save_index(parent_dir, index_dir)

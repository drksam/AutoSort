# AutoSort

## Overview
AutoSort is an intelligent Windows application that monitors a directory for new PDF scans, automatically analyzes their content, and sorts them into appropriate directories based on text recognition and fuzzy matching. The app features a smart multi-step sorting process with manual override capabilities and persistent indexing for improved performance.

## Features
- **Smart Text Recognition**: Extracts and analyzes full text from PDFs using PyPDF2
- **Fuzzy Directory Matching**: Handles OCR errors and misspellings in document text
- **Persistent Indexing**: Builds and maintains index files for faster subsequent processing
- **Manual Override GUI**: Interactive popup for manual folder selection when automatic sorting fails
- **Automatic File Renaming**: Files are renamed as "DIR_DATE_TIME.pdf" format
- **Comprehensive Logging**: Detailed progress and error logging
- **Background Monitoring**: Continuously monitors watch directory for new files

## Quick Install
Download and run the installer from: https://github.com/drksam/AutoSort/releases

## Manual Setup
1. Install Python 3.8+ from https://www.python.org/
2. Install required packages:
   ```powershell
   pip install -r requirements.txt
   ```
3. Edit `config.yaml` to set your watch directory and parent directory containing target folders.
4. Run initial indexing:
   ```powershell
   python build_index.py
   ```
5. You can also use `run_autosort.bat` to launch the app easily on Windows.

## How It Works
AutoSort uses a sophisticated 7-step process to classify and sort PDFs:

1. **Text Extraction**: Extracts full text from all pages of the PDF
2. **Directory Name Detection**: Uses fuzzy matching to find directory names in the document text
3. **Index Loading**: Loads pre-built index files containing text from existing PDFs
4. **Index Comparison**: Compares new PDF text to indexed files with similarity scoring
5. **Fallback Full Search**: Direct comparison to all files if index search fails
6. **Manual GUI Selection**: Interactive popup for user decision when automatic methods fail
7. **Final Placement**: Moves to selected directory or unknown folder

## Usage
Run the app with:
```powershell
python autosort.py
```

Or use the debug version for detailed output:
```powershell
python autosortdebug.py
```

## Configuration
Edit `config.yaml`:
```yaml
# Directory to monitor for new PDF scans
watch_directory: C:/path/to/watch/folder

# Parent directory containing all target folders
parent_directory: C:/path/to/sorted/folders

# Logging file
log_file: log.md
```

## Indexing
- Run `python build_index.py` to create initial index files
- Index files are automatically updated when new files are sorted
- Index files are stored in the `index` directory for shared access

## Logging
Progress and errors are logged in the configured log file (default: `log.md`).

## Advanced Features
- **Fuzzy Matching**: Handles OCR errors like "vwoRKsHoP" matching "WorkShop"
- **Similarity Scoring**: Uses 80% threshold for automatic classification
- **Error Recovery**: Robust error handling for corrupted or unreadable PDFs
- **Performance Monitoring**: Shows extraction times and similarity scores in debug mode

## Creating Standalone Executable
```powershell
pip install pyinstaller
pyinstaller --onefile --windowed autosort.py
```
The executable will be in the `dist` folder.

## Troubleshooting
- Ensure all directories exist and are writable
- Check log file for error messages
- Use debug version (`autosortdebug.py`) for detailed output
- Verify PDF files are not corrupted or password-protected
- Run `build_index.py` if index files are missing or outdated

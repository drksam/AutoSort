# AutoSort

## Overview
AutoSort is a Windows app that monitors a directory for new PDF scans, compares them to files in a set of directories, decides the correct directory, renames the file as "DIR_DATE_TIME.pdf", and moves it to the chosen directory. All configuration is done via `config.yaml`.

## Setup
1. Install Python 3.8+ from https://www.python.org/
2. Install required packages:
   ```powershell
   pip install pyyaml PyPDF2
   ```
3. Edit `config.yaml` to set your watch directory and target directories.
4. (Optional) To run without installing Python, use a tool like PyInstaller to create an executable:
   ```powershell
   pip install pyinstaller
   pyinstaller --onefile autosort.py
   ```
   The executable will be in the `dist` folder.
5. You can also use `run_autosort.bat` to launch the app easily on Windows.

## Usage
Run the app with:
```powershell
python autosort.py
```

## Logging
Progress and errors are logged in `buildlog.md`.

## Customization
- To improve PDF comparison, edit the `compare_pdfs` function in `autosort.py`.
- No formal UI; all settings are in `config.yaml`.

## Troubleshooting
- Ensure all directories exist and are writable.
- Check `buildlog.md` for error messages.

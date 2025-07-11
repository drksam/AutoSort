# AutoSort Installation Guide

## Quick Install (Recommended)

### Option 1: Batch Installer
1. Download `installer.bat` from https://github.com/drksam/AutoSort
2. Right-click and "Run as administrator" 
3. Follow the prompts

### Option 2: PowerShell Installer  
1. Download `installer.ps1` from https://github.com/drksam/AutoSort
2. Right-click and "Run with PowerShell"
3. If prompted about execution policy, type `Y` and press Enter
4. Follow the prompts

## Manual Installation

### Prerequisites
- Windows 10/11
- Python 3.8 or higher
- Internet connection for initial setup

### Steps
1. **Install Python**
   - Download from https://www.python.org/
   - **Important**: Check "Add Python to PATH" during installation

2. **Download AutoSort**
   - Clone or download from https://github.com/drksam/AutoSort
   - Extract to desired location (e.g., `C:\AutoSort`)

3. **Install Dependencies**
   ```cmd
   cd C:\AutoSort
   pip install -r requirements.txt
   ```

4. **Configure**
   - Edit `config.yaml` to set your directories
   - Run `python build_index.py` for initial indexing

5. **Create Shortcut (Optional)**
   - Right-click desktop > New > Shortcut
   - Target: `python.exe "C:\AutoSort\autosort.py"`
   - Name: "AutoSort"

## Default Directory Structure

The installer creates these directories:
```
C:\AutoSort_Watch\          # Place new PDFs here
C:\AutoSort_Sorted\         # Sorted PDFs go here
├── Documents\
├── Invoices\
└── Reports\
```

## First Run

1. **Start AutoSort**
   - Double-click desktop icon, or
   - Run `run_autosort.bat`, or 
   - Command: `python autosort.py`

2. **Test the System**
   - Place a PDF file in `C:\AutoSort_Watch\`
   - AutoSort will process and move it to the appropriate folder
   - Check `log.md` for processing details

## Troubleshooting

### "Python not found"
- Reinstall Python with "Add to PATH" checked
- Or add Python manually to PATH environment variable

### "Permission denied" 
- Run installer as administrator
- Check folder permissions

### "Module not found"
- Run: `pip install -r requirements.txt`
- Ensure you're in the AutoSort directory

### PDFs not processing
- Check `log.md` for error messages
- Verify directories exist and are writable
- Try debug mode: `python autosortdebug.py`

## Advanced Configuration

### Custom Directories
Edit `config.yaml`:
```yaml
watch_directory: D:/Scans
parent_directory: D:/Sorted_Documents
```

### Performance Tuning
- Larger directories may process slower
- Run `build_index.py` periodically to refresh indexes
- Use debug mode to monitor processing times

## Getting Help

- Check `readme.md` for detailed documentation
- Review `log.md` for error messages  
- Visit https://github.com/drksam/AutoSort for updates
- Report issues on GitHub Issues page

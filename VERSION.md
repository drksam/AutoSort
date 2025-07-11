# AutoSort Version Information

**Version:** 2.0.0  
**Release Date:** July 11, 2025  
**Repository:** https://github.com/drksam/AutoSort

## Features in This Version

### Core Functionality
- ✅ Intelligent PDF text extraction and analysis
- ✅ Multi-step sorting process with fallback options
- ✅ Fuzzy directory name matching (handles OCR errors)
- ✅ Persistent indexing system for improved performance
- ✅ Manual GUI override for uncertain classifications
- ✅ Automatic file renaming (DIR_DATE_TIME format)
- ✅ Comprehensive logging and error handling

### New in v2.0.0
- ✅ Manual folder selection GUI popup
- ✅ Persistent index files saved to disk
- ✅ Fuzzy matching for misspelled directory names
- ✅ Enhanced error handling and recovery
- ✅ Detailed debugging and progress feedback
- ✅ Automated installer packages
- ✅ Full documentation and setup guides

### Technical Improvements
- ✅ Removed half-page extraction (now uses full text only)
- ✅ Optimized index loading and saving
- ✅ Better GUI integration with tkinter
- ✅ Improved file path handling
- ✅ Enhanced similarity scoring algorithms
- ✅ Robust PDF processing with error recovery

## File Structure
```
AutoSort/
├── autosort.py              # Main application
├── autosortdebug.py         # Debug version with detailed output
├── build_index.py           # Index builder utility
├── config.yaml              # Configuration file
├── requirements.txt         # Python dependencies
├── installer.bat            # Windows batch installer
├── installer.ps1            # PowerShell installer
├── run_autosort.bat         # Launch script
├── run_autosort_debug.bat   # Debug launch script
├── readme.md                # Main documentation
├── INSTALL.md               # Installation guide
├── VERSION.md               # This file
└── index/                   # Index files directory
    ├── Documents_index.json
    ├── Invoices_index.json
    └── ...
```

## Dependencies
- Python 3.8+
- pyyaml >= 6.0
- PyPDF2 >= 3.0.0
- tkinter (included with Python)

## Supported Platforms
- Windows 10/11
- Windows Server 2019/2022

## Known Issues
- None currently reported

## Planned Features (Future Versions)
- OCR support for image-based PDFs
- Web interface for remote management
- Multiple file format support
- Advanced machine learning classification
- Network folder monitoring
- Email notifications

## Changelog

### v2.0.0 (July 11, 2025)
- Added manual GUI folder selection
- Implemented persistent indexing system
- Added fuzzy directory name matching
- Enhanced error handling and logging
- Created automated installer packages
- Comprehensive documentation update
- Removed half-page processing for consistency

### v1.0.0 (June 23, 2025)
- Initial release
- Basic PDF processing and sorting
- Simple text matching
- Configuration file support
- Basic logging functionality

# Build Log for AutoSort

## 2025-06-23
- Project initialized.
- Created config.yaml for configuration.
- Implemented basic monitoring, renaming, and moving logic in autosort.py.
- Added placeholder for PDF comparison logic.
- Created initial readme.md with setup and usage instructions.

## Next Steps
- Implement actual PDF comparison logic.
- Add error handling improvements.
- Test with real directories and PDF files.
2025-06-23 13:34:54.878514 - Starting AutoSort monitor
2025-06-23 13:36:25.093029 - Moved and renamed C:/test\232518tri.pdf to S:/Amazon\Amazon_20250623_133624.pdf
- Implemented actual PDF comparison logic using PyPDF2 and difflib.
  - Now compares text content of new PDF to existing PDFs in each directory and selects the best match.
2025-06-23 13:41:45.024769 - Starting AutoSort monitor
2025-06-23 13:42:00.398296 - Moved and renamed C:/test\Image_028.pdf to S:/Holston\Holston_20250623_134200.pdf
2025-06-23 13:44:46.581093 - Starting AutoSort monitor
2025-06-23 13:45:08.563854 - Moved and renamed C:/test\Image_028.pdf to S:/WorkOrders\WorkOrders_20250623_134508.pdf
2025-06-23 13:53:44.671616 - Moved and renamed C:/test\Image_010.pdf to S:/Holston\Holston_20250623_135344.pdf
2025-06-23 13:56:25.428258 - Moved and renamed C:/test\k.pdf to S:/WorkOrders\WorkOrders_20250623_135625.pdf
2025-06-23 13:57:32.072193 - Moved and renamed C:/test\Image_002.pdf to S:/Holston\Holston_20250623_135731.pdf

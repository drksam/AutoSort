@echo off
title AutoSort - PDF Document Sorter
echo Starting AutoSort...
echo.
echo AutoSort is now monitoring for PDF files.
echo To stop, close this window or press Ctrl+C
echo.
python autosort.py
if %errorlevel% neq 0 (
    echo.
    echo AutoSort encountered an error.
    echo Check the log file for details.
    echo.
)
pause

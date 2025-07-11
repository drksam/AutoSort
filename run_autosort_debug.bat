@echo off
title AutoSort Debug Mode
echo Starting AutoSort in Debug Mode...
echo.
echo This will show detailed processing information.
echo To stop, close this window or press Ctrl+C
echo.
python autosortdebug.py
if %errorlevel% neq 0 (
    echo.
    echo AutoSort encountered an error.
    echo Check the log file for details.
    echo.
)
pause

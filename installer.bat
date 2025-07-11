@echo off
title AutoSort Installer
color 0A

echo ===============================================
echo             AutoSort Installer
echo ===============================================
echo.
echo This installer will:
echo - Download AutoSort from GitHub
echo - Install Python dependencies
echo - Create desktop shortcut
echo - Set up initial configuration
echo.
pause

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org/
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

echo Python found. Continuing installation...
echo.

:: Create AutoSort directory
set INSTALL_DIR=%USERPROFILE%\AutoSort
if not exist "%INSTALL_DIR%" mkdir "%INSTALL_DIR%"
cd /d "%INSTALL_DIR%"

:: Download from GitHub
echo Downloading AutoSort from GitHub...
if exist autosort.py del autosort.py
if exist config.yaml del config.yaml

:: Use PowerShell to download files
powershell -Command "& {Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/drksam/AutoSort/main/autosort.py' -OutFile 'autosort.py'}"
powershell -Command "& {Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/drksam/AutoSort/main/config.yaml' -OutFile 'config.yaml'}"
powershell -Command "& {Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/drksam/AutoSort/main/requirements.txt' -OutFile 'requirements.txt'}"
powershell -Command "& {Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/drksam/AutoSort/main/build_index.py' -OutFile 'build_index.py'}"
powershell -Command "& {Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/drksam/AutoSort/main/readme.md' -OutFile 'readme.md'}"

if not exist autosort.py (
    echo ERROR: Failed to download AutoSort files
    echo Please check your internet connection and try again
    pause
    exit /b 1
)

echo Download complete!
echo.

:: Install Python dependencies
echo Installing Python dependencies...
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo Dependencies installed successfully!
echo.

:: Create desktop shortcut
echo Creating desktop shortcut...
set DESKTOP=%USERPROFILE%\Desktop
set SHORTCUT=%DESKTOP%\AutoSort.lnk

:: Create VBS script to create shortcut
echo Set oWS = WScript.CreateObject("WScript.Shell") > CreateShortcut.vbs
echo sLinkFile = "%SHORTCUT%" >> CreateShortcut.vbs
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> CreateShortcut.vbs
echo oLink.TargetPath = "python.exe" >> CreateShortcut.vbs
echo oLink.Arguments = """%INSTALL_DIR%\autosort.py""" >> CreateShortcut.vbs
echo oLink.WorkingDirectory = "%INSTALL_DIR%" >> CreateShortcut.vbs
echo oLink.IconLocation = "python.exe,0" >> CreateShortcut.vbs
echo oLink.Description = "AutoSort - Intelligent PDF Sorter" >> CreateShortcut.vbs
echo oLink.Save >> CreateShortcut.vbs

cscript CreateShortcut.vbs >nul
del CreateShortcut.vbs

echo Desktop shortcut created!
echo.

:: Create initial directories
echo Setting up initial configuration...
if not exist "C:\AutoSort_Watch" mkdir "C:\AutoSort_Watch"
if not exist "C:\AutoSort_Sorted" mkdir "C:\AutoSort_Sorted"
if not exist "C:\AutoSort_Sorted\Documents" mkdir "C:\AutoSort_Sorted\Documents"
if not exist "C:\AutoSort_Sorted\Invoices" mkdir "C:\AutoSort_Sorted\Invoices"
if not exist "C:\AutoSort_Sorted\Reports" mkdir "C:\AutoSort_Sorted\Reports"

:: Update config file with default paths
echo # AutoSort Configuration > config.yaml
echo. >> config.yaml
echo # Directory to monitor for new PDF scans >> config.yaml
echo watch_directory: C:/AutoSort_Watch >> config.yaml
echo. >> config.yaml
echo # Parent directory containing all target folders >> config.yaml
echo parent_directory: C:/AutoSort_Sorted >> config.yaml
echo. >> config.yaml
echo # Logging file >> config.yaml
echo log_file: log.md >> config.yaml

echo.
echo ===============================================
echo         Installation Complete!
echo ===============================================
echo.
echo AutoSort has been installed to: %INSTALL_DIR%
echo.
echo Default directories created:
echo - Watch folder: C:\AutoSort_Watch
echo - Sorted folders: C:\AutoSort_Sorted
echo.
echo To get started:
echo 1. Double-click the AutoSort icon on your desktop
echo 2. Or edit config.yaml to set custom directories
echo 3. Place PDF files in the watch folder
echo.
echo For help, see readme.md in the installation folder
echo.
pause

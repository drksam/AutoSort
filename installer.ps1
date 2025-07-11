# AutoSort PowerShell Installer
# Run with: powershell -ExecutionPolicy Bypass -File installer.ps1

Write-Host "===============================================" -ForegroundColor Green
Write-Host "             AutoSort Installer" -ForegroundColor Green
Write-Host "===============================================" -ForegroundColor Green
Write-Host ""
Write-Host "This installer will:" -ForegroundColor Yellow
Write-Host "- Download AutoSort from GitHub" -ForegroundColor Yellow
Write-Host "- Install Python dependencies" -ForegroundColor Yellow
Write-Host "- Create desktop shortcut" -ForegroundColor Yellow
Write-Host "- Set up initial configuration" -ForegroundColor Yellow
Write-Host ""
Read-Host "Press Enter to continue or Ctrl+C to cancel"

# Check if Python is installed
try {
    $pythonVersion = python --version 2>&1
    Write-Host "Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "ERROR: Python is not installed or not in PATH" -ForegroundColor Red
    Write-Host "Please install Python 3.8+ from https://www.python.org/" -ForegroundColor Yellow
    Write-Host "Make sure to check 'Add Python to PATH' during installation" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

# Create AutoSort directory
$installDir = "$env:USERPROFILE\AutoSort"
if (!(Test-Path $installDir)) {
    New-Item -ItemType Directory -Path $installDir | Out-Null
}
Set-Location $installDir

Write-Host "Downloading AutoSort from GitHub..." -ForegroundColor Cyan

# Download files from GitHub
$files = @(
    "autosort.py",
    "config.yaml", 
    "requirements.txt",
    "build_index.py",
    "readme.md"
)

foreach ($file in $files) {
    try {
        $url = "https://raw.githubusercontent.com/drksam/AutoSort/main/$file"
        Invoke-WebRequest -Uri $url -OutFile $file -ErrorAction Stop
        Write-Host "Downloaded: $file" -ForegroundColor Green
    } catch {
        Write-Host "ERROR: Failed to download $file" -ForegroundColor Red
        Write-Host "Please check your internet connection and try again" -ForegroundColor Yellow
        Read-Host "Press Enter to exit"
        exit 1
    }
}

Write-Host "Download complete!" -ForegroundColor Green
Write-Host ""

# Install Python dependencies
Write-Host "Installing Python dependencies..." -ForegroundColor Cyan
try {
    & python -m pip install --upgrade pip
    & python -m pip install -r requirements.txt
    Write-Host "Dependencies installed successfully!" -ForegroundColor Green
} catch {
    Write-Host "ERROR: Failed to install dependencies" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host ""

# Create desktop shortcut
Write-Host "Creating desktop shortcut..." -ForegroundColor Cyan
$desktop = [Environment]::GetFolderPath("Desktop")
$shortcutPath = "$desktop\AutoSort.lnk"

$WshShell = New-Object -comObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut($shortcutPath)
$Shortcut.TargetPath = "python.exe"
$Shortcut.Arguments = "`"$installDir\autosort.py`""
$Shortcut.WorkingDirectory = $installDir
$Shortcut.IconLocation = "python.exe,0"
$Shortcut.Description = "AutoSort - Intelligent PDF Sorter"
$Shortcut.Save()

Write-Host "Desktop shortcut created!" -ForegroundColor Green
Write-Host ""

# Create initial directories
Write-Host "Setting up initial configuration..." -ForegroundColor Cyan
$watchDir = "C:\AutoSort_Watch"
$sortedDir = "C:\AutoSort_Sorted"

$directories = @(
    $watchDir,
    $sortedDir,
    "$sortedDir\Documents",
    "$sortedDir\Invoices", 
    "$sortedDir\Reports"
)

foreach ($dir in $directories) {
    if (!(Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir | Out-Null
        Write-Host "Created: $dir" -ForegroundColor Green
    }
}

# Update config file
$configContent = @"
# AutoSort Configuration

# Directory to monitor for new PDF scans
watch_directory: C:/AutoSort_Watch

# Parent directory containing all target folders
parent_directory: C:/AutoSort_Sorted

# Logging file
log_file: log.md
"@

$configContent | Out-File -FilePath "config.yaml" -Encoding UTF8

Write-Host ""
Write-Host "===============================================" -ForegroundColor Green
Write-Host "         Installation Complete!" -ForegroundColor Green
Write-Host "===============================================" -ForegroundColor Green
Write-Host ""
Write-Host "AutoSort has been installed to: $installDir" -ForegroundColor Cyan
Write-Host ""
Write-Host "Default directories created:" -ForegroundColor Yellow
Write-Host "- Watch folder: $watchDir" -ForegroundColor Yellow
Write-Host "- Sorted folders: $sortedDir" -ForegroundColor Yellow
Write-Host ""
Write-Host "To get started:" -ForegroundColor White
Write-Host "1. Double-click the AutoSort icon on your desktop" -ForegroundColor White
Write-Host "2. Or edit config.yaml to set custom directories" -ForegroundColor White
Write-Host "3. Place PDF files in the watch folder" -ForegroundColor White
Write-Host ""
Write-Host "For help, see readme.md in the installation folder" -ForegroundColor White
Write-Host ""
Read-Host "Press Enter to exit"

@echo off
SETLOCAL ENABLEDELAYEDEXPANSION
@REM Check for administrator privileges
net session >nul 2>&1
if errorlevel 1 (
    echo This script must be run as an administrator.
    echo Please 
    echo #1. right-click the .bat file 
    echo #2. select "Run as administrator".
    echo.
    echo.
    pause
    exit /b
)
@REM Define ANSI color codes
@REM    echo %RED%This text is red.%RESET%
@REM    echo %YELLOW%This text is yellow.%RESET%
@REM    echo %GREEN%This text is green.%RESET%
set "RED=[31m"
set "YELLOW=[33m"
set "GREEN=[32m"
set "RESET=[0m"
@REM ============================================================
@REM Script Name: init_git.bat
@REM Description: This script checks if Git and Git Bash for 
@REM              Windows is installed and installs it if not.
@REM Usage: Run this script from an elevated command prompt.
@REM Author: Jaehoon Song
@REM Date: 2024-09-15
@REM ============================================================

@REM ============================================================
@REM :Start
@REM ============================================================
:Start
@REM Define the URL and local filename
set "url=https://github.com/git-for-windows/git/releases/download/v2.46.0.windows.1/Git-2.46.0-64-bit.exe"
set "filename=%~dp0Git-2.46.0-64-bit.exe"
set "logfile=%~dp0install.log"
set "searchString=Installation process succeeded"

@REM Check if Git Bash is installed
@REM echo Current Directory: %CD%
@REM echo Script Directory: %~dp0
@REM pause
echo "Checking if Git Bash is installed..."
git --version >nul 2>&1
if %ERRORLEVEL% == 0 (
    echo %YELLOW%Git Bash is already installed.%RESET%
    echo ------------------------------
    where git && git --version
    echo ------------------------------
    goto End
)

@REM Download the installer
echo Git Bash is %RED%not installed%RESET%. Downloading Git Bash...
echo %YELLOW%Press Enter to continue...%RESET%
powershell -Command "Invoke-WebRequest -Uri %url% -OutFile %filename%"
if %ERRORLEVEL% neq 0 (
    echo %RED%Failed to download the installer.%RESET%
    goto End
)

@REM Install Git Bash
echo Installing Git Bash...
start /wait %filename% /VERYSILENT /NORESTART /LOG="%logfile%"
if %ERRORLEVEL% neq 0 (
    echo %RED%Installation failed.%RESET%
    goto End
)

echo Git Bash %GREEN%installed successfully%RESET%.

@REM Check if the log file exists after installation
if not exist "%logfile%" (
    echo %RED%Error: The log file "%logfile%" does not exist.%RESET%
    goto End
)

@REM Check for success or error status in the log file
powershell -Command "if (Select-String -Path '%logfile%' -Pattern '%searchString%') { exit 0 } else { exit 1 }"
if %ERRORLEVEL% equ 0 (
    echo %YELLOW%Installation session has been successfully finished.%RESET%
    echo %YELLOW%Run the script again, so you can activate bash on your system settings.%RESET%
) else (
    echo %RED%Installation Failed. Check the error status in %logfile% file.%RESET%
)

@REM ============================================================
@REM :End
@REM ============================================================
:End
@REM Clean up installer and log file
del /f /q "%filename%" >nul 2>&1
del /f /q "%logfile%" >nul 2>&1
@REM /f: Forces deletion of read-only files.
@REM /q: Quiet mode, suppresses confirmation prompts.
@REM >nul: Redirects standard output (success messages) to nul (discard output).
@REM 2>&1: Redirects error messages (stderr) to the same place as standard output (also nul), ensuring no error messages appear.

pause
exit /b

endlocal
@REM ======================================================================
@REM Labels in Batch Scripting
@REM ======================================================================
@REM
@REM Labels to mark specific points so it can "jump" to the points 
@REM using the `goto` command. Unlike more advanced programming languages, 
@REM batch scripting only allows jumping forward to labels located later 
@REM in the script. Also, They are not functions so there is no "return"
@REM 
@REM :EOF
@REM The 'EOF' label is a special label that signifies the end of the file.
@REM It is used to denote that the script has reached its end, and the
@REM execution will exit at this point.
@REM ======================================================================

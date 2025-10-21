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
@REM ============================================================
@REM Script Name: init_perl.bat
@REM Description: This script checks if Strawberry Perl is 
@REM              installed and installs it if not.
@REM Usage: Run this script from an elevated command prompt.
@REM Author: Jaehoon Song
@REM Date: 2024-09-10
@REM ============================================================

@REM ============================================================
@REM :Start
@REM ============================================================
:Start
@REM Define ANSI color codes
set "RED=[31m"
set "YELLOW=[33m"
set "RESET=[0m"
@REM Define the URL and local filename
set "url=https://strawberryperl.com/download/5.32.1.1/strawberry-perl-5.32.1.1-64bit.msi"
set "filename=strawberry-perl-5.32.1.1-64bit.msi"
set "logfile=%CD%\install.log"
set "searchString=success or error status: 0"

@REM Check if Perl is installed
echo Checking if Perl is installed...
perl -v >nul 2>&1
if %ERRORLEVEL% == 0 (
    echo %YELLOW%Perl is already installed.%RESET%
    echo ------------------------------
    where perl && perl -v
    echo ------------------------------
    where perldoc && perldoc -V
    echo ------------------------------
    where cpan && cpan -v
    echo ------------------------------
    call pause
    goto End
)

@REM Download the MSI file
echo Perl is not installed. Downloading Strawberry Perl...
powershell -Command "Invoke-WebRequest -Uri %url% -OutFile %filename%"
if %ERRORLEVEL% neq 0 (
    echo Failed to download the MSI file.
    call pause
    goto End
)

@REM Install the MSI file
echo Installing Strawberry Perl...
msiexec /i %filename% /quiet /norestart /log install.log
if %ERRORLEVEL% neq 0 (
    echo Installation failed.
    del /f %filename%
    call pause
    goto End
)

del /f %filename%
echo Strawberry Perl installed successfully.

@REM Check if the log file after installation
if not exist "%logfile%" (
    echo Error: The log file "%logfile%" does not exist.
    call pause
    goto End
)

@REM Check for success or error status in the log file
powershell -Command "if (Select-String -Path '%logfile%' -Pattern '%searchString%') { exit 0 } else { exit 1 }"
if %ERRORLEVEL% equ 0 (
    echo Installation Succeeded.
    del "%logfile%"
) else (
    echo Installation Failed. Check the error status in %logfile% file.
)

@REM ============================================================
@REM :End
@REM ============================================================
:End
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
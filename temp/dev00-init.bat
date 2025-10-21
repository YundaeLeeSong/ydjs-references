@echo off
@REM ============================================================
@REM Script Name: win01-start.bat
@REM Description: This script automates the following tasks:
@REM              1. Opens multiple URLs in the default web browser.
@REM              2. Checks for the existence of specific directories:
@REM                 - Creates them if they do not exist.
@REM                 - Opens them in File Explorer.
@REM Usage: Run this script from the command line. Ensure that the 
@REM        script is not run from a directory named "repo".
@REM Author: Jaehoon Song
@REM Date: 2024-12-03
@REM ============================================================
SETLOCAL ENABLEDELAYEDEXPANSION



@REM ============================================================
@REM Pre-script
@REM ============================================================
@REM @param
@REM ANSI coloring
@REM Usage:
@REM    TEST_FAIL (RED)     : echo %TEST_FAIL%texttexttext%RESET%
@REM    TEST_PASS (GREEN)   : echo %TEST_PASS%texttexttext%RESET%
@REM    USRPROMPT (YELLOW)  : echo %USRPROMPT%texttexttext%RESET%
@REM    DEBUG_SYS (BLUE)    : echo %DEBUG_SYS%texttexttext%RESET%
@REM    DEBUG_USR (CYAN)    : echo %DEBUG_USR%texttexttext%RESET%
set "RESET=[0m"
set "TEST_FAIL=[31m"
set "TEST_PASS=[32m"
set "USRPROMPT=[33m"
set "DEBUG_SYS=[34m"
set "DEBUG_USR=[36m"
@REM @param
@REM Script Metadata References
@REM Data Example:
@REM    SCRIPT_FULLPATH (e.g., "C:\path\to\script.bat")
@REM    SCRIPT_FILENAME (e.g., "script")
@REM    SCRIPT_NAMENEXT (e.g., "script.bat")
@REM    SCRIPT_DIR_PATH (e.g., "C:\path\to\")
set SCRIPT_FULLPATH=%0
set SCRIPT_FILENAME=%~n0
set SCRIPT_NAMENEXT=%~nx0
set SCRIPT_DIR_PATH=%~dp0
@REM @REM @exception
@REM @REM    return if in "\repo"
@REM set CURR_DIR=%SCRIPT_DIR_PATH:~0,-1%
@REM set CURR_DIR=%CURR_DIR:~-5%
@REM if "%CURR_DIR%"=="\repo" (
@REM     echo %DEBUG_SYS%Move this %SCRIPT_NAMENEXT% on your desktop.%RESET%
@REM     pause
@REM     exit /b 1
@REM )
@REM @REM @exception
@REM @REM    return if not admin privilege
@REM net session >nul 2>&1
@REM if errorlevel 1 (
@REM     echo This script must be run as an administrator.
@REM     echo Please 
@REM     echo #1. right-click the .bat file 
@REM     echo #2. select "Run as administrator".
@REM     echo.
@REM     echo.
@REM     pause
@REM     exit /b
@REM ) else (
@REM     echo Welcome!You are running in %TEST_PASS%administrator mode%RESET%.
@REM     pause
@REM )
























@REM Define URLs to open (space-separated list, split across multiple lines for readability)
set urls=^
https://www.youtube.com ^
https://chat.openai.com ^
https://www.google.com

@REM Define directories to check and open (space-separated list, split across multiple lines for readability)
set dirs=^
%LocalAppData% ^
%LocalAppData%\Temp ^
%UserProfile%\AppData\LocalLow ^
%UserProfile%

@REM File I/O Path Rule: %UserProfile%\AppData\LocalLow\AuthorName\ProjectName






@REM ===================== Batch Script for Multi-Task Automation =====================
@REM This script performs the following tasks:
@REM 1. Opens multiple URLs in the default web browser.
@REM 2. Checks for the existence of specific directories:
@REM    - Creates them if they do not exist.
@REM    - Opens them in File Explorer.
@REM 3. Uses simulated multi-line arrays for URLs and directories.
@REM ================================================================================


@REM ===================== Start of Task Execution =====================
:Start
echo Starting tasks...
echo.
@REM --------------------- Task 1: Open URLs ---------------------
echo Opening URLs...
for %%U in (%urls%) do (
    echo Opening %%U...
    start "" "%%U"
)
echo.
@REM ----------------- Task 2: Check and Manage Directories -----------------
echo Checking directories...
for %%D in (%dirs%) do (
    if exist "%%D" (
        echo The directory "%%D" already exists.
    ) else (
        echo The directory "%%D" does not exist. Creating it now...
        mkdir "%%D"
        echo The directory "%%D" has been created.
    )
    start explorer "%%D"
)
goto End
@REM ===================== End of Task Execution =====================
:End
echo.
echo All tasks completed. Exiting script...
pause
exit 0

endlocal
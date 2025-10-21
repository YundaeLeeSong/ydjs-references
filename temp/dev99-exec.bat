@echo off
SETLOCAL ENABLEDELAYEDEXPANSION
@REM ============================================================
@REM Script Name: {script_filename.extension}.bat
@REM Description: This script executes different types of scripts
@REM              based on the file extension of the batch file.
@REM              Supported extensions: .pl (Perl), .sh (Bash), 
@REM              .bat (Batch).
@REM Usage: Run this script from the command line.
@REM Author: Jaehoon Song
@REM Date: 2024-12-03
@REM ============================================================










@REM Define ANSI color codes
@REM    echo %RED%This text is red.%RESET%
@REM    echo %YELLOW%This text is yellow.%RESET%
@REM    echo %GREEN%This text is green.%RESET%
set "RED=[31m"
set "YELLOW=[33m"
set "GREEN=[32m"
set "RESET=[0m"


@REM Find the path to git.exe
for /f "delims=" %%G in ('where git') do set "GIT_CMD_PATH=%%G"
@REM Navigate to the parent directory of git.exe and then the bin folder
set "GIT_PARENT_PATH=!GIT_CMD_PATH!\..\..\bin"
for %%G in ("!GIT_PARENT_PATH!") do set "GIT_BIN_PATH=%%~fG"
@REM Check if bash.exe exists in the bin folder
if exist "!GIT_BIN_PATH!\bash.exe" (
    echo !YELLOW!bash.exe found in !GIT_BIN_PATH!.!RESET!
    REM Add Git bin path to the PATH for the current session
    set "PATH=!PATH!;!GIT_BIN_PATH!"
    echo ------------------------------
    where bash
    echo ------------------------------
) else (
    echo "!GIT_BIN_PATH!"
    echo !RED!bash.exe not found. Something is wrong.!RESET!
    goto End
)







@REM ============================================================
@REM :Start
@REM ============================================================
:Start












@REM Extract script filename and extension
set "scriptFilename=%~n0"
for %%f in ("%scriptFilename%") do set "scriptExtension=%%~xf"
set "scriptExtension=%scriptExtension:~1%"

echo.
echo %GREEN%Script Details%RESET%
echo -----------------------------
echo Script Filename: %scriptFilename%
echo Script Extension: %scriptExtension%
echo -----------------------------
echo.






@REM Determine the command to run based on file extension
if "%scriptExtension%"=="pl" goto RunPerl
if "%scriptExtension%"=="sh" goto RunBash
if "%scriptExtension%"=="bat" goto RunBat

@REM If file extension is not recognized
echo %YELLOW%Error: Unknown file type '%scriptExtension%' detected.%RESET%
echo Please ensure your file has a supported extension and is in the correct directory.
echo %YELLOW%Rename this script file with the script filename with the following extensions supported.%RESET%
echo %YELLOW%i.e. [test.sh].bat, [test.bat].bat, [test.pl].bat%RESET%
echo Here are the supported file types:
echo    - .pl  : Runs Perl scripts
echo    - .sh  : Runs Bash scripts
echo    - .bat : Runs Batch scripts
pause
goto End

@REM ============================================================
@REM :RunPerl
@REM ============================================================
:RunPerl
echo.
echo Running Perl script: %scriptFilename%.pl
if exist "%scriptFilename%" (
    start "" perl "%scriptFilename%"
) else (
    echo %YELLOW%Error: The Perl script '%scriptFilename%.pl' does not exist.%RESET%
    echo Please ensure the file is located in the current directory.
    echo Use the 'dir' command to list files or move the file here.
    pause
)
goto End
@REM ============================================================
@REM :RunBash
@REM ============================================================
:RunBash
echo.
echo Opening a new window to run Bash script: %scriptFilename%.sh
if exist "%scriptFilename%" (
    start "" bash "%scriptFilename%"
) else (
    echo %YELLOW%Error: The Bash script '%scriptFilename%.sh' does not exist.%RESET%
    echo Instructions:
    echo    1. Verify the file exists in the current directory.
    echo    2. Ensure Bash is installed and accessible from the command line.
    echo    3. Use 'bash --version' to check if Bash is set up correctly.
    pause
)
goto End
@REM ============================================================
@REM :RunBat
@REM ============================================================
:RunBat
echo.
echo Opening a new window to run Batch file: %scriptFilename%.bat
if exist "%scriptFilename%" (
    start "" cmd /c "%scriptFilename%"
) else (
    echo %YELLOW%Error: The Batch file '%scriptFilename%.bat' does not exist.%RESET%
    echo Please verify the file is in the current directory and try again.
    pause
)
goto End
@REM ============================================================
@REM :End
@REM ============================================================
:End
goto EOF

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
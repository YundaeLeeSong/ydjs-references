#!/bin/bash
BASHRC_PATH="$HOME/.bashrc" # Check if .bashrc exists, create if missing
if [[ -f "$BASHRC_PATH" ]]; then
    echo ".bashrc exists at: $BASHRC_PATH."
else
    echo ".bashrc not found. Creating a new one at: $BASHRC_PATH."
    cat <<EOL > "$BASHRC_PATH"
# ~/.bashrc
# Add your custom configurations here.

EOL
fi

TITLE="~./bashrc"
CONFIG="General configuration for '${TITLE}'" # configuration title
MARKER="?GENERAL;" # Check if the configuration script exists in ~/.bashrc
SCRIPT=$(cat <<'EOF'



: '
Here-Document (Heredoc): A heredoc allows you to redirect a block of 
text to a command. 

    << <delimiter> 

tells the shell to read the following lines into the input for the colon command until it 
encounters the closing delimiter, delimiters can be just strings.

Colon (:) Command: it is a shell built-in that does nothing with exit status (0). 

    : <any_literals> 

Its often used as a no-op (no operation) or placeholder.
'

################################################################################
#                                   ?GENERAL;
################################################################################
# Current project folder's name
PROJ_NAME="$(basename "$PWD")"
PROJ_DIR="$PWD"
PROJ_SRC="$PWD/src"
PROJ_EXT="$PWD/ext"
# ANSI escape codes: font coloring
BLACK_RG='\033[0;30m'
RED_RG='\033[0;31m'
GREEN_RG='\033[0;32m'
MINT_GREEN_RG='\033[38;5;48m'
LIME_GREEN_RG='\033[38;5;154m'
YELLOW_RG='\033[0;33m'
BLUE_RG='\033[0;34m'
PURPLE_RG='\033[0;35m'
CYAN_RG='\033[0;36m'
WHITE_RG='\033[0;37m'
##########################
EOC='\033[0m' # End Of Coloring
#################################< VERSION >####################################
# Script metadata
SCRIPT_VERSION="2.1.3"
SCRIPT_AUTHOR="Jaehoon Song"
echo -e "${GREEN_RG}# Bash Configuration Version: ${SCRIPT_VERSION}${EOC}"
echo -e "${MINT_GREEN_RG}# Author: ${SCRIPT_AUTHOR}${EOC}"
echo -e "${CYAN_RG}############### SYSTEM & USER INFORMATION ###############${EOC}"
echo -e "HOME directory: ${LIME_GREEN_RG}$HOME${EOC}"
echo -e "Current directory: ${LIME_GREEN_RG}$PWD${EOC}"
echo -e "OS Kernel Type: ${LIME_GREEN_RG}$(uname -s)${EOC}"
echo -e "OS Kernel Version: ${LIME_GREEN_RG}$(uname -r)${EOC}"
echo -e "Architecture: ${LIME_GREEN_RG}$(uname -m)${EOC}"
echo -e "Hostname: ${LIME_GREEN_RG}$(hostname)${EOC}"
echo -e "Logged-in User: ${LIME_GREEN_RG}$(whoami)${EOC}"
echo -e "Shell Type: ${LIME_GREEN_RG}$SHELL${EOC}"
echo -e "Shell Version: ${LIME_GREEN_RG}$BASH_VERSION${EOC}"
# User-specific environment variables
echo -e "${CYAN_RG}################# ENVIRONMENT VARIABLES #################${EOC}"
echo -e "PATH Directories:"
IFS=':' read -ra PATH_ARRAY <<< "$PATH"  # Split PATH into an array by ':'
for dir in "${PATH_ARRAY[@]}"; do
    echo -e "  ${LIME_GREEN_RG}$dir${EOC}"
done
echo -e "${CYAN_RG}############### PROJECT INFORMATION ###############${EOC}"
echo -e "Project Name: ${LIME_GREEN_RG}$PROJ_NAME${EOC}"
echo -e "Project Directory: ${LIME_GREEN_RG}$PROJ_DIR${EOC}"
echo -e "Project Source Code Directory: ${LIME_GREEN_RG}$PROJ_SRC${EOC}"
echo -e "Project External Directory: ${LIME_GREEN_RG}$PROJ_EXT${EOC}"
echo -e "${CYAN_RG}#########################################################${EOC}"
echo -e "\n\n"
##################################< USAGE >#####################################
# echo "Pass: $(TEST_PASS 'All tests passed successfully!')."
# echo "Error: $(TEST_FAIL 'aaaa')."
# echo "Notice: $(USRPROMPT 'Prompt: Do the following actions')."
# echo "Debug: $(DEBUG_USR 'User-level debug: Input parameters are valid')."
# echo "Debug: $(DEBUG_SYS 'System-level debug: Memory allocation successful')."
###############################################################################
function TEST_PASS {
    local text=$1
    echo -e "${GREEN_RG}${text}${EOC}"
}
function TEST_FAIL {
    local text=$1
    echo -e "${RED_RG}${text}${EOC}"
}
function USRPROMPT {
    local text=$1
    echo -e "${YELLOW_RG}${text}${EOC}"
}
function DEBUG_SYS {
    local text=$1
    echo -e "${BLUE_RG}${text}${EOC}"
}
function DEBUG_USR {
    local text=$1
    echo -e "${CYAN_RG}${text}${EOC}"
}

###############################################################################
# FUNCTION: 
#   rnpause (Run aNd PAUSE)
#
# DESCRIPTION: 
#   Executes a passed no-args function (module) then pauses execution.
#
# USAGE: 
#   rnpause <function_name>
#
# ARGUMENTS:
#   <function_name> - The name of the function to execute. This must be a valid 
#                     function defined in the script.
#
# RETURNS:
#   0 - If success.
#   1 - If no function name is provided.
#   2 - If the provided function name is not defined as a function.
###############################################################################
function rnpause {
    # ARGUMENT VALIDATIONS
    if [[ $(type -t "$1") != "function" ]]; then
        echo -e "\n\n[failure] undefined function for execution of '$1'"
        return 2
    fi
    if [[ -z "$1" ]]; then
        echo -e "\n\n[failure] null argument for execution of '$1'"
        return 1
    fi
    # FUNCTION (MODULE) CALL
    echo -e "\n\n[success] execution of '$1'"
    "$1"
    # PAUSE
    read -p "Press Enter to continue..."
    return 0
}

###############################################################################
# FUNCTION: 
#   twd (Tree of Working Directory)
#
# DESCRIPTION:
#   This function prints the directory structure of the specified directory or 
#   the current working directory if none is provided. It displays directories,
#   subdirectories, and files in a hierarchical tree format.
#
# USAGE:
#   twd [directory]
#
# PARAMETERS:
#   directory     Specifies the directory whose structure is to be displayed. If omitted,
#                 the function operates on the current working directory.
#   $1 (optional): Represents the directory to be traversed. [default: current directory]
#   $2 (optional): Represents the indentation level. It is used for formatting purposes to visually represent the directory structure.
#
#
#
# RETURNS:
#   0 on success, non-zero on failure.
#
#
# NOTES:
#   - Hidden files and directories (those starting with `.`) are not displayed.
#   - Symlinks are not followed; only the symlink itself is displayed.
#
# REFERENCES:
#   - Hidden files and directories (those starting with `.`) are not displayed.
#   - Symlinks are not followed; only the symlink itself is displayed.
###############################################################################
function twd {
    # Print current directory
    echo "${2:-}$(basename "${1:-.}")/"
    # Increase indentation for subdirectories
    local sub_indent="${2:-}  "
    # Print files and directories recursively
    for item in "${1:-.}"/*; do
        if [ -f "$item" ]; then
            echo "${sub_indent}$(basename "$item")"
        elif [ -d "$item" ]; then
            twd "$item" "$sub_indent"
        fi
    done
}

###############################################################################
# FUNCTION: 
#   wpath (Windows-style PATH)
#
# DESCRIPTION: 
#   Converts a Unix-style file path to a Windows-style file path.
#   If the path is already a Windows-style path, it returns the path unchanged.
#
# USAGE: 
#   windows_path=$(wpath "$unix_path")
#
# ARGUMENTS:
#   unix_path (string): The Unix-style path to be converted.
#
# RETURNS:
#   0 - Successful conversion or the path was already a Windows path.
#   1 - Failure due to no input.
#   2 - Failure due to invalid input.
###############################################################################
wpath() {
    local input_path="$1"

    # Check if no argument is given
    if [[ -z "$input_path" ]]; then
        echo "Error: $(TEST_FAIL 'No input path provided.')" >&2
        return 1
    fi

    # Check if the input path is a valid Unix-style or Windows-style path
    if ! [[ "$input_path" =~ ^(/|[a-zA-Z]:\\) ]]; then
        echo "Error: $(TEST_FAIL 'Invalid path string provided.')" >&2
        return 2
    fi

    # If the path is already a valid Windows path, return it as is
    if [[ "$input_path" =~ ^[a-zA-Z]:\\ ]]; then
        echo "$input_path"
        return 0
    fi

    # Remove the leading '/'
    input_path="${input_path#/}"
    # Replace '/' with '\'
    windows_path=$(echo "$input_path" | sed 's/\//\\/g')
    # Convert the first segment to uppercase with a trailing ':'
    windows_path=$(echo "$windows_path" | sed 's/^\([a-zA-Z]\)/\U\1:/')

    echo "$windows_path"
    return 0
}

###############################################################################
# FUNCTION: 
#   INSTRACT
#
# DESCRIPTION: 
#   Downloads a file from a specified URL, extracts its contents into a 
#   designated directory, and removes the downloaded file after extraction.
#
# USAGE: 
#   INSTRACT "<url>" "<target_file>" "<extraction_dir>"
#
# ARGUMENTS:
#   url (string):               The URL to download the file from.
#   target_file (string):       The name to save the downloaded file as.
#   extraction_dir (string):    The directory to extract the contents into.
#
# RETURNS:
#   0 - Successful download, extraction, and cleanup.
#   1 - Failure due to missing arguments.
#   2 - Failure during download.
#   3 - Failure during extraction.
#   4 - Failure during cleanup.
###############################################################################
INSTRACT() {
    local url="$1"
    local target_file="$2"
    local extraction_dir="$3"

    # Check if arguments are missing
    if [[ -z "$url" || -z "$target_file" || -z "$extraction_dir" ]]; then
        echo "Error: $(TEST_FAIL 'Missing arguments.')" >&2
        return 1
    fi

    # Step 1: Download the file
    echo "Downloading '${target_file}' from '${url}'..."
    if ! curl -L "$url" -o "$target_file"; then
        echo "Error: $(TEST_FAIL 'Failed to download '${url}'.')" >&2
        return 2
    fi

    # read -p "Press Enter to continue..."

    # Step 2: Extract the file
    echo "Extracting '${target_file}' to '${extraction_dir}'..."
    mkdir -p "$extraction_dir"
    if ! unzip "$target_file" -d "$extraction_dir" >/dev/null; then
        echo "Error: $(TEST_FAIL 'Failed to extract '${target_file}'.')" >&2
        return 3
    fi

    # read -p "Press Enter to continue..."

    # Step 3: Cleanup
    echo "Cleaning up '${target_file}'..."
    if ! rm -f "$target_file"; then
        echo "Warning: Failed to remove '${target_file}'." >&2
        return 4
    fi

    echo "Successfully initialized '${target_file}' in '${extraction_dir}'."
    return 0
}

###############################################################################
# FUNCTION: 
#   exists
#
# DESCRIPTION: 
#   Checks whether a subdirectory with a specified prefix exists in a given
#   base directory. If the prefix is null, it matches the subdirectory name 
#   exactly. If the base directory is not provided, it prints an error message 
#   and exits.
#
# USAGE: 
#   exists <base_directory> [<prefix>]
#
# ARGUMENTS:
#   <base_directory> - The base directory to search within. Must be provided.
#   <prefix>         - The prefix to match against subdirectory names. If null, 
#                      the function will look for a subdirectory with the exact 
#                      name provided.
#
# RETURNS:
#   0 - If a subdirectory matching the criteria exists.
#   1 - If no matching subdirectory exists or the base directory is invalid.
#   2 - If the base directory is not provided.
#
# EXAMPLES:
#   exists "/path/to/dir" "gradle"
#     Checks if any subdirectory within "/path/to/dir" starts with "gradle".
#
#   exists "/path/to/dir"
#     Checks if any subdirectory exists in "/path/to/dir".
#
#   if exists "$PROJ_EXT" "$prefix"; then
#       ...
#   fi
###############################################################################
function exists {
    # ARGUMENT VALIDATIONS
    local base_dir="$1"
    local prefix="$2"

    # Error if base directory is not provided
    if [[ -z "$base_dir" ]]; then
        echo "[failure] No base directory provided. Usage: exists <base_directory> [<prefix>]"
        return 2
    fi

    # Validate the base directory
    if [[ ! -d "$base_dir" ]]; then
        echo "[failure] Base directory '$base_dir' does not exist or is invalid."
        return 1
    fi

    # Determine the search pattern
    local search_pattern
    if [[ -z "$prefix" ]]; then
        search_pattern="$base_dir"/*  # Match any subdirectory
    else
        search_pattern="$base_dir/$prefix"*  # Match prefix or exact name
    fi

    # Check for matching subdirectory
    if ls $search_pattern 1> /dev/null 2>&1; then
        echo "Pass: $(TEST_PASS 'Found a matching '${prefix}..' subdirectory in '$base_dir'')."
        return 0  # Matching subdirectory exists
    else
        echo "Error: $(TEST_FAIL 'No matching '${prefix}..' subdirectory found in '$base_dir'')."
        return 1  # No matching subdirectory exists
    fi
}

###############################################################################
# FUNCTION: 
#   opens
#
# DESCRIPTION: 
#   Opens the specified directory or file in the default system application 
#   based on the operating system. If the provided path does not exist, an 
#   error message is printed.
#
# USAGE: 
#   opens <path>
#
# ARGUMENTS:
#   <path>   - The directory or file to open. Must be provided.
#
# RETURNS:
#   0 - If the specified directory or file was successfully opened.
#   1 - If the path does not exist or is invalid.
#
# EXAMPLES:
#   opens "/path/to/dir"
#     Opens the specified directory in the default file explorer (depending on OS).
#
#   opens "/path/to/file"
#     Opens the specified file in its default application (e.g., a text editor or browser).
#
#   if opens "$file_path"; then
#       echo "File opened successfully!"
#   else
#       echo "Failed to open file."
#   fi
###############################################################################
function opens {
    # ARGUMENT VALIDATION
    local dir=$1

    # Error if no path is provided
    if [[ -z "$dir" ]]; then
        echo "[failure] No path provided. Usage: opens <path>"
        return 1
    fi

    # Check if the path exists
    if [[ ! -e "$dir" ]]; then
        echo "Error: Target not found - $dir"
        return 1
    fi

    # Open the path based on OS type
    case "$OSTYPE" in
        linux*)     xdg-open "$dir" ;;
        darwin*)    open "$dir" ;;
        cygwin*)    cygstart "$dir" ;;
        msys*)      start "$(wpath "$dir")" ;;
        win32*)     start "$(wpath "$dir")" ;;
        *)          echo "Unsupported OS type: $OSTYPE" ;;
    esac

    return 0
}

###############################################################################
# FUNCTION: 
#   instantiate_bash
#
# DESCRIPTION: 
#   Executes a specified script file in a given directory. The script will be 
#   executed in the context of the provided directory, ensuring that all relative
#   paths within the script are resolved correctly. It adapts execution behavior
#   based on the operating system type.
#
# USAGE: 
#   instantiate_bash <execution_directory> <script_filename>
#
# ARGUMENTS:
#   <execution_directory> - The directory in which the script should be executed.
#   <script_filename>      - The filename of the script to be executed (within
#                            the specified directory).
#
# RETURNS:
#   0 - If the script is executed successfully.
#   1 - If the execution directory or script file is invalid or does not exist.
#   2 - If insufficient arguments are provided.
#
# EXAMPLES:
#   instantiate_bash "/path/to/dir" "script.sh"
#     Executes the script "script.sh" located in "/path/to/dir" as an instance.
###############################################################################
function instantiate_bash {
    # ARGUMENT VALIDATIONS
    local execution_directory="$1"
    local script_filename="$2"

    # Error if insufficient arguments are provided
    if [[ -z "$execution_directory" || -z "$script_filename" ]]; then
        echo "[failure] Insufficient arguments provided. Usage: instantiate_bash <execution_directory> <script_filename>"
        return 2
    fi

    # Validate the execution directory
    if [[ ! -d "$execution_directory" ]]; then
        echo "[failure] Execution directory '$execution_directory' does not exist or is invalid."
        return 1
    fi

    # Construct the full script path
    local script_path="$execution_directory/$script_filename"

    # Validate the script file
    if [[ ! -f "$script_path" ]]; then
        echo "[failure] Script file '$script_filename' does not exist in directory '$execution_directory'."
        return 1
    fi

    # Determine the OS type and execute accordingly
    case "$OSTYPE" in
        linux* | darwin*) # Linux and macOS
            cd "$execution_directory"
            bash "./$script_filename"
            cd "$PROJ_DIR"
            ;;
        msys* | cygwin*) # Windows (Git Bash, Cygwin, or MSYS)
            cd "$execution_directory"
            start bash -c "./$script_filename; exec bash"
            cd "$PROJ_DIR"
            ;;
        *)
            echo "[failure] Unsupported OS: $OSTYPE"
            return 1
            ;;
    esac

    # Capture the exit status of the script execution
    local exit_status=$?
    if [[ $exit_status -eq 0 ]]; then
        echo "[success] Script '$script_filename' executed successfully in '$execution_directory'."
    else
        echo "[failure] Script '$script_filename' failed to execute in '$execution_directory' with exit status $exit_status."
    fi

    return $exit_status
}

###############################################################################
# FUNCTION: 
#   ...
#
# DESCRIPTION: 
#   ...
#
# USAGE: 
#   ...
#
# ARGUMENTS:
#   ...
#
# RETURNS:
#   0 - ...
#   1 - ...
#   ...
###############################################################################




#

EOF
)
if ! grep -qF "$MARKER" ~/.bashrc; then
    # Append the script to ~/.bashrc
    echo "$SCRIPT" >> ~/.bashrc
    echo -e "${CONFIG} has been \033[1;32msuccessfully added to \033[1;33m~/.bashrc\033[0m."
else
    echo -e "${CONFIG}\033[1;31m already exists. \033[1;33mNo changes made. \033[0m."
fi
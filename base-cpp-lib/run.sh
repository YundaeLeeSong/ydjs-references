#!/bin/bash
#
# init.sh - Dynamic OS-Aware Wrapper Script
#
# This script identifies the current operating system, displays clean
# system information, and then dynamically finds and executes an
# OS-specific script.
#
# The script to be executed is determined by the base name of this
# wrapper. For example, if this script is named `ex.sh`, it will look
# for `ex-linux.sh`, `ex-osx.sh`, or `ex-win.sh`.
#
# It includes robust, user-friendly error handling.
#

# --- Script Configuration and Safety ---
# -e: Exit immediately if a command exits with a non-zero status.
# -u: Treat unset variables as an error when substituting.
# -o pipefail: The return value of a pipeline is the status of
#              the last command to exit with a non-zero status,
#              or zero if no command exited with a non-zero status.
set -euo pipefail

# --- Dynamic Script Name Identification ---
# Get the base name of this script file, stripping the '.sh' suffix.
# '$0' is the path to the currently running script.
# 'basename' strips directory paths and an optional suffix.
BASE_NAME=$(basename "$0" .sh)

# --- Color Definitions for Output ---
# Use tput to make the output more readable. It checks if the terminal
# supports colors before attempting to use them.
if tput setaf 1 >&/dev/null; then
    COLOR_BLACK=$(tput setaf 0)
    COLOR_RED=$(tput setaf 1)
    COLOR_GREEN=$(tput setaf 10)   # bright green (normal: 2 / 10)
    COLOR_CYAN=$(tput setaf 14)    # bright cyan (normal: 6)
    COLOR_YELLOW=$(tput setaf 3)
    COLOR_BLUE=$(tput setaf 4)
    COLOR_MAGENTA=$(tput setaf 5)
    COLOR_WHITE=$(tput setaf 7)
    COLOR_RESET=$(tput sgr0)
else
    COLOR_BLACK=""
    COLOR_RED=""
    COLOR_GREEN=""
    COLOR_YELLOW=""
    COLOR_BLUE=""
    COLOR_MAGENTA=""
    COLOR_CYAN=""
    COLOR_WHITE=""
    COLOR_RESET=""
fi


echo "--- Wrapper Script [${COLOR_GREEN}./${BASE_NAME}.sh${COLOR_RESET}] Initializing ---"


# --- Display Clear System Information ---
echo "Gathering System Information..."
echo "----------------------------------------------------------------------------------------------"
echo "${COLOR_CYAN}Hostname${COLOR_RESET}:         $(hostname)"
echo "${COLOR_CYAN}Architecture${COLOR_RESET}:     $(uname -m)"

# Determine the operating system using the 'uname' command.
OS_NAME=$(uname -s)

# Use a case statement for OS-specific info gathering.
case "${OS_NAME}" in
    # For Linux systems.
    Linux*)
        # '/etc/os-release' is the standard way to get distro info.
        if [ -f /etc/os-release ]; then
            # Source the file to load its variables (like PRETTY_NAME).
            . /etc/os-release
            echo "${COLOR_CYAN}Operating System${COLOR_RESET}: ${PRETTY_NAME}"
        else
            # Fallback if the file doesn't exist.
            echo "${COLOR_CYAN}Operating System${COLOR_RESET}: Linux (Distribution details unavailable)"
        fi
        echo "${COLOR_CYAN}Kernel Version${COLOR_RESET}:   $(uname -r)"
        ;;

    # For macOS, 'uname -s' returns "Darwin".
    Darwin*)
        # 'sw_vers' is the standard command for macOS version info.
        PRODUCT_NAME=$(sw_vers -productName)
        PRODUCT_VERSION=$(sw_vers -productVersion)
        BUILD_VERSION=$(sw_vers -buildVersion)
        echo "${COLOR_CYAN}Operating System${COLOR_RESET}: ${PRODUCT_NAME} ${PRODUCT_VERSION} (Build ${BUILD_VERSION})"
        echo "${COLOR_CYAN}Kernel Version${COLOR_RESET}:   $(uname -r)"
        ;;

    # For Windows environments with bash compatibility (Git Bash, Cygwin, etc).
    CYGWIN*|MINGW*|MSYS*|Windows_NT*)
        echo "${COLOR_CYAN}Operating System${COLOR_RESET}: Windows (using a bash compatibility layer)"
        echo "${COLOR_CYAN}Environment${COLOR_RESET}:      ${OS_NAME}"
        echo "${COLOR_CYAN}Kernel Version${COLOR_RESET}:   $(uname -r)"
        ;;

    # If the OS is not recognized, print an error and exit.
    *)
        echo "${COLOR_RED}Error: Unsupported operating system kernel '${OS_NAME}'.${COLOR_RESET}"
        exit 1
        ;;
esac
echo "----------------------------------------------------------------------------------------------"


# --- Dynamic Script Lookup ---
# Based on the OS, determine the correct suffix for the target script.
OS_SUFFIX=""
case "${OS_NAME}" in
    Linux*)                           OS_SUFFIX="linux" ;;
    Darwin*)                          OS_SUFFIX="osx"   ;;
    CYGWIN*|MINGW*|MSYS*|Windows_NT*)  OS_SUFFIX="win"   ;;
esac

# Construct the full filename of the target script.
SCRIPT_TO_RUN="./scripts/${BASE_NAME}-${OS_SUFFIX}.sh"
echo "Looking for OS-specific script: ${SCRIPT_TO_RUN}"


# --- Execution Logic with Improved Error Handling ---
# First, check if the target script file and any subdirectories exist.
# The '-f' flag checks for a regular file.

if [ ! -f "${SCRIPT_TO_RUN}" ]; then
    # The file does not exist. Check if parent directories exist and create them if needed.
    SCRIPT_DIR=$(dirname "${SCRIPT_TO_RUN}")
    
    if [ ! -d "${SCRIPT_DIR}" ]; then
        echo "${COLOR_YELLOW}Creating directory structure: ${SCRIPT_DIR}${COLOR_RESET}"
        mkdir -p "${SCRIPT_DIR}"
    fi
    
    echo "${COLOR_RED}Error: Target script '${SCRIPT_TO_RUN}' was not found.${COLOR_RESET}"
    echo -e "\tCreating a template file for you..."

    # Use a 'here document' (cat <<EOF) to write a multiline string to the new file.
    cat <<EOF > "${SCRIPT_TO_RUN}"
#!/bin/bash
#
# ${SCRIPT_TO_RUN}
#
# This is an auto-generated template for your OS-specific logic.
# It was created by the wrapper script because the file did not exist.
#
set -euo pipefail
echo "Hello from the new, auto-generated script for win!"
echo "You can add your OS-specific commands here."

# --- Color Definitions for Output ---
# Use tput to make the output more readable. It checks if the terminal
# supports colors before attempting to use them.
if tput setaf 1 >&/dev/null; then
    COLOR_BLACK=\$(tput setaf 0)
    COLOR_RED=\$(tput setaf 1)
    COLOR_GREEN=\$(tput setaf 10)   # bright green (normal: 2 / 10)
    COLOR_CYAN=\$(tput setaf 14)    # bright cyan (normal: 6)
    COLOR_YELLOW=\$(tput setaf 3)
    COLOR_BLUE=\$(tput setaf 4)
    COLOR_MAGENTA=\$(tput setaf 5)
    COLOR_WHITE=\$(tput setaf 7)
    COLOR_RESET=\$(tput sgr0)
else
    COLOR_BLACK=""
    COLOR_RED=""
    COLOR_GREEN=""
    COLOR_YELLOW=""
    COLOR_BLUE=""
    COLOR_MAGENTA=""
    COLOR_CYAN=""
    COLOR_WHITE=""
    COLOR_RESET=""
fi

# --- Logic here! ---


EOF
    # Confirm creation and tell the user the next step.
    echo -e "\t${COLOR_GREEN}Successfully created '${SCRIPT_TO_RUN}'.${COLOR_RESET}"
    echo -e "\tPlease add your commands to the new file and then make it executable by running: ${COLOR_YELLOW}chmod +x ${SCRIPT_TO_RUN}${COLOR_RESET}"
    exit 1

# Next, if the file exists, check if it has execute permission ('-x').
elif [ ! -x "${SCRIPT_TO_RUN}" ]; then
    # The file exists but is not executable. Guide the user to fix it.
    echo "${COLOR_YELLOW}Error: Target script '${SCRIPT_TO_RUN}' was found, but it is not executable.${COLOR_RESET}"
    echo "Please grant execute permissions by running the following command:"
    echo "${COLOR_YELLOW}chmod +x ${SCRIPT_TO_RUN}${COLOR_RESET}"
    exit 1

else
    # Success: The file exists and is executable.
    echo "Found executable target script. ${COLOR_GREEN}Running the found file at ${SCRIPT_TO_RUN}...${COLOR_RESET}"
    echo ""
    echo "${COLOR_YELLOW}↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓${COLOR_RESET}"
    echo ""
    # Execute the OS-specific script, passing along any arguments
    # that were given to this wrapper script ('$@').
    "${SCRIPT_TO_RUN}" "$@"
fi










#   {
#     "key": "ctrl+r",
#     "command": "editor.action.insertSnippet",
#     "when": "editorTextFocus && editorLangId == 'shellscript'",
#     "args": { "snippet": "\\${COLOR_RED}${TM_SELECTED_TEXT}\\${COLOR_RESET}" }
#   },
#   {
#     "key": "ctrl+g",
#     "command": "editor.action.insertSnippet",
#     "when": "editorTextFocus && editorLangId == 'shellscript'",
#     "args": { "snippet": "\\${COLOR_GREEN}${TM_SELECTED_TEXT}\\${COLOR_RESET}" }
#   },
#   {
#     "key": "ctrl+b",
#     "command": "editor.action.insertSnippet",
#     "when": "editorTextFocus && editorLangId == 'shellscript'",
#     "args": { "snippet": "\\${COLOR_CYAN}${TM_SELECTED_TEXT}\\${COLOR_RESET}" }
#   },
#   {
#     "key": "ctrl+y",
#     "command": "editor.action.insertSnippet",
#     "when": "editorTextFocus && editorLangId == 'shellscript'",
#     "args": { "snippet": "\\${COLOR_YELLOW}${TM_SELECTED_TEXT}\\${COLOR_RESET}" }
#   },


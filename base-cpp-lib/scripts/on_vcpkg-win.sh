#!/bin/bash
#
# ./scripts/on_vcpkg-win.sh
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

# go to ../ext directory, ext should be created if there is no ext directory.
cd ..
mkdir -p ext
cd ext

# 1. Clone it, if there is no vcpkg directory.
if [ ! -d "vcpkg" ]; then
    echo -e "${COLOR_YELLOW}vcpkg directory not found. Cloning vcpkg...${COLOR_RESET}"
    git clone https://github.com/microsoft/vcpkg.git
fi

cd vcpkg
./bootstrap-vcpkg.bat



# # 2. Run the bootstrap script (do this only once)
# ./vcpkg/bootstrap-vcpkg.sh  # On Linux/macOS
# .\vcpkg\bootstrap-vcpkg.bat # On Windows
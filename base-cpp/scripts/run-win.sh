#!/bin/bash
#
# ./scripts/run-win.sh
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

# --- Logic here! ---

# if there is build directory, prompt the user if they want to delete it
if [ -d "build" ]; then
    echo -e "${COLOR_YELLOW}Build directory already exists.${COLOR_RESET}"
    read -p "Do you want to delete it and create a new one? (y/n): " choice
    if [[ "$choice" == "y" || "$choice" == "Y" ]]; then
        rm -rf build
        echo -e "${COLOR_GREEN}Deleted existing build directory.${COLOR_RESET}"
    else
        echo -e "${COLOR_CYAN}Using existing build directory.${COLOR_RESET}"
    fi
fi
cmake -S . -B build -DCMAKE_TOOLCHAIN_FILE=../ext/vcpkg/scripts/buildsystems/vcpkg.cmake
cmake --build build --config Release
./build/Release/qt_vcpkg_demo.exe
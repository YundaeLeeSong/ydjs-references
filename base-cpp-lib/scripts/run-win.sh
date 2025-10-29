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

# Clean up old build and distribution directories
if [ -d "build" ]; then
    echo -e "${COLOR_YELLOW}Build and Distribution directory already exists.${COLOR_RESET}"
    read -p "Do you want to delete it and create a new one? (y/n): " choice
    if [[ "$choice" == "y" || "$choice" == "Y" ]]; then
        rm -rf build
        rm -rf dist
        echo -e "${COLOR_GREEN}Deleted existing build directory.${COLOR_RESET}"
        # This reads 'CMakePresets.json' and runs the 'windows-vcpkg' preset.
        # It creates the 'build/' directory and generates the VS project files.
        cmake --preset=windows-vcpkg
        echo -e "${COLOR_CYAN}Build directory created.${COLOR_RESET}"
    else
        echo -e "${COLOR_CYAN}Using existing build directory.${COLOR_RESET}"
    fi
fi





# # Build and test using presets.
# # This finds the 'debug' build preset, which adds '--config Debug'.
# cmake --build --preset=debug
# # This finds the 'debug' test preset, which runs ctest for the Debug build.
# ctest --preset=debug




# switch-case for 1: build and test, 2: build and run, 3: distribution (install + package)
# user prompt
echo -e "${COLOR_YELLOW}Please select an option:${COLOR_RESET}"
echo -e "1) [Debug] Build and Test"
echo -e "2) [Debug] Build and Run"
echo -e "3) [Release] Build and Test"
echo -e "4) [Release] Build and Run"
echo -e "5) [Release] Distribution (Install + Package)"
read -p "Enter your choice (1/2/3/4/5): " choice
case $choice in
    1)
        echo -e "${COLOR_CYAN}Building and testing the Debug configuration...${COLOR_RESET}"
        cmake --build --preset=debug
        ctest --preset=debug
        ;;
    2)
        echo -e "${COLOR_CYAN}Building and running the Debug configuration...${COLOR_RESET}"
        cmake --build --preset=debug
        ./build/bin/Debug/my_app.exe
        ;;
    3)
        echo -e "${COLOR_CYAN}Building and testing the Release configuration...${COLOR_RESET}"
        cmake --build --preset=release
        ctest --preset=release
        ;;
    4)
        echo -e "${COLOR_CYAN}Building and running the Release configuration...${COLOR_RESET}"
        cmake --build --preset=release
        ./build/bin/Release/my_app.exe
        ;;
    5)
        echo -e "${COLOR_CYAN}Packaging the application...${COLOR_RESET}"
        cmake --build --preset=release
        cpack --config build/CPackConfig.cmake -C Release
        ;;
    *)
        echo -e "${COLOR_RED}Invalid option. Use 1 for build/test, 2 for build/run, 3 for package.${COLOR_RESET}"
        exit 1
        ;;
esac
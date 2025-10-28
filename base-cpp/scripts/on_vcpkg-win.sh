#!/bin/bash
#
# ./scripts/on_vcpkg-win.sh
#
# This is an auto-generated template for your OS-specific logic.
# It was created by the wrapper script because the file did not exist.
#

echo "Hello from the new, auto-generated script for win!"
echo "You can add your OS-specific commands here."

# Define color codes for terminal output.
COLOR_RED="\033[0;31m"
COLOR_GREEN="\033[0;32m"
COLOR_YELLOW="\033[0;33m"
COLOR_RESET="\033[0m"

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
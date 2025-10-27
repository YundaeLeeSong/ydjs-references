#!/bin/bash
echo -e "${MINT_COLOR}Starting installation process...${RESET_COLOR}"
# Color for formatting
MINT_COLOR="\e[38;5;49m"
RESET_COLOR="\e[0m"
# Set installation paths
INSTALL_DIR="$(pwd)/ext"
CPP_LANG_SYS="$INSTALL_DIR/mingw64/bin"
CMAKE_DIR="$INSTALL_DIR/cmake-3.26.4-windows-x86_64/bin"



NSIS_VERSION="3.10"
NSIS_DIR="$INSTALL_DIR/nsis-${NSIS_VERSION}"

# 7z PATH setup
SEVEN_ZIP_DIR="/c/Program Files/Unity/Hub/Editor/2021.3.38f1/Editor/Data/Tools"
export PATH="${PATH}:${SEVEN_ZIP_DIR}"
7z -version
EXECUTABLE="$(pwd)/bin/win"





# Clean up
echo -e "${MINT_COLOR}Cleaning up...${RESET_COLOR}"
rm -rf ${INSTALL_DIR}




# Download and extract MinGW
MINGW_URL="https://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win64/Personal%20Builds/mingw-builds/8.1.0/threads-posix/seh/x86_64-8.1.0-release-posix-seh-rt_v6-rev0.7z"
MINGW_TARGET="mingw.7z"
echo -e "${MINT_COLOR}Downloading MinGW...${RESET_COLOR}"
curl -L "$MINGW_URL" -o ${MINGW_TARGET}
echo -e "${MINT_COLOR}Extracting MinGW...${RESET_COLOR}"
7z x ${MINGW_TARGET} -o"$INSTALL_DIR"
rm ${MINGW_TARGET}
mv "$CPP_LANG_SYS/mingw32-make.exe" "$CPP_LANG_SYS/make.exe"




# Download and extract CMake
CMAKE_URL="https://github.com/Kitware/CMake/releases/download/v3.26.4/cmake-3.26.4-windows-x86_64.zip"
CMAKE_TARGET="cmake.zip"
echo -e "${MINT_COLOR}Downloading CMake...${RESET_COLOR}"
curl -L "$CMAKE_URL" -o ${CMAKE_TARGET}
echo -e "${MINT_COLOR}Extracting CMake...${RESET_COLOR}"
unzip ${CMAKE_TARGET} -d "$INSTALL_DIR"
rm ${CMAKE_TARGET}
# Add to PATH
echo -e "${MINT_COLOR}Adding MinGW to PATH...${RESET_COLOR}"
export PATH="${PATH}:${CPP_LANG_SYS}"
gcc --version
g++ --version
make --version
# Add to PATH
echo -e "${MINT_COLOR}Adding CMake to PATH...${RESET_COLOR}"
export PATH="${PATH}:${CMAKE_DIR}"
cmake --version
echo -e "${MINT_COLOR}Installation complete. Please restart your Git Bash.${RESET_COLOR}"





# Download and extract NSIS (Nullsoft Scriptable Install System)

NSIS_URL="https://sourceforge.net/projects/nsis/files/NSIS%203/${NSIS_VERSION}/nsis-${NSIS_VERSION}.zip"
NSIS_TARGET="nsis-${NSIS_VERSION}.zip"
echo -e "${MINT_COLOR}Downloading NSIS...${RESET_COLOR}"
curl -L "$NSIS_URL" -o ${NSIS_TARGET}
echo -e "${MINT_COLOR}Extracting NSIS...${RESET_COLOR}"
unzip ${NSIS_TARGET} -d "$INSTALL_DIR"
rm ${NSIS_TARGET}
# Add to PATH
echo -e "${MINT_COLOR}Adding NSIS to PATH...${RESET_COLOR}"
export PATH="${PATH}:${NSIS_DIR}"
makensis -version
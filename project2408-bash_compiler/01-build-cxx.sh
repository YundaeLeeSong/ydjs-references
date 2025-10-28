#!/bin/bash
echo -e "${MINT_COLOR}Starting installation process...${RESET_COLOR}"
TOP_LV_CMAKE_DIR="$(pwd)"
# Color for formatting
MINT_COLOR="\e[38;5;49m"
RESET_COLOR="\e[0m"
# Set download URLs
MINGW_URL="https://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win64/Personal%20Builds/mingw-builds/8.1.0/threads-posix/seh/x86_64-8.1.0-release-posix-seh-rt_v6-rev0.7z"
MINGW_TARGET="mingw.7z"
CMAKE_URL="https://github.com/Kitware/CMake/releases/download/v3.26.4/cmake-3.26.4-windows-x86_64.zip"
CMAKE_TARGET="cmake.zip"
# Set installation paths
INSTALL_DIR="$(pwd)/ext"
CPP_LANG_SYS="$INSTALL_DIR/mingw64/bin"
CMAKE_DIR="$INSTALL_DIR/cmake-3.26.4-windows-x86_64/bin"
NSIS_VERSION="3.10"
NSIS_DIR="$INSTALL_DIR/nsis-${NSIS_VERSION}"
# 7z PATH setup
SEVEN_ZIP_DIR="/c/Program Files/Unity/Hub/Editor/2021.3.38f1/Editor/Data/Tools"
export PATH="${PATH}:${SEVEN_ZIP_DIR}"
echo -e "\n\n\n${MINT_COLOR}Adding 7z to PATH...${RESET_COLOR}"
7z -version
echo -e "\n\n\n${MINT_COLOR}Adding MinGW to PATH...${RESET_COLOR}"
export PATH="${PATH}:${CPP_LANG_SYS}"
gcc --version
g++ --version
make --version
echo -e "\n\n\n${MINT_COLOR}Adding CMake to PATH...${RESET_COLOR}"
export PATH="${PATH}:${CMAKE_DIR}"
cmake --version
echo -e "${MINT_COLOR}Adding NSIS to PATH...${RESET_COLOR}"
export PATH="${PATH}:${NSIS_DIR}"
makensis -version


gcc --version
g++ --version
make --version
cmake --version



CMAKE_CURRENT_BINARY_DIR="$(pwd)/out/build/x64-Debug"
CMAKE_INSTALL_PREFIX="$(pwd)/out/install/x64-Debug"
CMACK_OUTPUT_FILE_PREFIX="$(pwd)/dist"



#################################################################
#################< ALL distribution process >##################
#################################################################
rm -rf ${CMAKE_CURRENT_BINARY_DIR}
rm -rf ${CMAKE_INSTALL_PREFIX}
rm -rf ${CMACK_OUTPUT_FILE_PREFIX}
echo -e "\n\n\n"
read -p "press any key to 'tranlate'... (cmake -> make)"
##### (1) CMakeLists -> Makefile (cross-platform)
cmake -G "MinGW Makefiles" ${TOP_LV_CMAKE_DIR} -B ${CMAKE_CURRENT_BINARY_DIR} \
-DCMAKE_MAKE_PROGRAM="$CPP_LANG_SYS/make.exe" \
-DCMAKE_C_COMPILER="$CPP_LANG_SYS/gcc.exe" \
-DCMAKE_CXX_COMPILER="$CPP_LANG_SYS/g++.exe" \
-DCMAKE_INSTALL_PREFIX="${CMAKE_INSTALL_PREFIX}" \
-DCMACK_OUTPUT_FILE_PREFIX="${CMACK_OUTPUT_FILE_PREFIX}"
##### (2) Makefile -> Executable (platform-specific)
echo "Choose the options to 'build'... (make/cpack)"
echo "1) Makefile -> Build: executable (compilation)"
echo "2) Makefile -> Build: executable & Library Distribution (compilation & export targets)"
echo "3) Makefile -> Release: Standalone Distribution (release & deployment)"
echo "Press any other key to exit."
read -p "Enter your choice: " choice
case $choice in
  1) cmake --build ${CMAKE_CURRENT_BINARY_DIR} ;;
  # (1) Equivalent Command: `make -C ${CMAKE_CURRENT_BINARY_DIR}`
  2) cmake --build ${CMAKE_CURRENT_BINARY_DIR} --target install ;;
  # (2) Equivalent Command: `make install -C ${CMAKE_CURRENT_BINARY_DIR}`
  3) cmake --build ${CMAKE_CURRENT_BINARY_DIR} --target package ;;
  # (3) Equivalent Command: `cd ${CMAKE_CURRENT_BINARY_DIR} && cpack`
  *) echo "Exiting..." && exit 0 ;;
esac
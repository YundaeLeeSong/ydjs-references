###############################################################
# configuration (Visual Studio)
###############################################################
# This section ensures that the MSVC compiler (Visual Studio) supports "Edit and Continue"
# and "Program Database" debugging features during the build process.
if (POLICY CMP0141) # Enable Hot Reload for MSVC compilers if supported.
    cmake_policy(SET CMP0141 NEW)
    set(CMAKE_MSVC_DEBUG_INFORMATION_FORMAT "$<IF:$<AND:$<C_COMPILER_ID:MSVC>,$<CXX_COMPILER_ID:MSVC>>,$<$<CONFIG:Debug,RelWithDebInfo>:EditAndContinue>,$<$<CONFIG:Debug,RelWithDebInfo>:ProgramDatabase>>")
endif()
###############################################################
# configuration (Debugging)
###############################################################
string(ASCII 27 ESCAPE)
set(_RESET        "${ESCAPE}[0m")
# creates the escape character for coloring
set(_USRPROMPT    "${ESCAPE}[1;33m")    # Yellow for prompts
set(_DEBUG_SYS    "${ESCAPE}[1;34m")    # Blue for system debug messages
set(_DEBUG_USR    "${ESCAPE}[1;36m")    # Cyan for user debug messages
set(_TEST_FAIL    "${ESCAPE}[1;31m")    # Red for test failures
set(_TEST_PASS    "${ESCAPE}[1;32m")    # Green for test passes
message(STATUS "${ESCAPE}[1;35m=============== Example Usage ================${_RESET}")
message(STATUS "${_USRPROMPT}[_USRPROMPT] * * * Debug [] in ${_CURRENT_DIR_NAME}${_RESET}")
message(STATUS "${_DEBUG_SYS}[_DEBUG_SYS]  _CURRENT_DIR_NAME  :  ${_CURRENT_DIR_NAME}${_RESET}")
message(STATUS "${_DEBUG_USR}[_DEBUG_USR]  _CURRENT_DIR_NAME  :  ${_CURRENT_DIR_NAME}${_RESET}")
message(STATUS "${_TEST_FAIL}[_TEST_FAIL]  _CURRENT_DIR_NAME  :  ${_CURRENT_DIR_NAME}${_RESET}")
message(STATUS "${_TEST_PASS}[_TEST_PASS]  _CURRENT_DIR_NAME  :  ${_CURRENT_DIR_NAME}${_RESET}")
message(STATUS "${ESCAPE}[1;35m==============================================${_RESET}")
###############################################################
# Project Meta-Data
###############################################################
# Define project-wide variables for easy configuration and maintainability.
# Project Variables:
# - _CURRENT_DIR_NAME: basename of the current source directory.
# - _PROJECT_NAME: The name of your project.
# - _PROJECT_VERSION: The version of your project.
# - _CMAKE_VERSION_REQUIRED: The minimum required version of CMake.
# - _CXX_STANDARD_REQUIRED: The C++ standard required for the project.
get_filename_component(_CURRENT_DIR_NAME ${CMAKE_CURRENT_SOURCE_DIR} NAME)
message(STATUS "${_USRPROMPT}[_USRPROMPT] * * * Debug [project meda-data] in ${_CURRENT_DIR_NAME}${_RESET}")
set(_PROJECT_NAME "${_CURRENT_DIR_NAME}")
message(STATUS "${_DEBUG_USR}[_DEBUG_USR]  _PROJECT_NAME  :  ${_PROJECT_NAME}${_RESET}")
set(_PROJECT_VERSION "2.3.4") # <major>.<minor>.<patch>
message(STATUS "${_DEBUG_USR}[_DEBUG_USR]  _PROJECT_VERSION  :  ${_PROJECT_VERSION}${_RESET}")
set(_PROJECT_CONTACT "jsong421@gatech.edu")
message(STATUS "${_DEBUG_USR}[_DEBUG_USR]  _PROJECT_CONTACT  :  ${_PROJECT_CONTACT}${_RESET}")
set(_PROJECT_DESCRIPTION_SUMMARY "A brief description of the project by Jaehoon Song.")
message(STATUS "${_DEBUG_USR}[_DEBUG_USR]  _PROJECT_DESCRIPTION_SUMMARY  :  ${_PROJECT_DESCRIPTION_SUMMARY}${_RESET}")
set(_CMAKE_VERSION_REQUIRED "3.8")
message(STATUS "${_DEBUG_USR}[_DEBUG_USR]  _CMAKE_VERSION_REQUIRED  :  ${_CMAKE_VERSION_REQUIRED}${_RESET}")
set(_CXX_STANDARD_REQUIRED "20")
message(STATUS "${_DEBUG_USR}[_DEBUG_USR]  _CXX_STANDARD_REQUIRED  :  ${_CXX_STANDARD_REQUIRED}${_RESET}")
# project configuration (platform-dependent)
if(WIN32)
    set(_OS_NAME "Windows")
elseif(UNIX AND NOT APPLE)
    set(_OS_NAME "Linux")
elseif(APPLE)
    set(_OS_NAME "macOS")
elseif(CMAKE_SYSTEM_NAME MATCHES "FreeBSD")
    set(_OS_NAME "FreeBSD")
elseif(CMAKE_SYSTEM_NAME MATCHES "OpenBSD")
    set(_OS_NAME "OpenBSD")
elseif(CMAKE_SYSTEM_NAME MATCHES "NetBSD")
    set(_OS_NAME "NetBSD")
else()
    set(_OS_NAME "Unknown OS")
endif()
message(STATUS "${_DEBUG_USR}[_DEBUG_USR]  _OS_NAME  :  ${_OS_NAME}${_RESET}")
if (_OS_NAME STREQUAL "Windows")
    set(CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS ON)  # automate __declspec(dllexport) on .dll
else()
    set(CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS OFF)
endif()
message(STATUS "${_DEBUG_SYS}[_DEBUG_SYS]  CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS  :  ${CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS}${_RESET}")
if (NOT DEFINED CMAKE_CXX_FLAGS OR CMAKE_CXX_FLAGS STREQUAL "")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -static-libgcc -static")    # statically link system dll(s)
endif()
message(STATUS "${_DEBUG_SYS}[_DEBUG_SYS]  CMAKE_CXX_FLAGS  :  ${CMAKE_CXX_FLAGS}${_RESET}")
############### project meta-data
cmake_minimum_required(VERSION ${_CMAKE_VERSION_REQUIRED})
project(${_PROJECT_NAME} VERSION ${_PROJECT_VERSION})





















###############################################################
# Project Compilation (Build, Private)
###############################################################
# Directory Variables:
# - _BUILD_SRC_DIR: Directory containing the source files.
# - _BUILD_INCLUDE_DIR: Directory containing the header files.
# - _BUILD_LIB_DIR: Directory where libraries would be stored.
# - _BUILD_TEST_DIR: Directory where tests would be stored.
get_filename_component(_CURRENT_DIR_NAME "${CMAKE_CURRENT_SOURCE_DIR}" NAME)
message(STATUS "${_USRPROMPT}[_USRPROMPT] * * * Debug [build] in ${_CURRENT_DIR_NAME}${_RESET}")
set(_BUILD_SRC_DIR "${CMAKE_CURRENT_SOURCE_DIR}/src/main")
message(STATUS "${_DEBUG_USR}[_DEBUG_USR]  _BUILD_SRC_DIR  :  ${_BUILD_SRC_DIR}${_RESET}")
set(_BUILD_LIB_DIR "${CMAKE_CURRENT_SOURCE_DIR}/lib")
message(STATUS "${_DEBUG_USR}[_DEBUG_USR]  _BUILD_LIB_DIR  :  ${_BUILD_LIB_DIR}${_RESET}")
set(_BUILD_STATIC_DIR "${CMAKE_CURRENT_SOURCE_DIR}/src/stat")
message(STATUS "${_DEBUG_USR}[_DEBUG_USR]  _BUILD_STATIC_DIR  :  ${_BUILD_STATIC_DIR}${_RESET}")
get_filename_component(_BUILD_STATIC_TARGETS "${_BUILD_STATIC_DIR}" NAME)
message(STATUS "${_DEBUG_USR}[_DEBUG_USR]  _BUILD_STATIC_TARGETS  :  ${_BUILD_STATIC_TARGETS}${_RESET}")
set(_BUILD_DYNAMIC_DIR "${CMAKE_CURRENT_SOURCE_DIR}/src/dyna")
message(STATUS "${_DEBUG_USR}[_DEBUG_USR]  _BUILD_DYNAMIC_DIR  :  ${_BUILD_DYNAMIC_DIR}${_RESET}")
get_filename_component(_BUILD_DYNAMIC_TARGETS "${_BUILD_DYNAMIC_DIR}" NAME)
message(STATUS "${_DEBUG_USR}[_DEBUG_USR]  _BUILD_DYNAMIC_TARGETS  :  ${_BUILD_DYNAMIC_TARGETS}${_RESET}")
set(_BUILD_DYNASTATIC_TARGETS "${_BUILD_DYNAMIC_TARGETS}_static")
message(STATUS "${_DEBUG_USR}[_DEBUG_USR]  _BUILD_DYNASTATIC_TARGETS  :  ${_BUILD_DYNASTATIC_TARGETS}${_RESET}")
set(_BUILD_DYNAMIC_SOVER "3") # soversion == major version
set(_BUILD_DYNAMIC_VER_MINOR "2")
set(_BUILD_DYNAMIC_VER_PATCH "1")
set(_BUILD_DYNAMIC_VER "${_BUILD_DYNAMIC_SOVER}.${_BUILD_DYNAMIC_VER_MINOR}.${_BUILD_DYNAMIC_VER_PATCH}")
message(STATUS "${_DEBUG_USR}[_DEBUG_USR]  _BUILD_DYNAMIC_SOVER  :  ${_BUILD_DYNAMIC_SOVER}${_RESET}")
message(STATUS "${_DEBUG_USR}[_DEBUG_USR]  _BUILD_DYNAMIC_VER  :  ${_BUILD_DYNAMIC_VER}${_RESET}")
set(_BUILD_TEST_DIR "${CMAKE_CURRENT_SOURCE_DIR}/src/tests")
message(STATUS "${_DEBUG_USR}[_DEBUG_USR]  _BUILD_TEST_DIR  :  ${_BUILD_TEST_DIR}${_RESET}")
set(_BUILD_INCLUDE_DIR "${PROJECT_SOURCE_DIR}/include")
message(STATUS "${_DEBUG_USR}[_DEBUG_USR]  _BUILD_INCLUDE_DIR  :  ${_BUILD_INCLUDE_DIR}${_RESET}")
set(_BUILD_LIB_DIR "${PROJECT_SOURCE_DIR}/lib")
message(STATUS "${_DEBUG_USR}[_DEBUG_USR]  _BUILD_LIB_DIR  :  ${_BUILD_LIB_DIR}${_RESET}")
# system variabele reference for debugging
message(STATUS "*************** Debugging in ${_CURRENT_DIR_NAME} ***************")
message(STATUS "-CMAKE_CURRENT_SOURCE_DIR-: ${CMAKE_CURRENT_SOURCE_DIR}")   # directory of submodule CMakeLists.txt
message(STATUS "-PROJECT_SOURCE_DIR-: ${PROJECT_SOURCE_DIR}")               # directory of top-level CMakeLists.txt
message(STATUS "-CMAKE_SYSTEM_NAME-: ${CMAKE_SYSTEM_NAME}")
message(STATUS "-CMAKE_INSTALL_PREFIX-: ${CMAKE_INSTALL_PREFIX}")
message(STATUS "-CMAKE_CURRENT_BINARY_DIR-: ${CMAKE_CURRENT_BINARY_DIR}")
message(STATUS "*****************************************")
message(STATUS "-CMAKE_MAKE_PROGRAM-: ${CMAKE_MAKE_PROGRAM}")
message(STATUS "-CMAKE_C_COMPILER-: ${CMAKE_C_COMPILER}")
message(STATUS "-CMAKE_CXX_COMPILER-: ${CMAKE_CXX_COMPILER}")
message(STATUS "******************** static linking *********************")
message(STATUS "-BUILD_SHARED_LIBS-: ${BUILD_SHARED_LIBS}")
message(STATUS "-CMAKE_EXE_LINKER_FLAGS-: ${CMAKE_EXE_LINKER_FLAGS}")

message(STATUS "*****************************************")
#
# Add sources to this project's executable.
#
# (1) preprocessor: Include directories 
include_directories(${_BUILD_INCLUDE_DIR})
# (2) Static Library
file(GLOB STATIC_SOURCES "${_BUILD_STATIC_DIR}/*.cpp")             # (2) compiler:
message(STATUS "${_TEST_FAIL}[_TEST_FAIL]  STATIC_SOURCES  :  ${STATIC_SOURCES}${_RESET}")
add_library(${_BUILD_STATIC_TARGETS} STATIC ${STATIC_SOURCES})
#target_include_directories(stat PUBLIC ${_BUILD_INCLUDE_DIR})
# (3-1) Dynamic Library
file(GLOB DYNAMIC_SOURCES "${_BUILD_DYNAMIC_DIR}/*.cpp")           # (2) compiler:
message(STATUS "${_TEST_FAIL}[_TEST_FAIL]  DYNAMIC_SOURCES  :  ${DYNAMIC_SOURCES}${_RESET}")
add_library(${_BUILD_DYNAMIC_TARGETS} SHARED ${DYNAMIC_SOURCES})
set_target_properties(${_BUILD_DYNAMIC_TARGETS} PROPERTIES 
    RUNTIME_OUTPUT_NAME "${_BUILD_DYNAMIC_TARGETS}-${_BUILD_DYNAMIC_SOVER}"      # This sets the DLL name
    ARCHIVE_OUTPUT_NAME "${_BUILD_DYNAMIC_TARGETS}"                              # This sets the import library name
    VERSION ${_BUILD_DYNAMIC_VER}
    SOVERSION ${_BUILD_DYNAMIC_SOVER}
    OUTPUT_NAME ${_BUILD_DYNAMIC_TARGETS}
)
#target_include_directories(dyna PUBLIC ${_BUILD_INCLUDE_DIR})
# (3-2) Dynamic Library for Static Linking
add_library(${_BUILD_DYNASTATIC_TARGETS} STATIC ${DYNAMIC_SOURCES})
set_target_properties(${_BUILD_DYNASTATIC_TARGETS} PROPERTIES 
    OUTPUT_NAME ${_BUILD_DYNAMIC_TARGETS}
)













##################################33 CMake Practice
# Create the directory structure
file(MAKE_DIRECTORY "project/data")
file(MAKE_DIRECTORY "project/scripts")
file(MAKE_DIRECTORY "project/images")

# Create some files with corrected names
file(WRITE "project/data/file-1.txt" "")
file(WRITE "project/data/file-2.txt" "")
file(WRITE "project/data/file-3.csv" "")
file(WRITE "project/data/file-7.txt" "")
file(WRITE "project/data/file-99.txt" "")
file(WRITE "project/data/script-10.sh" "")
file(WRITE "project/data/script-20.sh" "")
file(WRITE "project/scripts/script-1.sh" "")
file(WRITE "project/scripts/script-2.sh" "")
file(WRITE "project/images/image-1.jpg" "")
file(WRITE "project/images/image-2.png" "")
file(WRITE "project/README.md" "")
file(WRITE "project/setup.sh" "")

# List all files and directories in project
file(GLOB all_files_and_dirs "project/*")
message(STATUS "1. List all files and directories in project:")
message(STATUS "${all_files_and_dirs}")

# List all .txt files in project/data
file(GLOB txt_files "project/data/*.txt")
message(STATUS "2. List all .txt files in project/data:")
message(STATUS "${txt_files}")

# List files in project/data with a single digit in their name
file(GLOB single_digit_files "project/data/file-?.txt")
message(STATUS "3. List files in project/data with a single digit in their name:")
message(STATUS "${single_digit_files}")

# List files in project/data with either 1 or 2 in their name
file(GLOB one_or_two_files "project/data/file-[12].txt")
message(STATUS "4. List files in project/data with either 1 or 2 in their name:")
message(STATUS "${one_or_two_files}")

# List .sh files in both project/scripts and project/data
file(GLOB sh_files_data "project/data/*.sh")
file(GLOB sh_files_scripts "project/scripts/*.sh")
list(APPEND sh_files_data ${sh_files_scripts})
message(STATUS "5. List .sh files in both project/scripts and project/data:")
message(STATUS "${sh_files_data}")

# Combine .jpg and .png file lists
file(GLOB jpg_files "project/images/*.jpg")
file(GLOB png_files "project/images/*.png")
list(APPEND image_files ${jpg_files} ${png_files})
message(STATUS "6. List .jpg and .png files in project/images:")
message(STATUS "${image_files}")


# List all .txt files in project and its subdirectories using `file(GLOB_RECURSE)`
file(GLOB_RECURSE txt_files_recursive "project/**/*.txt")
message(STATUS "7. List all .txt files in project and its subdirectories:")
message(STATUS "${txt_files_recursive}")

# Clean up (optional)
file(REMOVE_RECURSE "project")
##################################33 CMake Practice








#target_include_directories(dyna PUBLIC ${_BUILD_INCLUDE_DIR})
# Executable
file(GLOB CPP_SOURCES "${_BUILD_SRC_DIR}/*.cpp")
message(STATUS "${_TEST_FAIL}[_TEST_FAIL]  CPP_SOURCES  :  ${CPP_SOURCES}${_RESET}")
add_executable(${_CURRENT_DIR_NAME} ${CPP_SOURCES})              # (2) compiler:
message(STATUS "${_TEST_PASS}[_TEST_PASS]  _CURRENT_DIR_NAME = ${_CURRENT_DIR_NAME}${_RESET}")
#target_include_directories(${_CURRENT_DIR_NAME} PRIVATE ${_BUILD_INCLUDE_DIR})
###############################################################
# configuration (C++20 Standard)
###############################################################
# Set the C++ Standard for the project. 
# If the CMake version is greater than 3.12, it will enforce the C++20 standard.
if (CMAKE_VERSION VERSION_GREATER 3.12)
    set_property(TARGET ${_CURRENT_DIR_NAME} PROPERTY CXX_STANDARD ${_CXX_STANDARD_REQUIRED})
endif()































###############################################################
# Project Compilation (Build, Public)
###############################################################
# (3-1) linker: Link internal libraries to executable
target_link_libraries(${_CURRENT_DIR_NAME} PRIVATE ${_BUILD_STATIC_TARGETS} ${_BUILD_DYNAMIC_TARGETS})

# # (3-2) linker: Link external libraries to executable (static)
# file(GLOB _STATIC_LIB_FOUND "${_BUILD_LIB_DIR}/*.a")
# target_link_libraries(${_CURRENT_DIR_NAME} PRIVATE ${_BUILD_STATIC_TARGETS} ${_STATIC_LIB_FOUND})
# install(FILES ${_STATIC_LIB_FOUND} DESTINATION lib)

# # (3-3) linker: Link external libraries to executable (dynamic)
# file(GLOB _DLL_IMPORT_FOUND "${_BUILD_LIB_DIR}/*.dll.a")
# file(GLOB _DLL_FOUND "${_BUILD_LIB_DIR}/*.dll")
# target_link_libraries(${_CURRENT_DIR_NAME} PRIVATE ${_BUILD_STATIC_TARGETS} ${_DLL_IMPORT_FOUND})
# install(FILES ${_DLL_IMPORT_FOUND} DESTINATION lib)# Install all .dll.a files
# install(FILES ${_DLL_FOUND} DESTINATION bin)        # Find all DLL files in the build library directory
# message(STATUS "${_TEST_PASS}[_TEST_PASS]  _DLL_IMPORT_FOUND = ${_DLL_IMPORT_FOUND}${_RESET}")
# message(STATUS "${_TEST_PASS}[_TEST_PASS]  _DLL_FOUND = ${_DLL_FOUND}${_RESET}")






# set(CMAKE_LIBRARY_PATH "${_BUILD_LIB_DIR}")
# message(STATUS "${_DEBUG_USR}[_DEBUG_USR]  CMAKE_LIBRARY_PATH  :  ${CMAKE_LIBRARY_PATH}${_RESET}")

# # Prioritize static libraries
# set(CMAKE_FIND_LIBRARY_SUFFIXES .a;.lib;.so;.dll)   # static force
# set(CMAKE_FIND_LIBRARY_SUFFIXES .so;.dll.a;.a;.lib) # dynamic force
# find_library(MY_LIBRARY NAMES libdyna)
# target_link_libraries(${_CURRENT_DIR_NAME} PRIVATE ${_BUILD_STATIC_TARGETS} ${MY_LIBRARY})
# message(STATUS "${_TEST_PASS}[_TEST_PASS]  MY_LIBRARY = ${MY_LIBRARY}${_RESET}")
# message(STATUS "${_TEST_PASS}[_TEST_PASS]  CMAKE_FIND_LIBRARY_SUFFIXES = ${CMAKE_FIND_LIBRARY_SUFFIXES}${_RESET}")







###############################################################
# TODO: Add tests and install targets if needed.
###############################################################
# 
# 









###############################################################
# CMake Installation (Library Distribution)
###############################################################
# Set custom installation directories
set(_INSTALL_INCLUDE_DIR "include")
set(_INSTALL_INCLUDE_DIR_ABS "${CMAKE_INSTALL_PREFIX}/${_INSTALL_INCLUDE_DIR}")
set(_INSTALL_LIB_DIR "lib")
set(_INSTALL_LIB_DIR_ABS "${CMAKE_INSTALL_PREFIX}/${_INSTALL_LIB_DIR}")
set(_INSTALL_BIN_DIR "bin")
set(_INSTALL_BIN_DIR_ABS "${CMAKE_INSTALL_PREFIX}/${_INSTALL_BIN_DIR}")
set(_INSTALL_EXPORT_DIR "lib/cmake/${_PROJECT_NAME}")
set(_INSTALL_EXPORT_DIR_ABS "${CMAKE_INSTALL_PREFIX}/${_INSTALL_EXPORT_DIR}")
set(_INSTALL_CMAKE_FILE_NAME "${_PROJECT_NAME}Targets.cmake")
set(_INSTALL_CMAKE_FILE_NAME_ABS "${_INSTALL_EXPORT_DIR_ABS}/${_INSTALL_CMAKE_FILE_NAME}")
message(STATUS "*****************************************")
message(STATUS "-_INSTALL_INCLUDE_DIR_ABS-: ${_INSTALL_INCLUDE_DIR_ABS}")
message(STATUS "-_INSTALL_LIB_DIR_ABS-: ${_INSTALL_LIB_DIR_ABS}")
message(STATUS "-_INSTALL_BIN_DIR_ABS-: ${_INSTALL_BIN_DIR_ABS}")
message(STATUS "-_INSTALL_EXPORT_DIR_ABS-: ${_INSTALL_EXPORT_DIR_ABS}")
message(STATUS "-_INSTALL_CMAKE_FILE_NAME_ABS-: ${_INSTALL_CMAKE_FILE_NAME_ABS}")
message(STATUS "*****************************************")
set(_INSTALL_EXPORTED_TARGETS "targets")          # based on `CMAKE_CURRENT_BINARY_DIR`
# (2) compiled/linked targets: Install targets (static, dynamic, and executable) and the export file
# (2-1) executable
# [Use-case: to GET a `entry-point`]
install(TARGETS ${_PROJECT_NAME}
    EXPORT ${_INSTALL_EXPORTED_TARGETS}
    RUNTIME DESTINATION ${_INSTALL_BIN_DIR} # For executable        (.exe)
)
# (2-2) static
# [Use-case: to GET `foundation`, e.g. sysArch, domain-specific DSA]
install(TARGETS ${_BUILD_STATIC_TARGETS}
    EXPORT ${_INSTALL_EXPORTED_TARGETS}
    ARCHIVE DESTINATION ${_INSTALL_LIB_DIR} # For static libraries  (.a/.lib)
)
# (2-3) dynamic
# [Use-case: to UPDATE/DELETE `libraries` for the foundation, e.g. utility DSA, networking, security]
install(TARGETS ${_BUILD_DYNAMIC_TARGETS}
    EXPORT ${_INSTALL_EXPORTED_TARGETS}
    LIBRARY DESTINATION ${_INSTALL_LIB_DIR} # For shared libraries + import lib (.so/.dll + .dll.a)
)
# [Use-case: to POST a `framework` for distribution, ]
install(TARGETS ${_BUILD_DYNASTATIC_TARGETS}
    EXPORT ${_INSTALL_EXPORTED_TARGETS}     # (special) As a package release to other system.
    ARCHIVE DESTINATION ${_INSTALL_LIB_DIR} # For static linking from dynamic (.a/.lib)
)
# (1) preprocessed targets: Install the header files
install(DIRECTORY ${_BUILD_INCLUDE_DIR}/           # The directory containing the header files
    DESTINATION ${_INSTALL_INCLUDE_DIR}     # Install to the include directory ${_INSTALL_INCLUDE_DIR_ABS}
)
# (3) expoted targets: targets as `${_PROJECT_NAME}::_TARGETS` in `.cmake`
install(EXPORT ${_INSTALL_EXPORTED_TARGETS} # Export the targets for reuse
    FILE ${_INSTALL_CMAKE_FILE_NAME}        # The export file
    NAMESPACE ${_PROJECT_NAME}::             # Namespace for the targets
    DESTINATION ${_INSTALL_EXPORT_DIR}      # Install location for the export file
)









###############################################################
# Project Packaging with CPack (Standalone Distribution)
###############################################################
# CPack allows for easy packaging and distribution of the project.
# It integrates with the CMake installation process and generates
# packages in various formats (e.g., ZIP, TGZ, DEB, RPM, etc.).

# Set the installation prefix to ensure correct path usage
set(CPACK_OUTPUT_CONFIG_FILE "${CMAKE_CURRENT_BINARY_DIR}/CPackConfig.cmake") 
# Set the output config file for CPack
set(CPACK_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")
# Specify the generator for package formats (e.g., ZIP, TGZ, DEB, RPM)
set(_CPACK_GENERATOR_WIN "NSIS;ZIP;TGZ")
set(_CPACK_GENERATOR_OSX "NSIS;ZIP;TGZ")
set(_CPACK_GENERATOR_LINUX "NSIS;ZIP;TGZ")
set(CPACK_GENERATOR "${_CPACK_GENERATOR_WIN}")
# set(CPACK_GENERATOR "ZIP;TGZ")
# specify the output destination directory for the generated packages
set(CPACK_OUTPUT_FILE_PREFIX "${CMACK_OUTPUT_FILE_PREFIX}")
# project meta-data
set(CPACK_PACKAGE_NAME "${_PROJECT_NAME}")
set(CPACK_PACKAGE_CONTACT "${_PROJECT_CONTACT}")
set(CPACK_PACKAGE_VERSION "${_PROJECT_VERSION}")
set(CPACK_PACKAGE_VENDOR "Georgia Institute of Technology")
set(CPACK_PACKAGE_DESCRIPTION_SUMMARY "${_PROJECT_DESCRIPTION_SUMMARY}")
set(CPACK_RESOURCE_FILE_LICENSE "${PROJECT_SOURCE_DIR}/LICENSE")
set(CPACK_RESOURCE_FILE_README "${PROJECT_SOURCE_DIR}/README.md")
# # Include the CPack variables
include(CPack)
message(STATUS "**************** CPack *****************")
message(STATUS "-CMAKE_COMMAND-: ${CMAKE_COMMAND}")
message(STATUS "-CMAKE_BINARY_DIR-: ${CMAKE_BINARY_DIR}")
message(STATUS "-CMAKE_SOURCE_DIR-: ${CMAKE_SOURCE_DIR}")
message(STATUS "****************************************")
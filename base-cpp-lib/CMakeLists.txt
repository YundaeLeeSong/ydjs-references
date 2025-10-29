# my_project/CMakeLists.txt

cmake_minimum_required(VERSION 3.15)
project(my_project VERSION 1.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# -----------------------------------------------------------------
# --- Set Custom Output Directories (User Request) ---
#
# ${CMAKE_BINARY_DIR} is the 'build' directory.
#
# NOTE: Visual Studio (a "multi-configuration generator")
# will still add a /Debug or /Release sub-directory.
# e.g., build/bin/Debug/my_app.exe
# -----------------------------------------------------------------
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)  # .exe, .dll
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)  # .lib (import lib)
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)  # .lib (static), .a

# -----------------------------------------------------------------
# --- Add All Sub-Projects ---
# -----------------------------------------------------------------

# Add our libraries
add_subdirectory(src/libcore)
add_subdirectory(src/libcount)

# Add our main application (which depends on the libraries)
add_subdirectory(src/app)

# Enable testing
enable_testing()

# Add tests (only if building tests)
option(BUILD_TESTS "Build tests" ON)
if(BUILD_TESTS)
    add_subdirectory(tests)
endif()




message(STATUS "CMAKE_SOURCE_DIR=${CMAKE_SOURCE_DIR}")
message(STATUS "CMAKE_CURRENT_SOURCE_DIR=${CMAKE_CURRENT_SOURCE_DIR}")
message(STATUS "CMAKE_CURRENT_LIST_DIR=${CMAKE_CURRENT_LIST_DIR}")
message(STATUS "PROJECT_SOURCE_DIR=${PROJECT_SOURCE_DIR}")



# --- Add Install Rules ---
#

# Install the library target
install(TARGETS libcore
    # ARCHIVE = The static .lib file (or .a on Linux)
    # DESTINATION lib = Install it to the 'lib' directory
    ARCHIVE DESTINATION lib
)
# Install the library target
install(TARGETS libcount
    # RUNTIME = The .dll file (or .so on Linux)
    # DESTINATION bin = Install it to the 'bin' directory,
    #                   alongside the executables.
    RUNTIME DESTINATION bin

    # # LIBRARY = The .lib import library (or .so on Linux)
    # # DESTINATION lib = Install it to the 'lib' directory.
    # LIBRARY DESTINATION lib

    # # ARCHIVE = (Only relevant for static builds, but good to include)
    # ARCHIVE DESTINATION lib
)
# --- Add Install Rules ---
#
# Install the executable target
install(TARGETS my_app
    # RUNTIME = The .exe file
    # DESTINATION bin = Install it to the 'bin' directory.
    RUNTIME DESTINATION bin
)
# Install the public header files
install(DIRECTORY 
    ${PROJECT_SOURCE_DIR}/include/
    DESTINATION include
    FILES_MATCHING 
    PATTERN "*.h"
)
# Install the fmt DLLs from vcpkg
install(DIRECTORY 
    ${CMAKE_CURRENT_BINARY_DIR}/vcpkg_installed/x64-windows/bin/
    DESTINATION bin
    FILES_MATCHING 
    PATTERN "fmt*.dll"
)









# -----------------------------------------------------------------
# --- CPack Packaging Configuration ---
# -----------------------------------------------------------------
# Set a default version from the project() command
set(CPACK_PACKAGE_VERSION_MAJOR ${PROJECT_VERSION_MAJOR})
set(CPACK_PACKAGE_VERSION_MINOR ${PROJECT_VERSION_MINOR})
set(CPACK_PACKAGE_VERSION_PATCH ${PROJECT_VERSION_PATCH})

# Set the package name
set(CPACK_PACKAGE_NAME "${PROJECT_NAME}")
set(CPACK_PACKAGE_DESCRIPTION_SUMMARY "My Cool C++ Project")

# Set the generator. 'ZIP' creates a simple .zip file.
# 'NSIS' would create a Windows installer .exe.
set(CPACK_GENERATOR "ZIP;NSIS")

# Tell CPack to put the final .zip file (or .exe installer, etc.)
# into a 'dist' directory at the project's root.
# ${CMAKE_SOURCE_DIR} is the variable for 'my_project/'
set(CPACK_PACKAGE_DIRECTORY "${CMAKE_SOURCE_DIR}/dist")

# Include the CPack module to make it all work
include(CPack)
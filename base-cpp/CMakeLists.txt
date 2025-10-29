# CMakeLists.txt

cmake_minimum_required(VERSION 3.18)
project(SimpleProject CXX)

# Qt 5 works great with C++14
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# --- Qt Specific Configuration ---
# This block is required for Qt to work.
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTORCC ON)

# --- vcpkg Integration (Find *both* packages) ---

# 1. Find {fmt} (this is unchanged)
find_package(fmt CONFIG REQUIRED)

# 2. Find Qt5 (this is the main change)
#    We look for version 5.15 (a common vcpkg version)
#    and the same components.
# find_package(Qt5 5.15 COMPONENTS Core Widgets REQUIRED)
find_package(Qt5 COMPONENTS Core Widgets REQUIRED)

# Link libraries (Qt via vcpkg export will provide targets like Qt5::Widgets;
# fmt from vcpkg provides fmt::fmt)


# --- Project Setup ---

# Add our executable (this is unchanged)
add_executable(qt_vcpkg_demo
    src/main.cpp
)

# --- Link the Libraries ---

# We link the Qt5 targets, which are named slightly
# differently (Qt5::Core vs Qt::Core)
target_link_libraries(qt_vcpkg_demo
    PRIVATE
    fmt::fmt        # Link the fmt library
    Qt5::Core       # Link the Qt 5 Core library
    Qt5::Widgets    # Link the Qt 5 Widgets library
)











# -----------------------------------------------------------------
# --- 4. Define the "Staging" (Install) Step ---
# -----------------------------------------------------------------
# This is the "preparation" for the distro.

# 4a. Install the main .exe
install(
    TARGETS qt_vcpkg_demo
    RUNTIME DESTINATION bin  # Copies .exe to "install/bin"
)

# 4b. Install Qt5 DLLs and dependencies from vcpkg
#     This ensures all Qt dependencies are included in the distribution
install(DIRECTORY 
    "${CMAKE_CURRENT_BINARY_DIR}/vcpkg_installed/x64-windows/bin/"
    DESTINATION bin
    FILES_MATCHING 
    PATTERN "Qt5*.dll"
    PATTERN "*.dll"
)

# 4c. Install Qt5 plugins
install(DIRECTORY 
    "${CMAKE_CURRENT_BINARY_DIR}/vcpkg_installed/x64-windows/plugins/"
    DESTINATION bin/plugins
)

# 4d. Install additional dependencies (fmt, etc.)
install(DIRECTORY 
    "${CMAKE_CURRENT_BINARY_DIR}/vcpkg_installed/x64-windows/bin/"
    DESTINATION bin
    FILES_MATCHING 
    PATTERN "fmt*.dll"
    PATTERN "*.dll"
    EXCLUDE PATTERN "Qt5*.dll"  # Already installed above
)

# 4e. Create qt.conf to help Qt find its plugins
install(FILES 
    "${CMAKE_CURRENT_BINARY_DIR}/Release/qt.conf"
    DESTINATION bin
    OPTIONAL
)

# -----------------------------------------------------------------
# --- 5. Define the "Distribution" (CPack) Step ---
# -----------------------------------------------------------------
set(CPACK_PACKAGE_NAME "SimpleQtDemo")
set(CPACK_PACKAGE_VERSION "0.1.0")

# Detect available installer tools
set(CPACK_GENERATOR "ZIP;TGZ")

# Check for NSIS
find_program(NSIS_EXECUTABLE makensis)
if(NSIS_EXECUTABLE)
    set(CPACK_GENERATOR "NSIS;${CPACK_GENERATOR}")
    message(STATUS "NSIS found: ${NSIS_EXECUTABLE}")
endif()

# Check for other common installers
find_program(INNO_SETUP_EXECUTABLE iscc)
if(INNO_SETUP_EXECUTABLE)
    set(CPACK_GENERATOR "INNO;${CPACK_GENERATOR}")
    message(STATUS "Inno Setup found: ${INNO_SETUP_EXECUTABLE}")
endif()

# Configure CPack to output to dist/ directory
set(CPACK_PACKAGE_DIRECTORY "${CMAKE_SOURCE_DIR}/dist")

# Set the install prefix for packaging
set(CPACK_SET_DESTDIR TRUE)
set(CPACK_INSTALL_PREFIX "")

# NSIS specific settings
if(NSIS_EXECUTABLE)
    set(CPACK_NSIS_DISPLAY_NAME "SimpleQtDemo")
    set(CPACK_NSIS_PACKAGE_NAME "SimpleQtDemo")
    set(CPACK_NSIS_CONTACT "your-email@example.com")
    set(CPACK_NSIS_MODIFY_PATH ON)
    set(CPACK_RESOURCE_FILE_LICENSE "${PROJECT_SOURCE_DIR}/LICENSE")
endif()

include(CPack)
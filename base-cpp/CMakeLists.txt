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
find_package(Qt5 5.15 COMPONENTS Core Widgets REQUIRED)

# --- Project Setup ---

# Add our executable (this is unchanged)
add_executable(
    my_app
    src/main.cpp
)

# --- Link the Libraries ---

# We link the Qt5 targets, which are named slightly
# differently (Qt5::Core vs Qt::Core)
target_link_libraries(
    my_app
    PRIVATE
    fmt::fmt        # Link the fmt library
    Qt5::Core       # Link the Qt 5 Core library
    Qt5::Widgets    # Link the Qt 5 Widgets library
)

# -----------------------------------------------------------------
# --- "windeployqt" Automatic Deployment (Explicit Path Fix) ---
# -----------------------------------------------------------------

# 1. Get the directory where 'Qt5Config.cmake' was found
#    (e.g., .../build/vcpkg_installed/x64-windows/share/qt5)
get_filename_component(QT5_CONFIG_DIR "${Qt5_DIR}" DIRECTORY)

# 2. Find the 'windeployqt' tool. We know it lives in a
#    'tools/qt5/bin' directory relative to the vcpkg install.
#    We provide this path as a HINT.
find_program(
    WINDEPLOYQT_EXECUTABLE windeployqt
    HINTS "${QT5_CONFIG_DIR}/../../tools/qt5/bin"
    REQUIRED
)
# This will find the full, absolute path to windeployqt.exe

# 3. Add the post-build command, using the full path
add_custom_command(
    TARGET my_app POST_BUILD
    
    # This now uses the full path, e.g., C:/.../windeployqt.exe
    COMMAND ${WINDEPLOYQT_EXECUTABLE}
    
    ARGS "$<TARGET_FILE:my_app>"
    WORKING_DIRECTORY "$<TARGET_FILE_DIR:my_app>"
    COMMENT "Running windeployqt to deploy dependencies..."
)
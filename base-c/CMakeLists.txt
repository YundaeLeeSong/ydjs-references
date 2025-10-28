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
# --- The Modern "Install" Workflow ---
# -----------------------------------------------------------------
#
# This single, standard CMake command is all you need.
#
# 1. It tells CMake to install 'my_app.exe' to 'bin'.
# 2. The vcpkg toolchain automatically detects this and
#    *also* installs the required dependency DLLs
#    (like Qt5Core.dll) to the same 'bin' directory.
#
install(
    TARGETS my_app
    RUNTIME DESTINATION bin  # Copies the .exe
)
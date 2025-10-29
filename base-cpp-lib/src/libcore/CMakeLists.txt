# src/libcore/CMakeLists.txt

# This creates the 'libcore.lib' static library
add_library(libcore STATIC
    static_lib.cpp
)

# Tell this target (and any consumer) where to find its
# public headers. ${CMAKE_SOURCE_DIR} is the root of my_project.
target_include_directories(libcore
  PUBLIC
    ${CMAKE_SOURCE_DIR}/include
)

# Set target properties for installation
set_target_properties(libcore PROPERTIES
    EXPORT_NAME core
    VERSION ${PROJECT_VERSION}
    SOVERSION ${PROJECT_VERSION_MAJOR}
)
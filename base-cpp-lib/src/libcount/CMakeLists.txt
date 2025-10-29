# src/libcount/CMakeLists.txt

# Find the 'fmt' dependency (provided by vcpkg)
find_package(fmt CONFIG REQUIRED)

# This creates the 'libcount.dll' and 'libcount.lib' (import lib)
add_library(libcount SHARED
    dynamic_lib.cpp
)

# Public include path
target_include_directories(libcount
  PUBLIC
    ${CMAKE_SOURCE_DIR}/include
)

# Add the export macro, just as before
target_compile_definitions(libcount
  PRIVATE
    MY_DYNAMIC_LIB_EXPORTS
)

# Link to fmt
target_link_libraries(libcount
  PUBLIC
    fmt::fmt
)
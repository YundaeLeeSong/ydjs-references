# tests/CMakeLists.txt

# Find the GoogleTest package
find_package(GTest CONFIG REQUIRED)

# Create the test executable
add_executable(tests
    tests.cpp
)

# Set the include directories for the test executable
target_include_directories(tests
    PRIVATE
        ${CMAKE_SOURCE_DIR}/include
)

# Link the test executable with the libraries we want to test
target_link_libraries(tests
    PRIVATE
        libcore
        libcount
        GTest::gtest
        GTest::gtest_main
)

# Enable CTest integration
enable_testing()

# Add the test to CTest
add_test(NAME StaticLibTest COMMAND tests --gtest_filter=StaticLibTest.*)
add_test(NAME DynamicLibTest COMMAND tests --gtest_filter=DynamicLibTest.*)

# Set test properties for better output
set_tests_properties(StaticLibTest PROPERTIES
    TIMEOUT 30
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
)

set_tests_properties(DynamicLibTest PROPERTIES
    TIMEOUT 30
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
)
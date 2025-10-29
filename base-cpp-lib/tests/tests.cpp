// my_project/tests/tests.cpp

#include <gtest/gtest.h>

// Include the headers for the code we want to test
#include <my_project/static_lib.h>
#include <my_project/dynamic_lib.h>

// Test Fixture for the static library
TEST(StaticLibTest, Greeting) {
    std::string result = get_static_greeting();
    // Check that the static library returns the correct string
    EXPECT_EQ(result, "Saying hi from static!");
}

// Test Fixture for the dynamic library
TEST(DynamicLibTest, State) {
    // Create an instance of our class
    DynamicGreeter greeter;

    // Check the stateful greeting three times
    EXPECT_EQ(greeter.get_greeting(), "Saying hi with state #1 from dynamic!");
    EXPECT_EQ(greeter.get_greeting(), "Saying hi with state #2 from dynamic!");
    EXPECT_EQ(greeter.get_greeting(), "Saying hi with state #3 from dynamic!");
}

// You can add more TEST(...) blocks here
// src/libcount/dynamic_lib.cpp



// CRITICAL: This define tells the header (dynamic_lib.h)
// that we are *building* the DLL, so it should use __declspec(dllexport).
// #define MY_DYNAMIC_LIB_EXPORTS





#include <my_project/dynamic_lib.h>

// This include comes from vcpkg (and is found via find_package)
#include <fmt/core.h>

// Constructor
DynamicGreeter::DynamicGreeter() : m_counter(0) {
    // m_counter is initialized to 0
}

// Method implementation
std::string DynamicGreeter::get_greeting() {
    // Increment the internal state
    m_counter++;
    
    // Use the vcpkg 'fmt' library to format our string
    return fmt::format("Saying hi with state #{} from dynamic!", m_counter);
}
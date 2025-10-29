// include/my_project/dynamic_lib.h
#pragma once
#include <string>

// --- Windows DLL Import/Export Boilerplate ---
// This is necessary for dynamic libraries on Windows.
#ifdef _WIN32
  // We are building this library (i.e., this is dynamic_lib.cpp)
  #ifdef MY_DYNAMIC_LIB_EXPORTS
    #define MY_DYNAMIC_LIB_API __declspec(dllexport)
  // We are using this library (i.e., this is main.cpp)
  #else
    #define MY_DYNAMIC_LIB_API __declspec(dllimport)
  #endif
#else
  // Not needed on Linux/macOS
  #define MY_DYNAMIC_LIB_API
#endif
// --- End of Boilerplate ---

/**
 * @brief A class with state, exported from a dynamic library.
 * The MY_DYNAMIC_LIB_API macro marks this class for export.
 */
class MY_DYNAMIC_LIB_API DynamicGreeter {
public:
    DynamicGreeter();

    /**
     * @brief Returns a greeting with an incrementing state counter.
     */
    std::string get_greeting();

private:
    // This state is stored within the .dll/.so
    int m_counter;
};
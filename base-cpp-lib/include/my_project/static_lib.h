// include/my_project/static_lib.h
#pragma once
#include <string>

/**
 * @brief Provides a greeting from the static library.
 * The code for this will be compiled *into* the final executable.
 */
std::string get_static_greeting();
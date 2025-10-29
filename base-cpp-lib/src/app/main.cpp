// src/main.cpp
#include <my_project/static_lib.h>
#include <my_project/dynamic_lib.h>

#include <iostream>

int main() {
    // 1. Call the static library function.
    // This code is compiled directly into my_app.exe
    std::cout << get_static_greeting() << std::endl;
    
    std::cout << "---" << std::endl;
    
    // 2. Use the dynamic library class.
    // This code is loaded at runtime from my_dynamic_lib.dll
    DynamicGreeter greeter;
    
    // Call it multiple times to see the state change
    std::cout << greeter.get_greeting() << std::endl;
    std::cout << greeter.get_greeting() << std::endl;
    std::cout << greeter.get_greeting() << std::endl;
    
    return 0;
}
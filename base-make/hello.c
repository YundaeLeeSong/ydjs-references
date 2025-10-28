/*
 * hello.c
 *
 * This is a minimal C program. Its only purpose is
 * to be compiled by 'make' to verify the build
 * process is working.
 * 
 * Usage:
 * 1. make
 * 2. ./hello   (on Unix-like systems)
 *    hello.exe (on Windows)
 * 3. make clean
 */

// Include the standard I/O header for the printf function
#include <stdio.h>

// The main entry point for the program
int main() {
    
    // Print a success message to the console
    printf("Hello, Make! The build was successful.\n");
    
    // Return 0 to indicate successful execution
    return 0;
}
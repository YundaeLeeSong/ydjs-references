/*
 * This program demonstrates how to read and use
 * "command-line arguments" passed to the main function.
 * Command Usages:
 *   1. gcc main.c -o candy
 *   2. ./candy 
 *   3. ./candy arg1 arg2 arg3
 *   4. rm -rf *.exe
 */
#include <stdio.h> // "ST"an"D"erd "I"nput "O"utput's (.) "H"eader


int main(int argc, char *argv[]) {

    // Print the total number of arguments (program name + user args)
    // 'argc' stands for "argument count"
    printf("Total arguments passed: %d\n", argc);

    // Print the name of the program itself
    // This is always stored in argv[0]
    // 'argv' stands for "argument vector"
    printf("Program name: %s\n", argv[0]);
    printf("------------------------------\n");
    printf("Arguments received:\n");
    printf("index 1: %s\n", argv[1]);
    // printf("index 2: %s\n", argv[2]);
    // printf("index 3: %s\n", argv[3]);
    printf("------------------------------\n");
    for (int i = 1; i < argc; i++) {
        printf("Argument %d: %s\n", i, argv[i]);
    }

    // int i = 0;
    // while (i < 5) {
    //     printf("Hello %d\n", i);
    //     i = i+1;
    // }



    for(int i = 0; i < 5; i += 2){
        // even numbers only
        printf("Hello %d\n", i);
    }


    // for (int i = 0; i < 3; i++) {
    //     printf("arr[%d]: %d\n", i, arr[i]);
    // }

    // ./jihoo_python.exe main.py
    // [./jihoo_python.exe, main.py]
    // [./jihoo_python.exe, main.py, hi.py]
    // Array (Vector): [main.py, ..., hi.py]


    // [6, 1, -4] = 
    // 0th index: 6
    // 1st index: 1
    // 2nd index: -4
    // [argv[1], argv[2], argv[3]] = [6, 1, -4]
    // []


    





    int a = 10;
    int b = 5;
    int sum = a + b;
    printf("Sum: %d\n", sum);
    printf("Hello, C World!\n");
    printf("Let's look at our variables.\n");
    // wait input to exit (prompt needed)
    printf("Press Enter to exit..."); scanf("%*c");
    return 0;
}


// The gcc command is used for compiling C programs 
// because GCC, or the {GNU Compiler Collection}, 
// is the standard and widely used compiler for the 
// C programming language (among others like C++, Objective-C, Fortran, etc.).
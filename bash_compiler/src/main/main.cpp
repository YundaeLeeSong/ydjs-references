#include "bash_compiler.h"
#include "fibonacci.h"
#include "static_lib.h"
#include "dynamic_lib.h"

int main() {
    // Your code here
    sayHello();
    display_fibonacci(10);




    staticFunction();
    dynamicFunction();



    printf("Press any key to continue...\n");
    getchar(); // no dynamic memory allocation
    return 0;
}

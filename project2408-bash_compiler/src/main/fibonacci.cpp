#include <stdio.h>

void display_fibonacci(int n) {
    int t1 = 0, t2 = 1, nextTerm;

    printf("Fibonacci Sequence: %d, %d", t1, t2);

    for (int i = 3; i <= n; ++i) {
        nextTerm = t1 + t2;
        printf(", %d", nextTerm);
        t1 = t2;
        t2 = nextTerm;
    }
    printf("\n");
}

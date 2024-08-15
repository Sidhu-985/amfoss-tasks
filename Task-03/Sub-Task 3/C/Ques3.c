#include <stdio.h>

int main() {
    int n = 5;

    for (int i = 1; i <= n; i += 2) {
        for (int j = 0; j < (n - i) / 2; j++) {
            printf(" ");
        }
        for (int k = 0; k < i; k++) {
            printf("*");
        }
        printf("\n");
    }

    for (int i = n - 2; i > 0; i -= 2) {
        for (int j = 0; j < (n - i) / 2; j++) {
            printf(" ");
        }
        for (int k = 0; k < i; k++) {
            printf("*");
        }
        printf("\n");
    }

    return 0;
}

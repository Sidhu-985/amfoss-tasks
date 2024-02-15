#include <stdio.h>

int main() {
    int n,i,j,flag;
    printf("Enter the number: ");
    scanf("%d", &n);

    if (n <= 1) {
        printf("%d is not a prime number\n", n);
    } else {
        for (i = 2; i <= n; i++) {
            flag = 0;
            for (j = 2; j <= sqrt(i); j++) {
                if (i % j == 0) {
                    flag = 1;
                    break;
                }
            }
            if (flag == 0) {
                printf("%d is a prime number\n", i);
            }
        }
    }

    return 0;
}

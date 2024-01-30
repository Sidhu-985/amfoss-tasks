#include <stdio.h>
#include <math.h>

int main() {
    int n;
    printf("Enter a value for n: ");
    scanf("%d", &n);

    if (n <= 1) {
        printf("%d is not a prime number\n", n);
    } else {
        for (int i = 2; i <= n; i++) {
            int flag = 0;
            for (int j = 2; j <= sqrt(i); j++) {
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

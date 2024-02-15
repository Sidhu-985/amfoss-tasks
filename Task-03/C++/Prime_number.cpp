#include <iostream>

int main() {
    int n;
    std::cout << "Enter a value for n: ";
    std::cin >> n;

    if (n <= 1) {
        std::cout << n << " is not a prime number" << std::endl;
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
                std::cout << i << " is a prime number" << std::endl;
            }
        }
    }

    return 0;
}

#include <iostream>
#include <fstream>
#include <string>

void generateDiamond(int n, std::ofstream &outputFile) {
    for (int i = 1; i <= n; i += 2) {
        for (int j = 0; j < (n - i) / 2; j++) {
            outputFile << " ";
        }
        for (int k = 0; k < i; k++) {
            outputFile << "*";
        }
        outputFile << "\n";
    }
    for (int i = n - 2; i > 0; i -= 2) {
        for (int j = 0; j < (n - i) / 2; j++) {
            outputFile << " ";
        }
        for (int k = 0; k < i; k++) {
            outputFile << "*";
        }
        outputFile << "\n";
    }
}

int main() {
    int n;
    std::ifstream inputFile("input.txt");
    if (!inputFile) {
        std::cerr << "Error opening input.txt\n";
        return 1;
    }
    inputFile >> n;
    inputFile.close();

    std::ofstream outputFile("output.txt");
    if (!outputFile) {
        std::cerr << "Error opening output.txt\n";
        return 1;
    }
    generateDiamond(n, outputFile);
    outputFile.close();

    std::cout << "Diamond pattern written to output.txt\n";
    return 0;
}

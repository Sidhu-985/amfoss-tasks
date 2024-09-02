#include <stdio.h>

void generateDiamond(int n, FILE *outputFile) {
    for (int i = 1; i <= n; i += 2) {
        for (int j = 0; j < (n - i) / 2; j++) {
            fprintf(outputFile, " ");
        }
        for (int k = 0; k < i; k++) {
            fprintf(outputFile, "*");
        }
        fprintf(outputFile, "\n");
    }
    for (int i = n - 2; i > 0; i -= 2) {
        for (int j = 0; j < (n - i) / 2; j++) {
            fprintf(outputFile, " ");
        }
        for (int k = 0; k < i; k++) {
            fprintf(outputFile, "*");
        }
        fprintf(outputFile, "\n");
    }
}

int main() {
    int n;
    FILE *inputFile = fopen("input.txt", "r");
    if (inputFile == NULL) {
        printf("Error opening input.txt\n");
        return 1;
    }
    fscanf(inputFile, "%d", &n);
    fclose(inputFile);

    FILE *outputFile = fopen("output.txt", "w");
    if (outputFile == NULL) {
        printf("Error opening output.txt\n");
        return 1;
    }
    generateDiamond(n, outputFile);
    fclose(outputFile);

    printf("Diamond pattern written to output.txt\n");
    return 0;
}

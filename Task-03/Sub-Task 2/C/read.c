#include <stdio.h>

int main() {
    char buffer[1024];
    FILE *infile = fopen("input.txt", "r");
    FILE *outfile = fopen("output.txt", "w");

    if (infile && outfile) {
        while (fgets(buffer, sizeof(buffer), infile)) {
            fputs(buffer, outfile);
        }
    }

    fclose(infile);
    fclose(outfile);
    return 0;
}

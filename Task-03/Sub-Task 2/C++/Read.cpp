#include <fstream>
#include <string>

int main() {
    std::ifstream infile("input.txt");
    std::ofstream outfile("output.txt");

    std::string content((std::istreambuf_iterator<char>(infile)), std::istreambuf_iterator<char>());
    outfile << content;

    return 0;
}

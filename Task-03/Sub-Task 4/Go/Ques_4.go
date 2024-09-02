package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func generateDiamond(n int, writer *bufio.Writer) {
	for i := 1; i <= n; i += 2 {
		for j := 0; j < (n-i)/2; j++ {
			writer.WriteString(" ")
		}
		for k := 0; k < i; k++ {
			writer.WriteString("*")
		}
		writer.WriteString("\n")
	}
	for i := n - 2; i > 0; i -= 2 {
		for j := 0; j < (n-i)/2; j++ {
			writer.WriteString(" ")
		}
		for k := 0; k < i; k++ {
			writer.WriteString("*")
		}
		writer.WriteString("\n")
	}
}

func main() {
	inputFile, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Error opening input.txt:", err)
		return
	}
	defer inputFile.Close()

	var n int
	scanner := bufio.NewScanner(inputFile)
	if scanner.Scan() {
		n, err = strconv.Atoi(scanner.Text())
		if err != nil {
			fmt.Println("Error converting input to integer:", err)
			return
		}
	}

	outputFile, err := os.Create("output.txt")
	if err != nil {
		fmt.Println("Error opening output.txt:", err)
		return
	}
	defer outputFile.Close()

	writer := bufio.NewWriter(outputFile)

	generateDiamond(n, writer)

	writer.Flush()

	fmt.Println("Diamond pattern written to output.txt")
}

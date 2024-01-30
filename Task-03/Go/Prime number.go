package main

import (
	"fmt"
	"math"
)

func main() {
	var n int
	fmt.Print("Enter a value for n: ")

	if n <= 1 {
		fmt.Printf("%d is not a prime number\n", n)
	} else {
		for i := 2; i <= n; i++ {
			flag := 0
			for j := 2; j <= int(math.Sqrt(float64(i))); j++ {
				if i%j == 0 {
					flag = 1
					break
				}
			}
			if flag == 0 {
				fmt.Printf("%d is a prime number\n", i)
			}
		}
	}
}

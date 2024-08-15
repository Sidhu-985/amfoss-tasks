package main

import (
    "fmt"
    "strings"
)

func main() {
    n := 5

    for i := 1; i <= n; i += 2 {
        fmt.Println(strings.Repeat(" ", (n-i)/2) + strings.Repeat("*", i))
    }

    for i := n - 2; i > 0; i -= 2 {
        fmt.Println(strings.Repeat(" ", (n-i)/2) + strings.Repeat("*", i))
    }
}

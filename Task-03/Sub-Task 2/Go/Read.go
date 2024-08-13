package main

import (
    "io/ioutil"
)

func main() {
    content, _ := ioutil.ReadFile("input.txt")
    _ = ioutil.WriteFile("output.txt", content, 0644)
}

package main

import (
	"fmt"
)

func main() {
	var a, b, c int
	var s string
	fmt.Scan(&a)
	fmt.Scan(&b, &c)
	fmt.Scan(&s)
	answer := a + b + c
	fmt.Println(answer)
	fmt.Println(s)
}

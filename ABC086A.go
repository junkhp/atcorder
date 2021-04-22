package main

import (
	"fmt"
)

func main() {
	var s string
	var ans int
	fmt.Scan(&s)
	for i := 0; i < 3; i++ {
		if k := s[i : i+1]; k == "1" {
			ans++
		}
	}
	fmt.Println(ans)
}

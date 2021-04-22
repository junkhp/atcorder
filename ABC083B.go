package main

import (
	"fmt"
)

func check(n int) bool {
	var out bool
	return out
}

func getSum(n int) int {
	var outSum int
	waru := 10
	var keta int
	for {
		if n < 10 {
			outSum += n
			break
		}
		keta = n % waru
		outSum += keta
		n = (n - (n % waru)) / 10
	}
	return outSum
}

func main() {
	var n, a, b, ans int
	fmt.Scan(&n, &a, &b)
	for i := 0; i <= n; i++ {
		if sum := getSum(i); sum >= a && sum <= b {
			ans += i
		}
	}
	fmt.Println(ans)
}

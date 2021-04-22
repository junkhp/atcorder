package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

var sc = bufio.NewScanner(os.Stdin)

func nextInt() int {
	sc.Scan()
	ret, e := strconv.Atoi(sc.Text())
	if e != nil {
		panic(e)
	}
	return ret
}

func main() {
	sc.Split(bufio.ScanWords)
	n := nextInt()
	aSlice := make([]int, 0, n)
	for i := 0; i < n; i++ {
		m := nextInt()
		aSlice = append(aSlice, m)
	}
	sort.Sort(sort.Reverse(sort.IntSlice(aSlice)))
	var AlicePoint, BobPoint int
	for i, card := range aSlice {
		if i%2 == 0 {
			AlicePoint += card
		} else {
			BobPoint += card
		}
	}
	fmt.Println(AlicePoint - BobPoint)
}

package main

import (
	"bufio"
	"fmt"
	"os"
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
	var ans int
	var stopFlg bool
	for {
		for i, val := range aSlice {
			if val%2 == 0 {
				aSlice[i] = val / 2
			} else {
				stopFlg = true
				break
			}
		}
		if stopFlg {
			break
		}
		ans++
	}
	fmt.Println(ans)
}

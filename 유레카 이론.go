package main

import "fmt"

var triangleNum [1001]int

func check(num int) bool {
	for i := 1; i <= 50; i++ {
		for j := 1; j <= 50; j++ {
			for k := 1; k <= 50; k++ {
				if triangleNum[j]+triangleNum[i]+triangleNum[k] == num {
					return true
				}
			}
		}
	}
	return false
}

func main() {
	for l := 1; l <= 1000; l++ {
		triangleNum[l] = triangleNum[l-1] + l
	}
	var T int
	fmt.Scanln(&T)
	for i := 0; i < T; i++ {
		var n int
		fmt.Scanln(&n)
		if check(n) == true {
			fmt.Println(1)
		} else {
			fmt.Println(0)
		}
	}
}

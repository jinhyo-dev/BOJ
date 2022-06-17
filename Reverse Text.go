package main

import (
	"bufio"
	"fmt"
	"os"
)

func reverse(s string) string {
	rns := []rune(s)
	for i, j := 0, len(rns)-1; i < j; i, j = i+1, j-1 {
		rns[i], rns[j] = rns[j], rns[i]
	}
	return string(rns)
}

func main() {
	var n int
	reader := bufio.NewScanner(os.Stdin)
	fmt.Scanln(&n)
	for i := 0; i < n; i++ {
		reader.Scan()
		str := reader.Text()
		fmt.Print(reverse(str))
		fmt.Println()
	}
}

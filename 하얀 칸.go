package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	var line string
	var whiteBox int = 0
	reader := bufio.NewReader(os.Stdin)
	for i := 0; i < 8; i++ {
		line, _ = reader.ReadString('\n')
		var slice = strings.Split(line, "")
		for j := 0; j < 8; j++ {
			if i%2 == 0 {
				if "F" == slice[j] && j%2 == 0 {
					whiteBox++
				}
			} else {
				if "F" == slice[j] && j%2 != 0 {
					whiteBox++
				}
			}
		}
	}
	fmt.Println(whiteBox)
}

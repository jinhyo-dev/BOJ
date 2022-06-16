package main

import "fmt"

func main() {
	var A float64
	var B float64
	fmt.Scanln(&A, &B)
	if A*(100-B)/100 >= 100 {
		fmt.Println(0)
	} else {
		fmt.Println(1)
	}
}

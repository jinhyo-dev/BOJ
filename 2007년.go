package main

import (
	"fmt"
)

func main() {
	var day int = 0
	var lastDayList = [...]int{31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}
	var weekList = [...]string{"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"}

	var x, y int
	fmt.Scanln(&x, &y)

	for i := 0; i < x-1; i++ {
		day += lastDayList[i]
	}
	day = (day + y) % 7
	fmt.Println(weekList[day])
}

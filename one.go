package main

import (
	"fmt"
	"time"
)


// func main() {
// 	for i:=1;i<=100000;i++{
// 		fmt.Print(i)
// 	}
// 	m, _ := time.ParseDuration("1h30m")
// 	fmt.Printf("The movie is %.0f minutes long.", m.Minutes())
// 	fmt.Print("\n Hamza Lajk")
// }

 
// func mainx() {
//     now := time.Now()
//     defer func() {
//         fmt.Println(time.Now().Sub(now))
//     }()
// 	for i:=1;i<=100000;i++{
// 		fmt.Print(i)
// 	}
        
//     // Here you can do whatever you want

// }

func timeMeasurement(start time.Time) {
	elapsed := time.Since(start)
	fmt.Printf("Execution time: %s", elapsed)
}

func workerFunction() {
	defer timeMeasurement(time.Now())
	fmt.Println("Running 'workerFunction' function")
	for index := 0; index < 1000000; index++ {
		fmt.Print(index)
	}
	for i:=0; i<=1000000; i++{
		fmt.Print(i)
	}
}

func main() {
	fmt.Println("Function time measurement Golang Example")
	fmt.Println("")

	workerFunction()
}
// normal run time of goo Program if running Two LOOPs is 17 seconds and of python is 40 sec
// after converting it machine code time reduceds now is 16.24 seconds
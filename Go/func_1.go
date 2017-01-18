package main

import "fmt"

func average(args []float64) float64 {    
    total := 0.0
    for _, v := range args {
        total += v
    }
    return total / float64(len(args))
}

func f1() int {
    return f2()
}

func f2() int {
    return 42
}

func add(args ...int) int {
    total := 0
    for _, v := range args {
        total += v
    }
    return total
}

func makeEvenGenerator() func() uint {
    i := uint(0)
    return func() (ret uint) {
        ret = i
        i += 2
        return
    }
}

func main() {
    xs := []float64{1,2,3,4,5}
    fmt.Println("Averge value:", average(xs))
    fmt.Println("Value of f2:", f1())
    fmt.Println("Summ 1+2+3 =", add(1,2,3))
    nextEven := makeEvenGenerator()
    fmt.Println(nextEven()) 
    fmt.Println(nextEven()) 
    fmt.Println(nextEven())     
}
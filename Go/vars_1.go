package main

import "fmt"

var x string = "first"

func new_func() {
    fmt.Println("Value from new_func:", x)
}

func main() {
    new_func()
    fmt.Println(x)
    x = x + " second"
    fmt.Println(x)
    x = x + " third"
    fmt.Println(x)
    // short assigment
    n := 42
    fmt.Println(n)
}

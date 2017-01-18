package main

import "fmt"

var x int = 5

func main() {
    fmt.Println("Len of str 'Hello World!' is", len("Hello World!"))
    fmt.Println("Hello World"[0:11])
    fmt.Println("Hello " + "World!")
    
    x += 1
    fmt.Println(x)
    fmt.Println()

    i := 1
    for i <= 10 {
        fmt.Println(i)
        i = i + 1
    }
    
    fmt.Println()
    
    for i := 10; i >= 0; i-- {
        fmt.Println(i)
    }
    
    fmt.Println()
    
    j := 0
    switch j {
        case 0: fmt.Println("Zero")
        case 1: fmt.Println("One")
        case 2: fmt.Println("Two")
        case 3: fmt.Println("Three")
        case 4: fmt.Println("Four")
        case 5: fmt.Println("Five")
        default: fmt.Println("Unknown Number")
    }
}

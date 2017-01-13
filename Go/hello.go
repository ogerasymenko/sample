package main

// this is a comment

import "fmt"

func main() {
    var name string
    // print help message
    fmt.Print("Enter a name: ")
    // call stdin method
    fmt.Scanln(&name)
    // print result
    fmt.Println("Hello from", name+"!")
}

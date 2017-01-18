package main

import "fmt"

func main() {
    for i := 1; i <= 100; i++ {
       if i % 3 == 0 {
           if i == 99 {
               fmt.Print(i)
           } else {
            fmt.Print(i)
            fmt.Printf(", ")
           }
       }    
    }
    fmt.Printf("\n")
    
    var arr = [5] float64 {1,2,3,4,5}
    fmt.Print(arr[0:5])
    
    fmt.Printf("\n")
    
    // new arr for 1024 elements
    var new_arr [1024] int
    fmt.Print(new_arr[0:5])
    
    fmt.Printf("\n")
    
    // make slice
    slice := make([]string, 5)
    // def value to insert into slice
    var value string
    
    for i := 0; i < len(slice); i++ {
        // print help message
        fmt.Print("Enter a value to insert into slice: ")
        // read value from stdin
        fmt.Scanln(&value)
        // append it
        slice[i] = value
    }
    
    fmt.Println("Slice:", slice)
    fmt.Println("Slice len:", len(slice))
      
    // fmt.Printf("\n")
}

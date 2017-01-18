package main

import "fmt"

func first() {
    fmt.Println("1st")
}
func second() {
    fmt.Println("2nd")
}
func main() {
    defer second()
    first()
    /*
Ранее мы создали функцию, которая вызывает panic, чтобы сгенерировать ошибку выполнения. Мы можем обрабатывать паники с помощью встроенной функции recover. Функция recover останавливает панику и возвращает значение, которое было передано функции panic.
    */
    defer func() {    
        str := recover()
        fmt.Println(str)
    }()
    panic("***Panic message***")
}

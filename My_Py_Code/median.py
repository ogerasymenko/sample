def mediana(data):
    data.sort()
    if len(data) % 2 == 0:
        mid_index = int(len(data)/2)
        a = data[mid_index-1]
        b = data[mid_index]
        c = (a+b)/2
        return c
    elif len(data) % 2 != 0:
        mid_index = int((len(data)/2)+1)
        d = data[mid_index-1]
        return d

if __name__ == '__main__':
    assert mediana([1, 2, 3, 4, 5]) == 3, "Sorted list"
    assert mediana([3, 1, 2, 5, 3]) == 3, "Not sorted list"
    assert mediana([1, 300, 2, 200, 1]) == 2, "It's not an average"
    assert mediana([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
    print("Start the long test")
    assert mediana(list(range(1000000))) == 499999.5, "Long."
    print("The local tests are done.")


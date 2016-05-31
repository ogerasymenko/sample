def count_chars(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count

filename = input("Enter filename: ")

with open(filename) as f:
    text = f.read()

for char in "abcdefgihjklmnopqrstwxyz":
    result = 100 * count_chars(text, char) / len(text)
    print("{0} - {1}%".format(char, round(result, 2)))


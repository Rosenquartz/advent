inputFile = open("input01.txt", "r")
sum = 0
letters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
for line in inputFile:
    number = 0
    for t in line:
        if t in letters:
            number += 10 * int(t)
            break
    for u in line[::-1]:
        if u in letters:
            number += int(u)
            break
    sum += number
print(sum)
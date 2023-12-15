
import re

def findSymbol(grid, row, left, right):
    verMin = max(row-1, 0)
    verMax = min(row+1, len(grid)-1) 
    horMin = max(left-1, 0)
    horMax = min(right+1, len(grid[0]) - 1)
    # return (verMin, verMax, horMin, horMax)
    for r in range(verMin, verMax + 1):
        for c in range(horMin, horMax + 1):
            if r == row and left <= c and c <= right:
                # print(f"passing {r}x{c}:grid[r][c]")
                pass
            elif grid[r][c] != "." and grid[r][c].isnumeric() == False:
                return True
    print("returning False")
    return False

def findNumbers(row):
    rowString = "".join(row)
    numberList = {}
    matchingInProgress = False
    currentNumber = ""
    startIndex = 0
    for i in range(len(row)):
        if row[i].isnumeric():
            if matchingInProgress:
                currentNumber += row[i]
            else:
                matchingInProgress = True
                startIndex = i
                currentNumber += row[i]
        else:
            if matchingInProgress:
                matchingInProgress = False
                numberList[startIndex] = int(currentNumber)
                currentNumber = ""
    if matchingInProgress:
        matchingInProgress = False
        numberList[startIndex] = int(currentNumber)
        currentNumber = ""

    return numberList

if __name__ == "__main__":
    file = open("03-scratch-input.txt", "r")
    file = open("input03.txt", "r")
    grid = []
    for line in file:
        grid.append(list(line.strip()))
    sum = 0
    for row in range(len(grid)):
        # if row > 5:
        #     break
        numberList = findNumbers(grid[row])
        print(numberList)
        print(f"--------------------Row {row}")
        for number in numberList.keys():
            # isPart = findSymbol(grid, row, number, number+len(str(numberList[number]))-1)
            # print(f"Checking for {numberList[number]}")
            # if not isPart:
            #     print(isPart, f"for {numberList[number]}")
            # if isPart: sum += numberList[number]
            # # print(numberList[nu])
            # # print(numberList[number], findSymbol(grid, row, number, number+len(str(numberList[number]))-1))
            if findSymbol(grid, row, number, number+len(str(numberList[number]))-1):
                print(numberList[number])
                sum += numberList[number]
    print(f"Sum is {sum}")
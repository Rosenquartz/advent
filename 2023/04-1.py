def parseLine(line):
    line = line.strip()
    sepLine = line.split(" | ")
    winList = [int(k) for k in sepLine[0].split(": ")[1].split()]
    numList = [int(k) for k in sepLine[1].split()]
    return (winList, numList)

def compare(winList, numList):
    sum = 0
    for winNum in winList:
        if winNum in numList:
            sum += 1
    return sum

def pow(n):
    if n == 0:
        return 1
    else:
        return 2*pow(n-1)

if __name__ == "__main__":
    file = open("input04.txt", "r")
    totalScore = 0
    for line in file:
        winList, numList = parseLine(line)
        score = compare(winList, numList)
        if score == 0:
            continue
        else:
            totalScore += pow(score-1)
    print(totalScore)
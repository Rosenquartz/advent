def parseLine(line):
    line = line.strip()
    sepLine = line.split(" | ")
    winList = [int(k) for k in sepLine[0].split(": ")[1].split()]
    cardNo = int(sepLine[0].split(": ")[0].split()[1])
    numList = [int(k) for k in sepLine[1].split()]
    return (cardNo, winList, numList)

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

class Card():
    def __init__(self, cardNo, winList, numList):
        self.number = cardNo
        self.winList = winList
        self.numList = numList
        self.amount = 1

if __name__ == "__main__":
    file = open("input04.txt", "r")
    totalScore = 0
    cardDict = {}
    for line in file:
        cardNo, winList, numList = parseLine(line)
        cardDict[cardNo] = Card(cardNo, winList, numList)
    numCards = len(cardDict.keys())
    totalCards = 0
    for key in range(numCards):
        totalCards += cardDict[key+1].amount
        print(f"Card {key+1} ran {cardDict[key+1].amount} times")
        wins = compare(cardDict[key+1].winList, cardDict[key+1].numList)
        for win in range(wins):
            if win+1+key+1 > numCards:
                pass
            else:
                cardDict[win+1+key+1].amount += cardDict[key+1].amount
    print(totalCards)
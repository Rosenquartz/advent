def power(gameList):
    minRed = 0
    minBlue = 0
    minGreen = 0
    for game in gameList:
        if "red" in game:
            if minRed == 0: minRed = game["red"]
            elif minRed > 0 and game["red"] > minRed: minRed = game["red"]
        if "blue" in game:
            if minBlue == 0: minBlue = game["blue"]
            elif minBlue > 0 and game["blue"] > minBlue: minBlue = game["blue"]
        if "green" in game:
            if minGreen == 0: minGreen = game["green"]
            elif minGreen > 0 and game["green"] > minGreen: minGreen = game["green"]
    return minRed * minBlue * minGreen

def parseLine(line):
    id = int(line.split(": ")[0][5:])
    gamesRawString = line.split(": ")[1]
    gamesRawList = gamesRawString.split("; ")
    outputList = []
    for game in gamesRawList:
        cubeList = game.split(", ")
        currentList = {}
        for roll in cubeList:
            if "red" in roll:
                currentList['red'] = int(roll[:len(roll)-4])
            elif "blue" in roll:
                currentList['blue'] = int(roll[:len(roll)-5])
            elif "green" in roll:
                currentList['green'] = int(roll[:len(roll)-6])
        outputList.append(currentList)
    return {"gameList": outputList, "id": id}

if __name__ == "__main__":
    file = open("input02.txt", "r")
    totalPower = 0
    for line in file:
        line = line.strip()
        totalPower += power(parseLine(line)["gameList"])
    print(f"Total power is {totalPower}")
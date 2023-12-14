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

    

def checkGame(gameList, redMax, blueMax, greenMax):
    for game in gameList:
        if "red" in game:
            if game["red"] > redMax: return False
        if "blue" in game:
            if game["blue"] > blueMax: return False
        if "green" in game:
            if game["green"] > greenMax: return False
    return True

file = open("input02.txt", "r")

sum = 0

for line in file:
    line = line.strip()
    lineData = parseLine(line)

    if checkGame(lineData["gameList"], 12, 14, 13):
        print(f"Game {lineData['id']}: PASS")
        sum += lineData["id"]
    else:
        print(f"Game {lineData['id']}: FAIL")        
print(sum)
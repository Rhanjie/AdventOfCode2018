import re
import numpy

def solveFirstPuzzle(data: list):
    currentId = 0
    guards = {}
    sleepStart = 0
    howMany = 0

    goodMinute = 0
    bestId = 0

    for line in data:
        values = re.findall(r'([\d]+)', line)
        processedTask = (re.findall(r"(begins|falls|wakes)", line))[0]

        if processedTask == "begins":
            currentId = int(values[5])

            if bestId == 0:
                bestId = currentId

            if not currentId in guards:
                guards[currentId] = {"sleepTime": 0, "minutes": numpy.zeros(60)}

        elif processedTask == "falls":
            sleepStart = int(values[4])

        elif processedTask == "wakes":
            sleepEnd = int(values[4])

            sleepTime = (sleepEnd - sleepStart)

            guards[currentId]["sleepTime"] += sleepTime
            guards[currentId]["minutes"][sleepStart:sleepEnd] += 1

            for i in range(0, len(guards[currentId]["minutes"])):
                if howMany <= guards[currentId]["minutes"][i] and guards[bestId]["sleepTime"] <= guards[currentId]["sleepTime"]:
                    howMany = guards[currentId]["minutes"][i]

                    bestId = currentId
                    goodMinute = i

    return bestId * goodMinute

def solveSecondPuzzle(data: list):
    currentId = 0
    guards = {}
    sleepStart = 0
    howMany = 0

    goodMinute = 0
    bestId = 0

    for line in data:
        values = re.findall(r'([\d]+)', line)
        processedTask = (re.findall(r"(begins|falls|wakes)", line))[0]

        if processedTask == "begins":
            currentId = int(values[5])

            if not currentId in guards:
                guards[currentId] = {"sleepTime": 0, "minutes": numpy.zeros(60)}

        elif processedTask == "falls":
            sleepStart = int(values[4])

        elif processedTask == "wakes":
            sleepEnd = int(values[4])

            sleepTime = (sleepEnd - sleepStart)

            guards[currentId]["sleepTime"] += sleepTime
            guards[currentId]["minutes"][sleepStart:sleepEnd] += 1

            for i in range(0, len(guards[currentId]["minutes"])):
                if howMany <= guards[currentId]["minutes"][i]:
                    howMany = guards[currentId]["minutes"][i]

                    bestId = currentId
                    goodMinute = i

    return bestId * goodMinute

def main():
    file = open("../input/4.txt", "r")
    data = file.readlines()
    data.sort()

    print("#solveFirstPuzzle():",  solveFirstPuzzle(data))
    print("solveSecondPuzzle():", solveSecondPuzzle(data))


if __name__ == "__main__":
    main()
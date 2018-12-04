import re
import numpy
import collections

def solvePuzzle(tab: list):
    fabricList = numpy.zeros((1000, 1000))
    notOverlapAreaId = -1

    for i in range(len(tab)):
        numbers = re.findall(r"[\d]+", tab[i])

        for y in range(int(numbers[2]), int(numbers[2]) + int(numbers[4])):
            for x in range(int(numbers[1]), int(numbers[1]) + int(numbers[3])):
                if fabricList[y][x] == 0:
                    fabricList[y][x] = numbers[0]
                else:
                    fabricList[y][x] = -1

    for i in range(len(tab)):
        numbers = re.findall(r"[\d]+", tab[i])

        areaId = numbers[0]
        for y in range(int(numbers[2]), int(numbers[2]) + int(numbers[4])):
            for x in range(int(numbers[1]), int(numbers[1]) + int(numbers[3])):
                if fabricList[y][x] == -1:
                    areaId = 0

        if areaId != 0:
            notOverlapAreaId = areaId


    overlappedSegments = 0
    for y in range(0, 1000):
        for x in range(0, 1000):
            if fabricList[y][x] == -1:
                overlappedSegments += 1

    return overlappedSegments, notOverlapAreaId

    ##return fabricList.sum()


def main():
    file = open("../input/3.txt", "r")
    tab = file.readlines()

    print("solvePuzzle():", solvePuzzle(tab))


if __name__ == "__main__":
    main()
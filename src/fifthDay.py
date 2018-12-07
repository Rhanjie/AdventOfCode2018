import re
import numpy

def solveFirstPuzzle(chars: list):
    isEnd = False
    lastSize = len(chars)

    while not isEnd:
        isEnd = True

        i = 0
        while i < len(chars) - 1:
            if ord(chars[i]) <= 90:
                isBig = -1 #big letter
            else:
                isBig = 1  #small letter

            if ord(chars[i]) == (ord(chars[i + 1]) + (32 * isBig)):
                chars.pop(i + 1)
                chars.pop(i)
            else:
                i += 1

            if lastSize > len(chars):
                lastSize = len(chars)
                isEnd = False

    return len(chars)

def solveSecondPuzzle(chars: list):
    size = len(chars)

    for k in range(65, 91):
        copiedChars = chars.copy()

        i = 0
        while i < len(copiedChars) - 1:
            if ord(copiedChars[i].upper()) == k:
                copiedChars.pop(i)
            else:
                i += 1

        newSize = solveFirstPuzzle(copiedChars)
        if size > newSize:
            size = newSize

    return size

def main():
    file = open("../input/5.txt", "r")

    chars = []
    for char in file.readlines()[0]:
        chars.append(char)


    print("#solveFirstPuzzle():",  solveFirstPuzzle(chars.copy()))
    print("solveSecondPuzzle():", solveSecondPuzzle(chars.copy()))


if __name__ == "__main__":
    main()
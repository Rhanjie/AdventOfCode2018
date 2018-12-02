import math
import collections

def day1A():
    file = open("../input/1.txt", "r")
    value = 0

    for line in file:
        value += int(line)

    print(value)

def day1B():
    file = open("../input/1.txt", "r")
    tab = file.readlines()
    firstValue = 0
    found = [0]

    while True:
        for i in range(0, len(tab)):
            firstValue += int(tab[i])

            for item in found:
                if firstValue == item:
                    print("Found value =", item)
                    return

            found.append(firstValue)

def day2A():
    file = open("../input/2.txt", "r")
    tab = file.readlines()

    two = 0
    three = 0

    for line in tab:
        isTwo = False
        isThree = False

        d = collections.defaultdict(int)
        for char in line:
            d[char] += 1

        for item in d:
            if d[item] == 2 and isTwo == False:
                two += 1
                isTwo = True

            if d[item] == 3 and isThree == False:
                three += 1
                isThree = True

    print(two, "*", three, "=", two * three)

def day2B():
    file = open("../input/2.txt", "r")
    tab = file.readlines()

    for i in range(0, len(tab)):
        for j in range(i + 1, len(tab)):
            badLetters = 0
            lastBadIndex = 0

            for k in range(0, len(tab[i]) - 1):
                if tab[i][k] != tab[j][k]:
                    badLetters += 1
                    lastBadIndex = k

            if badLetters == 1:
                letters = list(tab[i])
                letters[lastBadIndex] = ""
                print("".join(letters))



def main():
    #day1A()
    #day1B()

    day2A()
    day2B()


if __name__ == "__main__":
    main()
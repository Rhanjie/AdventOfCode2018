import collections

def day2A(tab: list):
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

    return two * three

def day2B(tab: list):
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

                return "".join(letters)


    return None

def main():
    file = open("../input/2.txt", "r")
    tab = file.readlines()

    print("Day2A():", day2A(tab))
    print("Day2B():", day2B(tab))


if __name__ == "__main__":
    main()
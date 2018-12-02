

def day1A(tab: list):
    value = 0

    for line in tab:
        value += int(line)

    return value

def day1B(tab: set):
    firstValue = 0
    found = {firstValue}

    while True:
        for i in range(0, len(tab)):
            firstValue += int(tab[i])
            #print(firstValue)


            for item in found:
                if firstValue == item:
                    return item

            found.add(firstValue)


def main():
    file = open("../input/1.txt", "r")
    tab = file.readlines()

    print("Day1A():", day1A(tab))
    print("Day1B():", day1B(tab))


if __name__ == "__main__":
    main()
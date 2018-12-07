

def day1A(tab: list):
    value = 0

    for line in tab:
        value += int(line)

    return value

def day1B(tab: list):
    firstValue = 0
    found = {}

    while True:
        for element in tab:
            firstValue += int(element)

            if found.get(firstValue):
                return firstValue

            found[firstValue] = True


def main():
    file = open("../input/1.txt", "r")
    tab = file.readlines()

    print("Day1A():", day1A(tab))
    print("Day1B():", day1B(tab))


if __name__ == "__main__":
    main()
import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    quick_picks = int(input("How many quick picks? "))
    while quick_picks < 0:
        print("Please enter a valid number.")
        quick_picks = int(input("How many quick picks? "))

    for i in range(quick_picks):
        picks = []
        for a in range(NUMBERS_PER_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in picks:
                number = random.randint(MINIMUM, MAXIMUM)
            picks.append(number)
        picks.sort()
        print(" ".join("{:2}".format(number) for number in picks))


main()

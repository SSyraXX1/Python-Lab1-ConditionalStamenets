def run():
    year = int(input("Enter your birth year: "))
    r = year % 12

    if r == 0:
        sign = "Monkey"
    elif r == 1:
        sign = "Rooster"
    elif r == 2:
        sign = "Dog"
    elif r == 3:
        sign = "Pig"
    elif r == 4:
        sign = "Rat"
    elif r == 5:
        sign = "Ox"
    elif r == 6:
        sign = "Tiger"
    elif r == 7:
        sign = "Rabbit"
    elif r == 8:
        sign = "Dragon"
    elif r == 9:
        sign = "Snake"
    elif r == 10:
        sign = "Horse"
    else:
        sign = "Sheep"

    print("Your Chinese Zodiac sign is:", sign)

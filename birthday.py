def run():
    set1 = "1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31"
    set2 = "2 3 6 7 10 11 14 15 18 19 22 23 26 27 30 31"
    set3 = "4 5 6 7 12 13 14 15 20 21 22 23 28 29 30 31"
    set4 = "8 9 10 11 12 13 14 15 24 25 26 27 28 29 30 31"
    set5 = "16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31"

    birthday = 0

    print("Set 1:", set1)
    print("Is your birthday included in this set?")
    if int(input("Enter 1 for Yes and 0 for No: ")) == 1:
        birthday += 1

    print("Set 2:", set2)
    print("Is your birthday included in this set?")
    if int(input("Enter 1 for Yes and 0 for No: ")) == 1:
        birthday += 2

    print("Set 3:", set3)
    print("Is your birthday included in this set?")
    if int(input("Enter 1 for Yes and 0 for No: ")) == 1:
        birthday += 4

    print("Set 4:", set4)
    print("Is your birthday included in this set?")
    if int(input("Enter 1 for Yes and 0 for No: ")) == 1:
        birthday += 8

    print("Set 5:", set5)
    print("Is your birthday included in this set?")
    if int(input("Enter 1 for Yes and 0 for No: ")) == 1:
        birthday += 16

    print("Your birthday is:", birthday)

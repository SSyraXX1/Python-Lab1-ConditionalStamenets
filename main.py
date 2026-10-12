import bmi
import zodiac
import birthday

while True:
    print("press 'a' for BMI")
    print("press 'b' for  Zodiac finder")
    print("press 'c' for Birthday Guess")
    print("press 'd' for EXIT")
    
    answer=input("select an option:", )
    
    if answer == "a":
        bmi.start()
    elif answer == "b":
        zodiac.start()
    elif answer == "c":
        birthday.start()
    elif answer == "d":
        break

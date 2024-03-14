import random

response = input("press y to roll the dice and to exit")

while response == "y":
    number = random.randint(1,6)
    if number ==1:
        print("-----")
        print("--0--")
        print("-----")
        break
    elif number ==2:
        print("-----")
        print("-0 0-")
        print("-----")
        break
    elif number ==3:
        print("-----")
        print("-0 0-")
        print("--0--")
        break
    elif number ==4:
        print("-----")
        print("-0 0-")
        print("-0 0-")
        break
    elif number ==5:
        print("-0 0-")
        print("--0--")
        print("-0 0-")
        break
    elif number ==6:
        print("-0 0-")
        print("-0 0-")
        print("-0 0-")
        break

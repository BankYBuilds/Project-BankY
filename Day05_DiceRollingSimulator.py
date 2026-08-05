#DICE ROLLING SIMULATOR

import random

def die():
    roll = random.randint(1,6)
    return roll

rolls = 0
while True:
    val1 = die()
    val2 = die()

    total = val1 + val2

    if val1 == val2:
        print("🎉 Double")

    elif total == 7 or total == 11:
        print("🔥 Lucky roll!")


    print("Die 1:", val1)
    print("Die 2:", val2)
    print("Total:", total)

    rolls += 1
    choice = input("Do you want to roll again? Y/N")

    if choice.lower() == "n":
        print("Thanks for playing!!")
        print(f"You rolled the dice {rolls} times.")
        break

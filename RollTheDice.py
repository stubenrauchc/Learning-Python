import random
print("-----------------------------------------------")
print("       Hello User, Welcome to Dice Land!       ")
print("-----------------------------------------------")
KeepRolling = input("Enter 1 to Roll, 2 to exit")
print()
RollO = int(KeepRolling)
while RollO == 1:
    number_of_sides = input("How many sides are there to the Die you're rolling?")
    nos = int(number_of_sides)
    print(f"you have chosen to roll a {nos} sided die! Rolling Now!")
    print()
    Roll = random.randint(1,nos)
    positive = nos / 2 + 1
    negative = nos / 2 - 1
    neutral = nos / 2
    if nos == 2:
        if Roll == 1:
            print("Flipped a coin for you! you got Heads! Or a 1...")
        else:
            print("Flipped a coin for you! You got Tails! Or a 2...")
    elif nos == 1:
        print("Bro, a 1 sided die is always gonna be 1...")
    elif Roll >= positive:
        print(f"Hey! you got {Roll}, not bad!")
    elif Roll <= negative:
        print(f"Dang bruh, You got {Roll}, not good...")
    else:
        print(f"Meh, you got {Roll}, could have been worse.")
    KeepRolling = input("Enter 1 to continue rolling, enter any other number to exit")
    Rollo = int(KeepRolling)
    if Rollo != 1:
        print("goodbye")
        break

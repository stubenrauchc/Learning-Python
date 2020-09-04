
print("----------------------------------------------------------")
print("       Hello User, welcome to the Odd or Even tool!       ")
print("----------------------------------------------------------")

print("If you enter a number, I'll tell you if it's even or odd!")
continue_text = input("enter 1 to test, 2 to quit")
again = int(continue_text)
while again == 1:

    num_text = input("What is your number of choice?")
    num = int(num_text)
    div = int(num / 2)
    rem = num % 2
    if rem > 0:
        print(f"oh no, {num} is odd!")
            
    else:
        print(f"yooooo, {num} is even!")
    continue_text = input("enter 1 to test, 2 to quit")
    again = int(continue_text)
    if again == 2:
        print("good by, jerk")
        break


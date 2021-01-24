import random
import array
print("|-------------------------------------------------|")
print("|           Welcome to the Card Picker!           |")
print("|-------------------------------------------------|")

array1 = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13
array2 = 14, 15, 16, 17

## uncomment the two lines below for diagnostics
## print(f"{array1}")
## print(f"{array2}")

## uncomment the two lines below for diagnostics
## print(f"{nom}")
## print(f"{st}")

KeepDrawing = input("Would you like to draw a card? 1 for yes, 2 for no: ")
KD = int(KeepDrawing)
while KD == 1:
    nom = random.choice(array1)
    st = random.choice(array2)
## this is for determining what suite the card is
    if st == 14:
        st1 = "Hearts"
    elif st == 15:
        st1 = "Spades"
    elif st == 16:
        st1 = "Clovers"
    elif st == 17:
        st1 = "Diamonds"
## this will convert the card from a number to ace/jack/queen/king if applicable
    if nom == 1:
        nom1 = "Ace"
    elif nom == 11:
        nom1 = "Jack"
    elif nom == 12:
        nom1 = "Queen"
    elif nom == 13:
        nom1 = "King"
    else:
        nom1 = nom
## continue or exit commands
    print(f"{nom1} of {st1}")
    KeepDrawing = input("would you like to draw again? 1 for yes, 2 for no: ")
    KD = int(KeepDrawing)
    if KD == 2:
        print("Peace out!")
        break
    elif KD > 2:
        print("uh oh, that's not a 1 or 2, Exiting Now")

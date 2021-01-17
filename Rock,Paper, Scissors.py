'''
use the random function here.
You make a move first and then the program makes one.
To indicate the move, you can either use a single alphabet or input an entire string.
A function will have to be set up to check the validity of the move.

Using another function, the winner of that round is decided.
You can then either give an option of playing again or
decide a pre-determined number of moves in advance.
A scorekeeping function will also have to be created which
will return the winner at the end.

'''
import random

def ai():
    number = random.randint(1,4)
    if number == 1:
        global aiinput
        aiinput = ("rock")
        print(("The choice of computer is: "),aiinput)
    elif number == 2:
        aiinput = ("paper")
        print(("The choice of computer is: "),aiinput)
    elif number == 3:
        aiinput = ("scissors")
        print(("The choice of computer is: "),aiinput)

def draw():
    print ("Draw")
def loser():
    print ("Loser!")
def winner():
    print ("You won!")

print("Welcome to the game to quit prompt q")
while True:
    usrinp = input("rock, scissors or paper? you can also prompt r,s or p: ")
    ai()
    if usrinp == ("r") and aiinput == ("rock"):
        draw()
    elif usrinp == ("r") and aiinput == ("paper"):
        loser()
    elif usrinp == ("r") and aiinput == ("scissors"):
            winner()


    if usrinp == ("p") and aiinput == ("rock"):
        winner()
    elif usrinp == ("p") and aiinput == ("paper"):
        draw()
    elif usrinp == ("p") and aiinput == ("scissors"):
        loser()

    if usrinp == ("s") and aiinput == ("rock"):
        loser()
    elif usrinp == ("s") and aiinput == ("paper"):
        winner()
    elif usrinp == ("s") and aiinput == ("scissors"):
        draw()
    if usrinp == ("q"):
        quit()






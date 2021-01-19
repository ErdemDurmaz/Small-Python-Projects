'''
    Generate a random number each dice the program runs,
and the users can use the dice repeatedly for as long as he wants.
When the user rolls the dice, the program will generate a random number between 1 and 6
(as on a standard dice).
The number will then be displayed to the user.
It will also ask users if they would like to roll the dice again.
The program should also include a function that can randomly grab a number within 1 to 6 and print it.
'''
import random
def roll():
    number = random.randrange(1,7)
    print (number)
while True:
    print("Welcome to Dice roller")
    usrinp = input("To roll a dice input roll: ")
    if usrinp == ("roll"):
        roll()
        secondinput = input("Would you like to roll the dice again? Prompt yes: ")
        if secondinput == ("yes"):
            roll()
        else:
            print("Thank you for playing the game")
            quit()
    else:
        print("unexptected input")
        quit()
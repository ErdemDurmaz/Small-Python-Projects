#Make a program in which the computer randomly chooses a number
# between 1 to 10, 1 to 100, or any range.
# Then give users a hint to guess the number.
# Every time the user guesses wrong, he gets another clue,
# and his score gets reduced. The clue can be multiples, divisible,
# greater or smaller, or a combination of all.
#You will also need functions to compare the inputted number with the guessed number,
# to compute the difference between the two,
# and to check whether an actual number was inputted or not in this python project.
import random
score = 100
number = (random.randint(0,101))
print("Welcome to the number guessing game you will start with 100 points ")
print("Every mistake you make will result in 10 points.")

while True:
    usrinp = int(input("Please prompt the number: "))
    if usrinp > number:
        modulo = usrinp % number
        print("This is bigger than guessed number,modulo of your number is ",modulo ,"try a smaller number")
        score = score -10
        print("Your Score:",score)
    elif usrinp < number:
        print("Well This number is too small try a bigger number")
        score = score -10
        print("Your Score: ",score)
    elif usrinp == number:
        print("BULLS EYE, This is the guessed number")
        score = score -10
        print("Your Score: ",score)
        quit()
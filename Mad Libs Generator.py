#The input from the user could be anything ,
# from an adjective, a pronoun, or even a verb.
# After all the inputs are entered the application takes
# all the data and arranges it to build a story template.
# adjective, noun, verb

print("Welcome to the Story Generator prompt done to exit program")
while True:
    adjective_input = input('Enter an adjective prompt: ')
    if adjective_input == ('done'):
        quit()
    noun_input = input('Enter a noun prompt: ')
    if adjective_input == ('done'):
        quit()
    verb_input = input('Enter a verb prompt: ')
    if adjective_input == ('done'):
        quit()
    print ("The problem with thieves today, said Lledos, Is the lack of",noun_input)
    print ("My dear friends, we aren't mugging some",adjective_input, " tourist fresh off the ferry.")
    print ("Now I",verb_input, "them the greatest lesson of all", )
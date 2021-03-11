###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# Try to figure out what this code is doing and how it might be useful to you
from random import randint, shuffle
# digits = list(range(10))
# shuffle(digits)
# print(digits[:3])

# Another hint:
# guess = input("What is your guess? ")
# print(guess)

# Think about how you will compare the input to the random number, what format
# should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!


def generate_random_num():
    '''
    Returns a list of a random three digit number.
    '''
    digits = list(range(10))
    shuffle(digits)
    return digits[:3]


def get_guess():
    '''
    Asks to guess a number and returns it in a list.
    '''
    raw_guess = input("What is your guess? ")
    return [int(i) for i in raw_guess]


def generate_clues(guess, computer_num):
    '''
    Compares user guess to computer num and checks for matches,
    similarities (Close) or nothing in common (Nope)
    '''

    if guess == computer_num:
        print("You have guessed the number!")
        return "Correct!"

    # Compare guess to computer_num
    for i in range(3):

        if int(guess[i]) == computer_num[i]:
            print("Match")

        elif int(guess[i]) in computer_num:
            print("Close")

        else:
            print("None")

    return "Continue"


# Game Start
print("Welcome to Code Breaker! Guess a 3 digit number")

# Generate computer_num that will be guessed
computer_num = generate_random_num()
print("Code has been generated, take a guess (3 digit number)")

# Empty clue to start the game
clue = ""

# Keep asking until guess is correct
while clue != "Correct!":

    # Ask for guess
    guess = get_guess()

    # Compare guess and give clue
    clue = generate_clues(guess, computer_num)

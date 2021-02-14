from random import randint
from art import  logo

# constants :
EASY_LEVEL = 10
HARD_LEVEL = 5

# functions :
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard' : ")
    if level == 'easy':
        return EASY_LEVEL
    elif level == 'hard':
        return HARD_LEVEL

def check_answer(number, answer, turns):
    if number < answer:
        print("Too high.")
        return turns - 1
    elif number > answer:
        print("Too low.")
        return turns -1
    else:
        print(f"You got it. The answer is {number}")

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 to 100.")
    number = randint(1, 100)
    print(f"pssst. the correct answer is {number}")
    turns = set_difficulty()
    answer = 0
    while answer != number:
        print(f"You have {turns} attempts remaining to guess the answer.")
        answer = int(input("Make a guess : "))
        turns = check_answer(number, answer, turns)
        if turns == 0:
            print("You've run out of turns. You lose.")
            return
        elif answer != number:
            print("Guess again.")

game()

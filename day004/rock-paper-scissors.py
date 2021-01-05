rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
invalid = '''
 ___ _   ___     ___    _     ___ ____
|_ _| \ | \ \   / / \  | |   |_ _|  _ \
 | ||  \| |\ \ / / _ \ | |    | || | | |
 | || |\  | \ V / ___ \| |___ | || |_| |
|___|_| \_|  \_/_/   \_\_____|___|____/

'''
import random

computer_score = 0
player_score = 0
a = [rock, paper, scissors]
while (player_score < 5 and computer_score < 5):
    choose = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
    if (choose == "0"):
        print(rock)
    elif (choose == "1"):
        print(paper)
    elif (choose == "2"):
        print(scissors)
    else:
        print(invalid)
    print("Computer chose:")
    computer = random.choice(a)
    print(computer)
    if (choose == "0" and computer == rock):
        print("Tie")
        print(f"Player score: {player_score} \nComputer score: {computer_score}")
    elif (choose == "0" and computer == paper):
        computer_score += 1
        print(f"Player score: {player_score} \nComputer score: {computer_score}")
    elif (choose == "0" and computer == scissors):
        player_score += 1
        print(f"Player score: {player_score} \nComputer score: {computer_score}")
    if (choose == "1" and computer == rock):
        player_score += 1
        print(f"Player score: {player_score} \nComputer score: {computer_score}")
    elif (choose == "1" and computer == paper):
        print("Tie")
        print(f"Player score: {player_score} \nComputer score: {computer_score}")
    elif (choose == "1" and computer == scissors):
        computer_score += 1
        print(f"Player score: {player_score} \nComputer score: {computer_score}")
    if (choose == "2" and computer == rock):
        computer_score += 1
        print(f"Player score: {player_score} \nComputer score: {computer_score}")
    elif (choose == "2" and computer == paper):
        player_score += 1
        print(f"Player score: {player_score} \nComputer score: {computer_score}")
    elif (choose == "2" and computer == scissors):
        print("Tie")
        print(f"Player score: {player_score} \nComputer score: {computer_score}")
if player_score >= 5:
    print("Player won the game !!!")
else:
    print("Computer won the game!!! bhoooo")

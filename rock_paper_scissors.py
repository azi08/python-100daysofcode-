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

#Write your code below this line 👇
import random

computer_move = random.randint(0,2)
player_move = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

moves = [rock, paper, scissors]

print(moves[computer_move], "\n COMPUTER \n")
print(moves[player_move], '\n YOU \n')

if computer_move == 0:
  if player_move == 0:
    print("It's a draw!")
  elif player_move == 2:
    print('You Lose! Game Over.')
  elif player_move == 1:
    print('You win! You are smarter than the computer!')

if computer_move == 1:
  if player_move == 1:
    print("It's a draw!")
  elif player_move == 0:
    print('You Lose! Game Over.')
  elif player_move == 2:
    print('You win! You are smarter than the computer!')

if computer_move == 2:
  if player_move == 2:
    print("It's a draw!")
  elif player_move == 1:
    print('You Lose! Game Over.')
  elif player_move == 0:
    print('You win! You are smarter than the computer!')

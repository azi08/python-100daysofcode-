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

print("Welcome to the classic Rock-Paper-Scissors Game!\n")
moves = [rock, paper, scissors]



def Prompt():
  message = "Thank you for playing!"
  user_choice = input("Try Again? Type 'yes' or 'no' : \n").lower()
  if user_choice == 'yes':
    return Player()
  elif user_choice == 'no':
    print(message)

def Computer():
  computer_move = random.randint(0, 2)
  return computer_move

def Player():

  try:
    user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    print(f"{moves[computer_move]} \n COMPUTER \n {moves[user_input]} \n YOU \n")
    return user_input
  except IndexError:
    return Prompt()
  except ValueError:
    return Prompt()
     

    
def MainGame(computer_move, player_move):
    
    if computer_move == 0:
        if player_move == 0:
          print("It's a draw!")
          Prompt()
        elif player_move == 2:
          print('You Lose! Game Over.')
          Prompt()
        elif player_move == 1:
          print('You win!')
          Prompt()
        
      
    if computer_move == 1:
        if player_move == 1:
          print("It's a draw!")
          Prompt()
        elif player_move == 0:
          print('You Lose! Game Over.')
          Prompt()
        elif player_move == 2:
          print('You win!')
          Prompt()
 
      
    if computer_move == 2:
        if player_move == 2:
          print("It's a draw!")
          Prompt()
        elif player_move == 1:
          print('You Lose! Game Over.')
          Prompt()
        elif player_move == 0:
          print('You win!')
          Prompt()

          
computer_move = Computer()
player_move  = Player()
MainGame(computer_move, player_move)

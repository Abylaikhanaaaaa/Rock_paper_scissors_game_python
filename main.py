import random
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
game_image = [rock, paper, scissors]
user_choise = int(input("Type 0 for Rock, 1 Paper, 2 for SCissors?\n"))
if user_choise >= 3 or user_choise < 0:
	print('invalid number or sumbol')
else:
	print(game_image[user_choise])
computer_choise = random.randint(0, 2)
print(game_image[computer_choise])
if user_choise >= 3 or user_choise < 0:
	print('invalid number or sumbol')
elif user_choise == computer_choise:
	print('Draw')
elif user_choise == 0 and computer_choise == 2:
	print('You WIN!!!')
elif computer_choise == 0 and user_choise == 2:
	print('You Lose')
elif user_choise > computer_choise:
	print('You WIN!!')
elif computer_choise > user_choise:
	print('You Lose')



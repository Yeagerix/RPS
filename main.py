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

game_images = [rock, paper, scissors]

player_input = input("What do you choose? Type 0 for rock, type 1 for paper, type 2 for scissors.\n")

computer_choice = random.randint(0,2)

if player_input == "0":
  print(f"You chose {rock}")
elif player_input == "1":
  print(f"You chose {paper}")
elif player_input == "2":
  print(f"You chose {scissors}")


if computer_choice == 0:
  print(f"The computer chose {rock}")
elif computer_choice == 1:
  print(f"The computer chose {paper}")
elif computer_choice == 2:
  print(f"The computer chose {scissors}")

if computer_choice & player_input == 





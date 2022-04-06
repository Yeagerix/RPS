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

player_input = input("What do you choose? Type 0 for rock, type 1 for paper, type 2 for scissors ")

if player_input == "0":
  print(rock)
elif player_input == "1":
  print(paper)
elif player_input == "2":
  print(scissors)
else:
  print("That's Invalid")


rps_computer = ["0","1","2"]
computer_choice = rps_computer
print(random.choice(computer_choice))

if computer_choice == "0":
  print(rock)
elif computer_choice == "1":
  print(paper)
elif computer_choice == "2":
  print(scissors)

#simple text rock paper scissors program to utilize randomization, and lists

import random
import sys

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
choices = [rock, paper, scissors]
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n"))
comp_choice = random.randint(0,2)
if user_input == 0:
    print(choices[0])
elif user_input == 1:
    print(choices[1])
elif user_input == 2:
    print(choices[2])
else:
    print("Wrong input")
    sys.exit()

print("Computer chose:\n")
print(choices[comp_choice])

if user_input == comp_choice:
    print("\nDraw!")
elif user_input == 0 and comp_choice == 1 or user_input == 1 and comp_choice == 2 or user_input == 2 and comp_choice == 0:
    print("\nYou Lose!")
elif comp_choice == 0 and user_input == 1 or comp_choice == 1 and user_input == 2 or comp_choice == 2 and user_input == 0:
    print("\nYou Win!")
import random
print('Welcome to Rock, Paper, Scissors!!')
rock = """ 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors ="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
images = [rock, paper, scissors]
actions = ["Rock", "Paper", "Scissors"]
user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors:\n'))
computer_choice = random.randint(0,2)
print("Computer chose: ")
print(images[computer_choice])
print(f"\nYou chose: {images[user_choice]}")
if user_choice == 0 and computer_choice == 2:
    print('You win!')
elif user_choice == 2 and computer_choice == 0:
    print('You lose!')
elif user_choice > computer_choice:
    print('You win!')
elif user_choice < computer_choice:
    print('You lose!')
elif user_choice == computer_choice:
    print('It\'s a tie!')
elif user_choice < 0 or user_choice > 2:
    print('Invalid input! Please choose 0, 1, or 2.')
else:
    print('Invalid input! Please choose 0, 1, or 2.')
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
import random
a=[rock,scissors,paper]
game_start=True
while game_start:
    choice=input("welcome to rock, paper, scissors game.which one you want to choose rock, paper, scissors?\n")
    if choice=="rock":
        choice1=a[0]
        print(a[0])
    elif choice=="scissors":
        choice1=a[1]
        print(a[1])
    elif choice=="paper":
        choice1=a[2]
        print(a[2])
    
    computer_choice=random.randint(0,2)
    computer_choice1=a[computer_choice]
    print(f"computer's choice is {computer_choice1}")
    if choice1==computer_choice1:
        print("you are equal, no win or lose, continue.")
    elif (choice1==rock and computer_choice1==scissors) or (choice1==paper and computer_choice1==rock) or (choice1==scissors and computer_choice1==paper):
        print("you win! congradulation!")
        game_start = False
    else:
        print("you lose. never mind.")
        game_start = False

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
game_image=[rock,paper,scissors]
user_choice=int(input("what do you choose? type 0 for rock,1 for paper and 2 for scissors\n"))

if(user_choice>=0 and user_choice<=2):
    print("you choose")
    print(game_image[user_choice])

    computer_choice=random.randint(0,2)
    print("computes choose")
    print(game_image[computer_choice])

if(user_choice>=3 or user_choice<0):
    print("you typed an invalid number you loose")
elif(user_choice==0 and computer_choice ==2):
    print("you win")
elif(computer_choice==0 and user_choice==2):
    print("you loose")

elif(computer_choice>user_choice):
    print("you loose")
elif(user_choice>computer_choice):
    print("you win")
elif(computer_choice==user_choice):
    print("its a draw")


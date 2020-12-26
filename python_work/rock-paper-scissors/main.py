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
computer_choice = random.randint(0, 2)
my_choice = int(input('''choose
0, for rock
1, for paper
2, scissors \n''')) 
image = [rock, paper, scissors]


if my_choice >= 3 or my_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif my_choice == 0 and computer_choice == 2:
  print('computer_choice' + image[computer_choice] + "my_choice" + image[my_choice] + "You win!\n")
elif computer_choice == 0 and my_choice == 2:
  print("computer_choice" + image[computer_choice]+ "my_choice" + image[my_choice] + "You lose\n")
elif computer_choice > my_choice:
  print("computer_choice"+image[computer_choice] + "my_choice\n" + image[my_choice] + "You lose\n")
elif my_choice > computer_choice:
  print("computer_choice" +image[computer_choice] + "my_choice\n" +image[my_choice] + "You win!")
elif computer_choice == my_choice:
  print("computer_choice" + image[computer_choice] +"my_choice\n" + image[my_choice] + "It's a draw")
  
  
  




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

human_choice = int(input("what do you choose, type 0 for rock , 1 for paper or 2 for scissors.\n"))
if human_choice==0:
    print(rock)
elif human_choice==1:
    print(paper)
elif human_choice==2:
    print(scissors)
computer_choice=random.randint(0,2)
if computer_choice==0:
    print(f"computer choose\n{rock}")
elif computer_choice==1:
    print(f"computer choose\n{paper}")
elif computer_choice==2:
    print(f"computer choose\n{scissors}")
    
if human_choice==computer_choice:
    print("tie match")
elif human_choice==0 and computer_choice==1 or human_choice==1 and computer_choice==2 or human_choice==2 and computer_choice==0:
    print("computer wins")  
else:
    print("human wins")
    

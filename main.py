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

a = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# rock = 0
# paper = 1
# scissors = 2

c = "Computer Choice"

if a == 0:
  print(rock)
elif a == 1:
  print(paper)
else:
  print(scissors)

import random
b = random.randint(0,2)

if a == 0:
  if b == 1:
    print(c)
    print(paper)
    print("You loss")
  elif b == 0:
    print(c)
    print(rock)
    print("Draw")
  else :
    print(c)
    print(scissors)
    print("Your won")
elif a == 1:
  if b == 2 :
    print(c)
    print(scissors)
    print("You loss")
  elif b == 1:
    print(c)
    print(paper)
    print("Draw")
  else:
    print(c)
    print(rock)
    print("You won")
else :
  if b == 0:
    print(c)
    print(rock)
    print("You loss")
  elif b == 2:
    print(c)
    print(scissors)
    print("Draw")
  else:
    print(c)
    print(paper)
    print("You won")

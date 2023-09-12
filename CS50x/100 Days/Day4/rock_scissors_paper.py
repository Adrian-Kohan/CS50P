import random
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

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

shapes = [rock, paper, scissors]
user = int(input("What do you choose?Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
computer = random.randint(0, 2)

if 0 > user or user >= 3:
    print("You pick up a wrong number so you loose")
else:
    print(shapes[user])
    print("Computer chose:")
    print(shapes[computer])
    if shapes[computer] == "rock" and shapes[user] == "scissors":
        print("You lose")
    elif shapes[computer] == "rock" and shapes[user] == "rock":
        print("It's a draw")
    elif shapes[computer] == "paper" and shapes[user] == "rock":
        print("You lose")
    elif shapes[computer] == "paper" and shapes[user] == "paper":
        print("It's a draw")
    elif shapes[computer] == "scissors" and shapes[user] == "rock":
        print("You lose")
    elif shapes[computer] == "scissors" and shapes[user] == "scissors":
        print("It's a draw")
    else:
        print("You win")

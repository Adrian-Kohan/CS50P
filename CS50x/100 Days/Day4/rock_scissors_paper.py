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
user = input("What do you choose?Type 0 for Rock, 1 for Paper and 2 for Scissors.\n")
print(shapes[user])
print("Computer chose:")
computer = random.choice(shapes)
print(computer)

if computer == "rock" and shapes[user] == "scissors":
    priint("You lose")
elif computer == "rock" and shapes[user] == "rock":
    priint("Tie")
elif computer == "paper" and shapes[user] == "rock":
    priint("You lose")
elif computer == "paper" and shapes[user] == "paper":
    priint("Tie")
elif computer == "scissors" and shapes[user] == "rock":
    priint("You lose")
elif computer == "scissors" and shapes[user] == "scissors":
    priint("Tie")
else:
    print("You win")

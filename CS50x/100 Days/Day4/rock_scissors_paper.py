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
computer = random.choice(shapes)

if 0 > user and user >= 3:
    print("You pick up a wrong number so you loose")
elif 0 <= user <= 2:
    print(shapes[user])
    print("Computer chose:")
    print(computer)

if computer == "rock" and shapes[user] == "scissors":
    print("You lose")
elif computer == "rock" and shapes[user] == "rock":
    print("It's a draw")
elif computer == "paper" and shapes[user] == "rock":
    print("You lose")
elif computer == "paper" and shapes[user] == "paper":
    print("It's a draw")
elif computer == "scissors" and shapes[user] == "rock":
    print("You lose")
elif computer == "scissors" and shapes[user] == "scissors":
    print("It's a draw")
else:
    print("You win")

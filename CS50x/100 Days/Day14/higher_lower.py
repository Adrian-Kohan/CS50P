from art import logo, vs
from game_data import data
import random

A = random.choice(data)
B = random.choice(data)

def game():
    print(logo)
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")
    print(vs)
    print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}.")

score = 0
while True:
    answer = input("Who has more followers? Type 'A' or 'B': ")
    if answer == 'A':
        if A['follower_count'] > B['follower_count']:
            print("You're right! Current score: {score}")
            score += 1
            game()
        else:
            print("Sorry, that's wrong. Final score: {score}")
            return
    else:
        if A['follower_count'] < B['follower_count']:
            print("You're right! Current score: {score}")
            score += 1
            game()
        else:
            print("Sorry, that's wrong. Final score: {score}")
            return
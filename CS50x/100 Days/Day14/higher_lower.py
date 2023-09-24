from art import logo, vs
from game_data import data
import random

A = random.choice(data)
B = random.choice(data)

print(logo)
print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")
print(vs)
print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}.")
answer = input("Who has more followers? Type 'A' or 'B': ")
score = 0
if answer == 'A':
    if A['follower_count'] > B['follower_count']:

        print("Sorry, that's wrong. Final score: {score}")
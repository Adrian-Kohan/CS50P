from art import logo, vs
from game_data import data
from replit import clear
import random

print(logo)

def random_A_and_B():
    return random.choice(data)

A = random_A_and_B()

def game():
    score = 0
    while True:
        A = {}
        B = random_A_and_B()

        def comparation():
            print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")
            print(vs)
            print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}.")

        comparation()
        answer = input("Who has more followers? Type 'A' or 'B': ")
        if answer == 'A':
            if A['follower_count'] > B['follower_count']:
                clear()
                print(logo)
                score += 1
                print(f"You're right! Current score: {score}")
                A = A
            else:
                print(f"Sorry, that's wrong. Final score: {score}")
                return
        else:
            if A['follower_count'] < B['follower_count']:
                clear()
                print(logo)
                score += 1
                print(f"You're right! Current score: {score}")
                A = B
            else:
                print(f"Sorry, that's wrong. Final score: {score}")
                return

game()
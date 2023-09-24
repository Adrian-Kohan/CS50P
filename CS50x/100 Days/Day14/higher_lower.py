from art import logo, vs
from game_data import data
from replit import clear
import random

print(logo)

def random_A_and_B():
    return random.choice(data)

A = random_A_and_B()
B = random_A_and_B()

def comparation(A, B):
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")
    print(vs)
    print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}.")

comparation(A, B)

score = 0

def check_answer():
        answer = input("Who has more followers? Type 'A' or 'B': ")
        if answer == 'A':
            if A['follower_count'] > B['follower_count']:
                clear()
                print(logo)

                return score + 1
            print(f"You're right! Current score: {score}")
            if A['follower_count'] < B['follower_count']:
                return
            print(f"Sorry, that's wrong. Final score: {score}")

        if answer == 'B':
            if A['follower_count'] > B['follower_count']:
                clear()
                print(logo)
                return score + 1
            print(f"You're right! Current score: {score}")
            if A['follower_count'] < B['follower_count']:
                return
            print(f"Sorry, that's wrong. Final score: {score}")

check_answer()


def game():
    while True:
        comparation(A, B)
        check_answer()

game()
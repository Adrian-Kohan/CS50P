from art import logo, vs
from game_data import data
import random

print(logo)
choosen_person = random.choice(data)

print(f"Compare A: {choosen_person[name]}")


print(vs)
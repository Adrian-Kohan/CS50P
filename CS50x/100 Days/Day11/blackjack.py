# # # # # # # # # # # # # # #  Our Blackjack House Rules # # # # # # # # # # # # # # # # #

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.

# # # # # # # # # # # # # # # # # # # # #  Hints # # # # # # # # # # # # # # # # # # # # #

from art import logo
from replit import clear
import random

print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

your_cards = random.sample(cards, 2)
current_score = your_cards[0] + your_cards[1]
print(f"Your cards: {your_cards}, Current score: {current_score}")
computer_first_card = random_choice()
print(f"Computer's first card: {computer_first_card}")


continue_game = True
while continue_game:
    another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if another_card == "n":
        continue_game = False
    choice = random.choice(cards)
    current_score += your_cards[2]
    print(f"Your cards: {your_cards}, Current score: {current_score}")
    print(f"Computer's first card: {computer_first_card}")




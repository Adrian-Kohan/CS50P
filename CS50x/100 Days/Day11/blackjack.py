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

def blackjack():
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    your_cards = random.sample(cards, 2)
    current_score = your_cards[0] + your_cards[1]
    print(f"Your cards: {your_cards}, Current score: {current_score}")
    computer_first_card = random.choice(cards)
    print(f"Computer's first card: {computer_first_card}")


    def winner():
        computer_second_card = random.sample(cards, 1)
        computer_second_card.append(computer_first_card)
        computer_score = sum(computer_second_card)
        def print_result():
            print(f"Your final hand: {your_cards}, final score: {current_score}")
            print(f"Computer's final hand: {computer_second_card}, final score: {computer_score}")

        while computer_score < 17:
            computer_second_card.append(random.choice(cards))
            computer_score = sum(computer_second_card)

        if 11 in your_cards and current_score > 21:
            your_cards.remove(11)
            your_cards.append(1)
            current_score = sum(your_cards)


        if 11 in computer_second_card and computer_score > 21:
            computer_second_card[computer_second_card.index(11)] = 1
            computer_score = sum(computer_second_card)

        if computer_score == 21 and len(computer_second_card) == 2:
            print_result()
            print("Lose, opponent has Blackjack  😱")

        elif current_score == 21 and len(your_cards) == 2:
            print_result()
            print("Win, with a Blackjack 😎")

        elif current_score == computer_score:
            print_result()
            print("Draw 🙃")

        elif computer_score < current_score and current_score < 21:
            print_result()
            print("You win 😃")

        elif current_score > 21 and computer_score < 21:
            print_result()
            print("You went over. You lose.😭")

        elif computer_score > 21 and current_score < 21:
            print_result()
            print("opponent went over. You win.😁")

        else:
            print_result()
            print(" You lose 😤")


    continue_game = True
    while continue_game:
        another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if another_card == "n":
            winner()
            answer = input("Do you want to play a game of Blackjack? type 'y' or 'n': ")
            if answer == 'y':
                clear()
                blackjack()
            elif  answer == 'n':
                continue_game = False

        elif another_card == "y":
            choice = random.choice(cards)
            your_cards.append(choice)
            current_score += choice
            print(f"Your cards: {your_cards}, Current score: {current_score}")
            print(f"Computer's first card: {computer_first_card}")
            winner()
            answer = input("Do you want to play a game of Blackjack? type 'y' or 'n': ")
            if answer == 'y':
                clear()
                blackjack()
            else:
                continue_game = False

blackjack()
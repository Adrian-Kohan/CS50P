from gavel import logo
from replit import clear
print(logo)
print("Welcome to the secret auction program.")
secret_auction = {}

def winner(auction):
    max = 0
    winner = ""
    for person in auction:
        bid_amount = auction[name]
        if bid_amount > max:
            max = bid_amount
            winner = person
    print(f"The winner is {winner} with a bid of {max}")

while True:
    name = input("What is your name?: ")
    bid = int(input("What's your bid? $"))
    secret_auction[name] = bid
    answer = input("Are there any other bidders? Type 'yes' or 'no'\n")
    if answer == "yes":
        clear()
        continue
    elif answer == "no":
        winner(secret_auction)
        break


from gavel import logo
from replit import clear
print(logo)
print("Welcome to the secret auction program.")
secret_auction = {}
def winner(auction):
    max = 0
    for person in auction:
        if auction[name] > max:
            max = auction[name]
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


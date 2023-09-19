from gavel import logo
from replit import clear
print(logo)
print("Welcome to the secret auction program.")
name = input("What is your name?: ")
bid = input("What's your bid? $")

def auction(input_name, input_bid):
    secret_auction ={}
    max = ''
    for key in secrect_auction:
        secrect_auction[name] = bid
    for i in range(len(secrect_auction)):
        max = secrect_auction[0]
        if secrect_auction[0] < secrect_auction[1]:
            max = secrect_auction[i]
    print(f"The winner is {name} with a bid of {max}")

while True:
    answer = input("Are there any other bidders? Type 'yes' or 'no'\n")
    if answer == "yes":
        name = input("What is your name?: ")
        bid = input("What's your bid? $")
        clear()
        auction(name, bid)
        continue

    elif answer == "no":
        break


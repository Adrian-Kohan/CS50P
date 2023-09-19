from gavel import logo
from replit import clear
print(logo)
print("Welcome to the secret auction program.")
name = input("What is your name?: ")
bid = input("What's your bid? $")
secret_auction =[]

def auction(input_name, input_bid):
    secret_auction.append({input_name : [input_bid] })

auction(name, bid)

while True:
    answer = input("Are there any other bidders? Type 'yes' or 'no'\n")
    if answer == "yes":
        clear()
        name = input("What is your name?: ")
        bid = input("What's your bid? $")
        auction(name, bid)
        continue

    elif answer == "no":
        max = secret_auction[0][name]
        for i in range(len(secret_auction)):
            if secret_auction[0][name] < secret_auction[i][name]:
                max = secret_auction[i][name]
        print(f"The winner is {name} with a bid of {max}")
        break


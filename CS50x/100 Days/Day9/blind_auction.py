from gavel import logo
from replit import clear
print(logo)
print("Welcome to the secret auction program.")

def auction(input_name, input_bid):
    secret_auction.append({input_name : [input_bid] })

auction(name, bid)

while True:
    name = input("What is your name?: ")
    bid = input("What's your bid? $")
    secret_auction =[]
    answer = input("Are there any other bidders? Type 'yes' or 'no'\n")
    if answer == "yes":
        clear()
        continue
    elif answer == "no":
        print(secret_auction)
        print(secret_auction[0][name][0])
        max = secret_auction[0][name]
        for i in range(len(secret_auction)):
            if secret_auction[0][name] < secret_auction[i][name]:
                max = secret_auction[i][name]
        print(f"The winner is {secret_auction[i]} with a bid of {max}")
        break


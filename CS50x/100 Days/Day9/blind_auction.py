#from gavel import logo
from replit import clear
#print(logo)
print("Welcome to the secret auction program.")
name = input("What is your name?: ")
bid = input("What's your bid? $")
secret_auction =[]

def auction(input_name, input_bid):
    secret_auction.append({input_name : input_bid })
    print(secret_auction)


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


        break


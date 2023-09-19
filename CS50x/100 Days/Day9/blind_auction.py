from gavel import logo
from replit import clear
print(logo)
print("Welcome to the secret auction program.")
def auction(input_name):
    max = secret_auction[0][0]
    for i in range(len(secret_auction)):
        if secret_auction[0][0] < secret_auction[i][0]:
            max = secret_auction[i][0]
    print(secret_auction)
    print(f"The winner is {input_name} with a bid of {max}")

while True:
    name = input("What is your name?: ")
    bid = input("What's your bid? $")
    secret_auction = []
    secret_auction += {name : bid}
    answer = input("Are there any other bidders? Type 'yes' or 'no'\n")
    if answer == "yes":
        clear()
        name = input("What is your name?: ")
        bid = input("What's your bid? $")
        secret_auction = []
        secret_auction += {name : bid}
        continue

    elif answer == "no":
        auction()
        break



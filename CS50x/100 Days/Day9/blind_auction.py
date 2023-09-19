from gavel import logo
print(logo)
print("Welcome to the secret auction program.")
name = input("What is your name?: ")
bid = input("What's your bid? $")

def auction(input_name, input_bid):
    secret_auction ={}
    for key
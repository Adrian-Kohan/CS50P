# Getting valid input from user
while True:
    try:
        cash = float(input("Change owed: "))
        if cash > 0:
            break
        else:
            continue
    except ValueError:
        print("That's not a valid input! Please enter a valid amount")

# Changing the cash to cent
cent = (cash * 100)

# Calculating the number of coins
coins = 0
while cent > 0:
    if cent >= 25:
        cent -= 25
    elif cent >= 10:
        cent -= 10
    elif cent >= 5:
        cent -= 5
    else:
        cent -= 1
    coins += 1

# Printing the number of coins 
print(coins)
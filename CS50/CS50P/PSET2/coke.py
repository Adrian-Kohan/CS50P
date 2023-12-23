coke = 50


while coke != 0:
    if coin == 5 or coin == 10 or coin == 25:
        coke = coke - coin
        print(f"Amount Due: {coke}")
        coin = input(int("Inser Coin: "))

print("Change Owed: ")
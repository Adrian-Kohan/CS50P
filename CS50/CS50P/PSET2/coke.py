coke = 50
print(f"Amount Due: {coke}")
coin = input("Inser Coin: ")
coin = int(coin)

while coke != 0:
    if coin == 5 or coin == 10 or coin == 25:
            coke = coke - coin
            print(f"Amount Due: {coke}")
            coin = input("Inser Coin: ")
        print("Change Owed: ")

    else:
        pass
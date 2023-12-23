coke = 50


if coin == 5 or coin == 10 or coin == 25:
    while coke != 0:
        coke = coke - coin
        print(f"Amount Due: {coke}")
        coin = input(int("Inser Coin: "))
    print("Change Owed: ")

else:
    pass
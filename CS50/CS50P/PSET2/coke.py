coke = 50


while coke > 0:
    print(f"Amount Due: {coke}")
    coin = input("Inser Coin: ")
    coin = int(coin)


    if coin == 5 or coin == 10 or coin == 25:
        coke = coke - coin

if coke >= 0:
    print(f"Change Owed: {coke}")
else:
    coke *= -1
    print(f"Change Owed: {coke}")


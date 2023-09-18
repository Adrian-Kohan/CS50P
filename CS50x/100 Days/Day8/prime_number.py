n = int(input("Check this number: "))
def prime_checker(number):
    num = ""
    for i in range(2,number):
        if number % i == 0:
            num = "not a prime"
        else:
            num = "a prime"
    print(f"It's {num} number")

prime_checker(number = n)
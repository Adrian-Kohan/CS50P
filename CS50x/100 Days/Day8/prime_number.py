n = int(input("Check this number: "))
def prime_checker(number):
    for i in range(2,number):
        num = ""
        if number % i == 0 and i != number:
            num = "not a prime"
        print(f"It's {num} number")
        if number % i != 0:
            num = "a prime"
        print(f"It's {num} number")
prime_checker(number = n)
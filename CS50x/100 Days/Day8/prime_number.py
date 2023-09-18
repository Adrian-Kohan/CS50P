n = int(input("Check this number: "))
def prime_checker(number):
    if number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number == number * number or number != 2 or number != 3 or number != 5:
        print("It's not a prime number")
    else:
        print("It's a prime number")
prime_checker(number = n)
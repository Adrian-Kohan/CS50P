n = int(input("Check this number: "))
def prime_checker(number):
    for i in range(2,100):
        if number % i == 0 and i != number:
            print("It's not a prime number")
        else:
            print("It's a prime number")
prime_checker(number = n)
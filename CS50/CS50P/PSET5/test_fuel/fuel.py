def main():
    fraction = input("Fraction: ")
    fuel = convert(fraction)
    if type(fuel) == float:
        print(gauge(fuel))



def convert(fraction):
    fraction = fraction.split("/")
    x = int(fraction[0])
    y = int(fraction[1])

    if x <= y:
        return (x / y) * 100

    elif y == 0:
        return ZeroDivisionError

    else:
        return ValueError





def gauge(percentage):
    if percentage <= 1:
        return "E"

    elif percentage >= 99:
        return "F"

    else:
        return f'{round(percentage)}%'



if __name__ == "__main__":
    main()
def main():
    fraction = input("Fraction: ")
    print(convert(fraction))



def convert(fraction):
    fraction = fraction.split("/")
    x = int(fraction[0])
    y = int(fraction[1])

    if x <= y:
        return gauge((x / y) * 100)

    elif not str(x).isdigit() or not str(y).isdigit() or x > y:
        raise ValueError

    elif y == 0:
        raise ZeroDivisionError






def gauge(percentage):
    if percentage <= 1:
        return "E"

    elif percentage >= 99:
        return "F"

    else:
        return f'{round(percentage)}%'



if __name__ == "__main__":
    main()
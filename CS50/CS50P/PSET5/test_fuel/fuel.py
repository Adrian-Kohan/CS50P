def main():
    fraction = input("Fraction: ")
    print(convert(fraction))



def convert(fraction):
    fraction = fraction.split("/")
    x = int(fraction[0])
    y = int(fraction[1])

    if not x.isdigit() or not y.isdigit() or x > y:
        raise ValueError

    elif y == 0:
        raise ZeroDivisionError

    elif x <= y:
        return gauge((x / y) * 100)




def gauge(percentage):
    if percentage <= 1:
        return "E"

    elif percentage >= 99:
        return "F"

    else:
        return f'{round(percentage)}%'



if __name__ == "__main__":
    main()
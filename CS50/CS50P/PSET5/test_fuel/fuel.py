def main():
    while True:
        fraction = input("Fraction: ").split("/")
        gauge(convert(fraction))




def convert(fraction):
    try:
        x = int(fraction[0])
        y = int(fraction[1])
        if x <= y:
        return (x / y) * 100

    except (ValueError, ZeroDivisionError):
        return True




def gauge(percentage):
    if percentage <= 1:
        return "E"

    elif percentage >= 99:
        return "F"

    else:
        return f'{round(percentage)}%'



if __name__ == "__main__":
    main()


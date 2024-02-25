def main():
    while True:
        fraction = input("Fraction: ").split("/")




def convert(fraction):
    try:
        x = int(fraction[0])
        y = int(fraction[1])
        if x <= y:
        return (x / y) * 100

    except (ValueError, ZeroDivisionError):
        continue




def gauge(percentage):
    if percentage <= 1:
        return "E"
        break
    elif percentage >= 99:
        return "F"
        break
    else:
        return f'{round(percentage)}%'
        break


if __name__ == "__main__":
    main()


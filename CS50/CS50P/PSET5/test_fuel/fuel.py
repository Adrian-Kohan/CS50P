def main():
    while True:
        fraction = input("Fraction: ").split("/")




def convert(fraction):
    try:
        x = int(fraction[0])
        y = int(fraction[1])

    except (ValueError, ZeroDivisionError):
        continue

    if x <= y:
        fuel = (x / y) * 100
        if fuel <= 1:
            print("E")
            break
        elif fuel >= 99:
            print("F")
            break
        else:
            print(f'{round(fuel)}%')
            break


def gauge(percentage):
    ...


if __name__ == "__main__":
    main()


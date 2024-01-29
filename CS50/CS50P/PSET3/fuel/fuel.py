while True:
    fraction = input("Fraction: ")
    try:
        x = int(fraction[0])
        y = int(fraction[2])
        if x <= y:
            fuel = (x / y)
            if fuel <= 1:
                print(fuel)
                print("E")
                break
            elif fuel >= 99:
                print(fuel)
                print("F")
                break
            else:
                print(f'{round(fuel)}%')
                break

    except (ValueError, ZeroDivisionError):
            continue

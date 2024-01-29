while True:
    fraction = input("Fraction: ").split("/")
    try:
        x = int(fraction[0])
        y = int(fraction[1])
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

    except (ValueError, ZeroDivisionError):
            continue

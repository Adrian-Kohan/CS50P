def fun():
    fraction = input("Fraction: ")
    x = int(fraction[0])
    y = int(fraction[2])
    return x, y

try:
    fuel = (x / y) * 100
except (ValueError, ZeroDivisionError):
    fun()
    finally:
        if fuel <= 1:
            print("E")
        elif fuel >= 99:
            print("F")
        else:
            print(f'{round(fuel)}%')

else:
    fraction = input("Fraction: ")
    x = int(fraction[0])
    y = int(fraction[2])
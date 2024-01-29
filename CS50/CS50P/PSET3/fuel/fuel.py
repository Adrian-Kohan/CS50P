
try:
    fraction = input("Fraction: ")
    x = int(fraction[0])
    y = int(fraction[2])
    fuel = (x / y) * 100
except (ValueError, ZeroDivisionError):
    fraction = input("Fraction: ")
    x = int(fraction[0])
    y = int(fraction[2])
    fuel = (x / y) * 100



print(f'{round(fuel)}%')
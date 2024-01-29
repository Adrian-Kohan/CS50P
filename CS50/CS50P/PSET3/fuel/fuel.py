fraction = input("Fraction: ")
x = int(fraction[0])
y = int(fraction[2])

try:
    fuel = (x/y) * 100
except ValueError or ZeroDivisionError:
    fraction = input("Fraction: ")
    x = int(fraction[0])
    y = int(fraction[2])
    
print(f'{round(fuel)}%')
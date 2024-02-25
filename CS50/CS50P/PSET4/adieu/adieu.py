import inflect

p = inflect.engine()
names = []

try:
    while True:
        name = input("Enter: ")
        names.append(name)

except(EOFError):
    mylist = p.join((names))
    print(f"Adieu, adieu, to {mylist}")
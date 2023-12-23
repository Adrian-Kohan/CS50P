def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    index = 0
    if 2 <= len(s) <= 6 and s[0].isalpha() and s[1].isalpha and s[-1].isnumeric:
        for i in s:
            if i.isnumeric and
        return True






main()
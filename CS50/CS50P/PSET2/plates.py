def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    symbols = "'!?@#$%^&*()_-+=}{[]"'"'
    if 2 <= len(s) <= 6 and s[0].isalpha() and s[1].isalpha():
        for i in s:
            if i not in symbols:
                print(symbols)
                return True







main()
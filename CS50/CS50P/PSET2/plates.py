def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6 and s[0].isalpha() and s[1].isalpha and s[-1].isnumeric:
        for i in s:
            if i.isalpha
            if i.isnumeric:
                index_i = s.index(i)
                before_i = index_i - 1
                if s[before_i].isalpha and s[index_i] !=0:
                    return True







main()
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    symbols = "'!?@#$%^&*()/\_-+=}{[]"'"'
    is_true = 0
    if 2 <= len(s) <= 6:
        if s[0].isalpha() and s[1].isalpha():
            for i in s:
                if i not in symbols:
                    if i.isnumeric() and s[-1].isnumeric():
                        index_i = s.index(i)
                        before_i = index_i - 1
                        if s[before_i].isalpha() and s[index_i] !=0:
                            is_true += 1
                    if i.isalpha():
                        is_true += 1
    elif is_true != 0:
        return True








main()
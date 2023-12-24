def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    symbols = "'!?@#$%^&*()/\_-+=}{[]"'"'
    is_true = False

    if 2 <= len(s) <= 6:
        is_true = True
    else:
        is_true = False
        break

    for i in s:
        if i not in symbols:
             is_true = True
        else:
            is_true = False
            break

    if s[0].isalpha() and s[1].isalpha():
        is_true = True
    else:
        is_true = False
        break

    for i in s:
        if i.isalpha():
            is_true = True

        elif i.isnumeric() and s[-1].isnumeric():
            index_i = s.index(i)
            before_i = index_i - 1
            if s[before_i].isalpha() and s[index_i] !=0:
                is_true = True
            else:
                is_true = False
                break

    if is_true:
        return True
    else:
        return False








main()
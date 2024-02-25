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
        for i in s:
            # check if any character is symbol
            if i not in symbols:
                # check if the first two characters are alphabet
                if s[0].isalpha() and s[1].isalpha():
                    for i in s:
                        if i.isalpha():
                            is_true = True

                        elif i.isnumeric():
                            index_i = s.index(i)
                            before_i = index_i - 1
                            after_i = index_i + 1

                            # check if the number is not the last character and there is not a letter after that
                            if s.index(i) != s.index(s[-1]):
                                if s[after_i].isnumeric():
                                    is_true = True
                                else:
                                    is_true = False
                                    break

                            # check if first digit is 0 or not
                            if i == "0":
                                if s[before_i].isalpha():
                                    is_true = False
                                    break
                                else:
                                    is_true = True
                            else:
                                    is_true = True

                        else:
                            is_true = False
                            break
                else:
                    is_true = False
            else:
                is_true = False
    else:
        is_true = False



    if is_true:
        return True
    else:
        return False



if __name__ == "__main__":
    main()
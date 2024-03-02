import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r'^([0-9]{1}[0-9]?):?([0-9]?[0-9]?) (A?P?M) to ([0-9]{1}[0-9]?):?([0-9]?[0-9]?) (A?P?M)$',s):

        h1 = matches.group(1)
        m1 = matches.group(2)
        h2 = matches.group(4)
        m2 = matches.group(5)
        print(type(h1))

        if len(matches.group(1)) == 1:
            h1 = 0 + matches.group(1)

        if "PM" in matches.group(3):
                return f"{int(h1) + 12}:{m1}"

        elif "AM" in matches.group(3):
                return f"{h1}:{m1}"

        if len(matches.group(1)) == 1:
            h2 = 0 + matches.group(4)

        if "PM" in matches.group(6):
            return f"{int(h2) + 12}:{m2}"

        elif "AM" in matches.group(6):
            return f"{h2}:{m2}"


    else:
        raise ValueError

if __name__ == "__main__":
    main()
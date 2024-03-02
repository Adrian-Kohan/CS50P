import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r'^([0-9]{1}[0-9]?):?([0-9]?[0-9]?) (A?P?M) to ([0-9]{1}[0-9]?):?([0-9]?[0-9]?) (A?P?M)$',s):

        h1 = matches.group(1)
        m1 = matches.group(2)
        time1 = f"{h1}:{m1}"

        h2 = matches.group(4)
        m2 = matches.group(5)
        time2 = f"{h2}:{m2}"

        if len(h1) == 1:
            h1 = "0" + h1

        if "PM" in matches.group(3):
            h1 = int(h1) + 12

        if len(m1) == 0:
            time1 = h1

        if len(h2) == 1:
            h2 = "0" + h2

        if "PM" in matches.group(6):
            h2 = int(h2) + 12

        if len(m2) == 0:
            time1 = h1

        

    else:
        raise ValueError

if __name__ == "__main__":
    main()
import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r'^([0-9]{1}[0-9]?(?::[0-9][0-9])?) (A?P?M) to ([0-9]{1}[0-9]?(?::[0-9][0-9])?) (A?P?M)$',s):
        if "PM" in matches.group(2):



...


if __name__ == "__main__":
    main()
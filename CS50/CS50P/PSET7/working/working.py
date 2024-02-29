import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r'^([1-9]{1}[0-9]?(?::00)?) (A?P?M) to ([1-9]{1}[0-9]?(?::00)?) (A?P?M)$',s):
        if "PM" in matches.group(2):



...


if __name__ == "__main__":
    main()
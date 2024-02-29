import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r'^[0-9]*[0-9]?:?(?:00)? A?P?M to [0-9]*[0-9]?:?(?:00)? A?P?M$',s):



...


if __name__ == "__main__":
    main()
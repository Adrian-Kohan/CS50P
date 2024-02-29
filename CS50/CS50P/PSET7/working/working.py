import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    time1 = ""
    time2 = ""
    if matches := re.search(r'^([0-9]{1}[0-9]?):?([0-9]?[0-9]?) (A?P?M) to ([0-9]{1}[0-9]?):?([0-9]?[0-9]?) (A?P?M)$',s):
        if "PM" in matches.group(3):
            time1 = f"{int(matches.group(1)) + 12}:{matches.group(2)}"

        elif "PM" in matches.group(6):
            time2 = f"{int(matches.group(1)) + 12}:{matches.group(2)}"



...


if __name__ == "__main__":
    main()
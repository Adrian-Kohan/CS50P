import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r'^[a-z0-9_]+\wsrc="https?://(?:www\.)?youtube.com/embed/([a-z0-9_]+)"$',s):



...


if __name__ == "__main__":
    main()
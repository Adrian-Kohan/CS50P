import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r'^<iframe.+\wsrc="https?://(?:www\.)?youtube.com/embed/([a-z0-9_]+)".+></iframe>$',s):
        return f"https://youtube.com/{matches.group(1)}"
    else:
        return None



if __name__ == "__main__":
    main()
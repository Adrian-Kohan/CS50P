import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r'^<iframe\w([a-z0-9_]="."\w)*src="https?://(?:www\.)?youtube.com/embed/([a-z0-9_]+)".*></iframe>$',s):
        return f"https://youtu.be/{matches.group(1)}"
    else:
        sys.exit



if __name__ == "__main__":
    main()
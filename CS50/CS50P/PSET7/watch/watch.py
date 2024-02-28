import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r'^<iframe\w*=*"*.*"* src="https?://(?:www\.)?youtube.com/embed/(\w+)"\w*=*"*.*"*></iframe>$',s):
        return f"https://youtu.be/{matches.group(1)}"
    else:
        sys.exit



if __name__ == "__main__":
    main()
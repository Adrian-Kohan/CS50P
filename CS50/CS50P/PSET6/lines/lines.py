import sys


if len(sys.argv) == 0:
    print("Too few command-line arguments")

if ".py" is not in sys.argv[1]:
    print("Not a python file")

with open(sys.argv[1], "r") as code:
    data = json.load(code)
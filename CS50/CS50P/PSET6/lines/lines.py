import sys


if len(sys.argv) == 0:
    sys.exit("Too few command-line arguments")

if ".py" is not in sys.argv[1]:
    sys.exit("Not a python file")

else:
    with open(sys.argv[1], "r") as code:
        data = code.readlines()
        lines = 0
        for i in data:
            if data[0] == "#":
                pass
            elif data is not None:
                lines += 1

        print(lines)
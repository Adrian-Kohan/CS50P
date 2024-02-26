import sys


try:
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    elif ".py" not in sys.argv[1]:
        sys.exit("Not a python file")

    else:
        with open(sys.argv[1], "r") as code:
            data = code.readlines()
            lines = 0
            for i in data:
                if i[0] == "#" and  i[1] != "#":
                    pass
                elif i[0] == " ":
                    pass
                elif i == "\n":
                    pass
                else:
                    lines += 1

            print(lines)

except(FileNotFoundError):
    print("File does not exist")
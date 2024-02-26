import sys
from tabulate import tabulate
import pandas


if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

elif ".csv" not in sys.argv[1]:
    sys.exit("Not a python file")

else:
    try:

        data = pandas.read_csv(ys.argv[1])
        print(data)
        headers = data[0]
        print(tabulate(data, headers, tablefmt="grid"))


    except(FileNotFoundError):
        print("File does not exist")
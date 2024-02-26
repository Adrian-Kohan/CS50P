import sys
from tabulate import tabulate
import csv


if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

elif ".csv" not in sys.argv[1]:
    sys.exit("Not a python file")

else:
    try:
        with open(sys.argv[1], "r") as table:
            data = list(csv.DictReader(table, delimiter=","))
            headers = list(data[0].keys())
            print(headers)
            print(tabulate(data, headers=headers, tablefmt="grid"))


    except(FileNotFoundError):
        print("File does not exist")
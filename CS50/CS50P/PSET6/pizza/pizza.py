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
            data = csv.DictReader(table, delimiter=",")
            print(tabulate(data, headers="Keys", tablefmt="grid"))


    except(FileNotFoundError):
        print("File does not exist")
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

            dict_from_csv = dict(list(data)[0])
            list_of_column_names = list(dict_from_csv.keys())

            print(tabulate(data, headers=list_of_column_names, tablefmt="grid"))


    except(FileNotFoundError):
        print("File does not exist")
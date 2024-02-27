import sys
import csv


if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")


else:
    try:
        with open(sys.argv[1], "r") as data_1:
            dataset1 = list(csv.DictReader(data_1, delimiter=","))

        with open(sys.argv[2], "r") as data_2:
            dataset2 = list(csv.DictReader(data_2, delimiter=","))



    except(FileNotFoundError):
        sys.exit("File does not exist")
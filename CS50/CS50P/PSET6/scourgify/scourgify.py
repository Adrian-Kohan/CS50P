import sys
import csv


if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")


else:
    try:
        with open(sys.argv[1], sys.argv[2], "r") as data_1:
            dataset1 = list(csv.DictReader(data_1, delimiter=","))
            dataset2 = list(csv.DictReader(data_2, delimiter=","))

            print(dataset1)
            print(dataset2)


    except(FileNotFoundError):
        sys.exit("File does not exist")
import sys
import csv


if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")


else:
    try:
        with open(sys.argv[1], "r") as data_1:
            dataset1 = list(csv.DictReader(data_1, delimiter=","))
            for i in dataset1:
                new_name = i["name"].split(", ")
                with open(sys.argv[2], "w") as data_2:
                    dataset2 = list(csv.DictReader(data_2, delimiter=","))
                    first = new_name[0]
                    last = new_name[1]



            print(dataset1)
            print(dataset2)


    except(FileNotFoundError):
        sys.exit(f"Could not read {sys.argv[1]}")
import sys
import csv


if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")


else:
    try:
        dataset2 = []
        with open(sys.argv[1], "r") as data_1:
            dataset1 = list(csv.DictReader(data_1, delimiter=","))

            for i in dataset1:
                new_name = i["name"].split(", ")
                first = new_name[1]
                last = new_name[0]
                house = i["house"]

                dataset2.append({"first": first, "last": last, "house": house})

        with open('after.csv', 'w', newline='\n') as data_2:
            for i in dataset2:
                writer = csv.DictWriter(data_2, fieldnames=i.keys())
                writer.writeheader()
                writer.writerow(i)

    except(FileNotFoundError):
        sys.exit(f"Could not read {sys.argv[1]}")
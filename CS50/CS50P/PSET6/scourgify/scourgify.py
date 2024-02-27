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
                first = new_name[1]
                last = new_name[0]
                house = i["house"]

                new_data = {"first": first, "last": last, "house": house}

                with open('after.csv', 'w', newline='') as data_2:
                    writer = csv.DictWriter(data_2, fieldnames=new_data.keys())
                    writer.writeheader()
                    writer.writerow(new_data)

    except(FileNotFoundError):
        sys.exit(f"Could not read {sys.argv[1]}")
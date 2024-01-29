months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ")
    try:
        if "/" in date:
            new_date = date.split("/")
            month = new_date[0]
            day = new_date[1]
            year = new_date[2]

        elif "," in date:
            new_date = date.split(" ")
            month = new_date[0]
            day = new_date[1]
            year = new_date[2]

    except :
        continue

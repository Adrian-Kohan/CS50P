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
            print(f"{year}/{month}/{day}")
            break
        elif "," in date:
            new_date = date.split(" ")
            month = new_date[0]
            day = new_date[1].split(",")
            new_day = day[0]
            year = new_date[2]
            if month.title() in months:
                print(f"{year}/{months.index(month.title()) + 1}/{new_day}")
                break
            else:
                continue
    except :
        continue

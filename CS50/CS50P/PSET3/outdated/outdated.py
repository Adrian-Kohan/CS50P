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
    date = input("Date: ").lower()
    try:
        if "/" in date:
            new_date = date.split("/")
            month = new_date[0]
            day = new_date[1]
            year = new_date[2]

            if int(day) <= 31 and int(month) < 13:
                if 0 < int(day) < 10:
                    day = "0" + day

                if 0 < int(month) < 10:
                    month = "0" + month

                print(f"{year}-{month}-{day}")
                break

        elif "," in date:
            new_date = date.split(" ")
            year = new_date[2]
            month = new_date[0].title()
            new_month = months.index(month) + 1
            day = new_date[1].split(",")
            new_day = day[0]

            if month in months and int(new_day) <= 31:
                if 0 < int(new_day) < 10:
                    new_day = "0" + new_day

                if 0 < new_month < 10:
                    new_month = "0" + str(new_month)

                print(f"{year}-{new_month}-{new_day}")
                break
    except:
        continue

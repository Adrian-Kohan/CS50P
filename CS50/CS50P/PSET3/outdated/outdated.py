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

            if int(day) <= 31:
                if 0 < int(day) < 10:
                    day = 0 + day

                if 0 < int(month) < 10:
                    month = 0 + month

                print(f"{year}-{month}-{day}")
                break

        elif "," in date:
            new_date = date.split(" ")
            month = new_date[0]
            day = new_date[1].split(",")
            new_day = day[0]
            year = new_date[2]

            if month.title() in months and int(new_day) <= 31:
                if 0 < int(new_day) < 10:
                    new_day = 0 + new_day

                if 1 <= months.index(month.title()) < 10:
                    month = 0 + str(months.index(month.title()) + 1)

                print(f"{year}-{month}-{new_day}")
                break
    except:
        continue

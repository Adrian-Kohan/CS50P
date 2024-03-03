from datetime import date, timedelta
import sys


def main():
    try:
        user_birth_date = date(input("Date of birth: "))
        today = date.today()

        year1, month1, day1 = user_birth_date.split("-")
        year2, month2, day2 = today.split("-")

        diff_year = year2 -year1
        diff_month = month2 - month1
        diff_day = day2 - day1

        time_delta1 = timedelta(years= days=23, hours=0, minutes=20)
        time_delta2 = timedelta(days=15, seconds=2, microseconds=123, milliseconds=234566, minutes=5, hours=2)

        result = time_delta1 - time_delta2
        print(today)
    except:
        sys.exit "Invalid date"




if __name__ == "__main__":
    main()
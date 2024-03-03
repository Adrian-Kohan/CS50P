from datetime import date, timedelta
import sys


def main():
    user_birth_date = input("Date of birth: ")
    today = date.today()

    try:
        year, month, day = user_birth_date.split("-")

        if birth_date := date(int(year), int(month), int(day)):
            days = abs(birth_date - today).days
            days_in_min = days * 24 * 60
            



    except:
        sys.exit ("Invalid date")



if __name__ == "__main__":
    main()
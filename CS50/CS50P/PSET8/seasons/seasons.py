from datetime import date
import sys


def main():
    try:
        user_birth_date = date(input("Date of birth: "))
        today = date.today()

        year1, month1, day1 = user_birth_date.split("-")
        year2, month2, day2 = today.split("-")
        years_in_min = (year2 -year1) * 365
        print(today)
    except:
        sys.exit "Invalid date"




if __name__ == "__main__":
    main()
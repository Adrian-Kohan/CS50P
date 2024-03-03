from datetime import date, timedelta
import sys


def main():
    user_birth_date = input("Date of birth: ")
    today = date.today()

    try:
        if date(user_birth_date):

            year1, month1, day1 = user_birth_date.split("-")
            year2, month2, day2 = today.split("-")


            time_delta1 = timedelta(year1, month1, day1)
            time_delta2 = timedelta(year2, month2, day2)

            result = time_delta1 - time_delta2
            print(result)
    except:
        sys.exit ("Invalid date")




if __name__ == "__main__":
    main()
from datetime import date, timedelta
import sys


def main():
    user_birth_date = date(input("Date of birth: "))
    today = date.today()
    # try:
        # if date(int(user_birth_date)):



    time_delta1 = timedelta(user_birth_date.year, user_birth_date.month, user_birth_date.day)
    time_delta2 = timedelta(today.year, today.month, today.day)

    result = time_delta1 - time_delta2
    print(result)
    # except:
    #     sys.exit ("Invalid date")




if __name__ == "__main__":
    main()
from datetime import date
import sys
import inflect


def main():
    user_birth_date = input("Date of birth: ")
    today = date.today()
    print(convert(user_birth_date, today))


def convert(date1, date2):
    inflector = inflect.engine()

    try:
        year, month, day = date1.split("-")

        # check if user iput the correct format of date
        if birth_date := date(int(year), int(month), int(day)):

            # returns a timedelta object
            days = abs(birth_date - date2).days

            # turn the days in minutes
            days_in_min = days * 24 * 60

            # turn numerical numbers to English words
            words = inflector.number_to_words(days_in_min).capitalize() + " minutes"
            return words


    except:
        sys.exit ("Invalid date")

if __name__ == "__main__":
    main()
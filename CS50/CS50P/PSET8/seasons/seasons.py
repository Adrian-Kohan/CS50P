from datetime import date
import sys
import inflect


def main():
    user_birth_date = input("Date of birth: ")
    today = date.today()

    try:
        year, month, day = user_birth_date.split("-")

        if birth_date := date(int(year), int(month), int(day)):

            # returns a timedelta object
            days = abs(birth_date - today).days

            days_in_min = days * 24 * 60

            inflector = inflect.engine()
            words = inflector.number_to_words(days_in_min)
            words = words.replace("and", "")
            print(words)


    except:
        sys.exit ("Invalid date")


if __name__ == "__main__":
    main()
from datetime import date
import sys
import inflect


def main():
    user_birth_date = input("Date of birth: ")
    today = date.today()

    try:
        year, month, day = user_birth_date.split("-")

        if birth_date := date(int(year), int(month), int(day)):
            days = abs(birth_date - today).days
            days_in_min = days * 24 * 60

            inflector = inflect.engine()
            words = inflector.number_to_words(days_in_min)
            print(words)


    except:
        sys.exit ("Invalid date")


if __name__ == "__main__":
    main()
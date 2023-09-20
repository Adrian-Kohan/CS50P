year = int(input("Enter a year. "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("It's a leap year")
        else:
            print("It's not a leap year")
    else:
        print("It's a leap year")
else:
    print("It's not a leap year")

def days_in_month():
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, ]
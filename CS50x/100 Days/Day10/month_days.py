def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(input_year, input_month):
    """"This function return the number of days in month based on the year"""
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(input_year) == True:
        month_days[1] = 28
        return month_days[input_month -1]
    return month_days[input_month -1]
#or
#if leap_year and input_month == 2:
    #return 29
#return month_days[input_month -1]

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
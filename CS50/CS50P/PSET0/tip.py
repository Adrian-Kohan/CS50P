def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d.replace("$", "")
    d  = int(d)
    return d:.1f


def percent_to_float(p):
    d.replace("%", "")
    d  = int(d) / 100
    return d:.2f


main()
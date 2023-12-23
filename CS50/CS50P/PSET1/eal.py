def main():
    time = input("What time is it? ")
    time = conver(time)

    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")
    else:
        pass


def convert(time):
    time_list = time.split(":")
    hour = int(time_list[0])
    min = int(time_list[1])
    if min == 30:
        return float(f"{hour}.5")
    else:
        return float(f"{hour}.{min}")


if __name__ == "__main__":
    main()
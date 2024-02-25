def main():
    greeting = input("Greeting: ").lower()
    print(f"{value(greeting)}")


def value(greeting):
    first_h = greeting[0]

    if "hello" in greeting:
        return "$0"
    elif first_h == "h":
        return "$20"
    else:
        return "$100"


if __name__ == "__main__":
    main()
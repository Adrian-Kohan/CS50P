import validators

def main():
    email = input("What's your email address? ")

    if validators.email(email):
        return Valid
    else:
        return Invalid



if __name__ == "__main__":
    main()
import validators

def main():
    email = input("What's your email address? ")

    if validators.email(email):
        return "\nValid"
    else:
        return "\nInvalid"



if __name__ == "__main__":
    main()
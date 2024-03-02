import validators

def main():
    user_email = input("What's your email address? ")

    if validators.email(user_email):
        return "\nValid"
    else:
        return "\nInvalid"



if __name__ == "__main__":
    main()
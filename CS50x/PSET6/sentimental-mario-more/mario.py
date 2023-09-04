# getting the height of pyramid from user while it isn't in range 1-8 and it isn't a number
while True:
    try:
        h = int(input("Height: "))
        # if the input height was number and was in range print the pyramid
        if (0 < h < 9):
            for i in range(h):
                print((h - 1 - i) * " " + (i + 1) * "#" + "  " + (i + 1) * "#")
            break

    except ValueError:
        print("That's not a valid input! Please enter a number between 1 and 8.")
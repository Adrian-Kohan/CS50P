from random import randint

# Take input until the level format is correct
while True:
    level = input("Level: ")
    if level.isdigit():
        level = int(level)
        if level > 0:
            # Generate a random number in the given range
            number = randint(1, level + 1)

            # Check until the guessed number is correct
            while True:
                guess = input("Guess: ")
                if guess.isdigit():
                    guess = int(guess)
                    if guess > number:
                        print("Too large!")
                    elif guess < number:
                        print("Too small!")
                    else:
                        print("Just right!")
                        break
            break
import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
random_number = random.choice(1, 101)
user_choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
if user_choice == "hard":
    print("You have 5 attempts remaining to guess the number.")
    number_of_attempts = 5
elif user_choice == "easy":
    print("You have 10 attempts remaining to guess the number.")
    number_of_attempts = 10

def game(number_of_attempts):
    end_of_game = False
    while not end_of_game or number_of_attempts != 0:
        guess = int(input("Make a guess: "))
        if guess > random_number:
            return "Too high"
        elif guess < random_number:
            return "Too low"
        else:
            end_of_game = True
            return

        remaining_attempts = number_of_attempts - 1
        print(f"You have {remaining_attempts} attempts remaining to guess the number.")
        
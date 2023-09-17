import random

word_list = ["ardvark", "baboon", "camel"]
#randomly chosen a word from word_list and assign it to a variable named word_chosen
chosen_word = random.choice(word_list)
print(chosen_word)
#ask the user to guess a letter and assign it to a variable called guess. make guess lowercase
guess = input("Guess a letter: ").lower()
guess_list = []
for i in chosen_word:
    guess_list.append("_")
    #or guess_list += "_"
    
#check if the letter user guessed is one of the lettere in the chosen word
for i in range(len(chosen_word)):
    if guess == chosen_word[i]:
        guess_list[i] = guess
        i += 1
print(guess_list)

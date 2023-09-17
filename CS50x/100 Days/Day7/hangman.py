import random

word_list = ["ardvark", "baboon", "camel"]
stages =['''
      _______
     |/      |
     |       O
     |
     |
     |
     |
     |___
         ''',
         '''
      _______
     |/      |
     |       O
     |       |
     |
     |
     |
     |___
         ''',
         '''
      _______
     |/      |
     |       O
     |       |/
     |
     |
     |
     |___
         ''',
         '''
      _______
     |/      |
     |       O
     |      \|/
     |
     |
     |
     |___
         ''',
         '''
      _______
     |/      |
     |       O
     |      \|/
     |       |
     |
     |
     |___
         ''',
         '''
      _______
     |/      |
     |       O
     |      \|/
     |       |
     |      /
     |
     |___
         ''',
         '''
      _______
     |/      |
     |       O
     |      \|/
     |       |
     |      / \
     |
     |___
         '''
         ]
lives = 6
#randomly chosen a word from word_list and assign it to a variable named word_chosen
chosen_word = random.choice(word_list)
print(chosen_word)

guess_list = []
for i in chosen_word:
    guess_list.append("_")
    #or guess_list += "_"
#ask the user to guess a letter and assign it to a variable called guess. make guess lowercase
s = 0
while "_" in guess_list:
    guess = input("Guess a letter: ").lower()
    #check if the letter user guessed is one of the lettere in the chosen word
    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                guess_list[i] = guess
        print(guess_list)

    elif guess not in chosen_word and lives != 0:
        lives -= 1
        print(stages[s])
        s += 1

    elif lives == 0:
        print(f"{stages[5]}\n You loose.")

    elif "_" not in guess_list:
        print("You win.")


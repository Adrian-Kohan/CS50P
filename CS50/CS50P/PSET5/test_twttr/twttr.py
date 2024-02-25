def main():
    user_input = input("Input: ")
    print(f"{shorten(user_input)}")



def shorten(word):
    vowels = ["o", "a", "u", "e", "i", "O", "A", "U", "E", "I"]
    new_word = word
    for char in word:
        if char in vowels:
            new_word = new_word.remove(char, "")
            return new_word


if __name__ == "__main__":
    main()



print(f"Output: {input}")
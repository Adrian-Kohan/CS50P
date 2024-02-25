def main():
    user_input = input("Input: ")
    print(f"Output: {shorten(user_input)}")



def shorten(word):
    vowels = ["o", "a", "u", "e", "i",]
    new_word = word
    for char in new_word:
        if char in vowels:
            new_word = new_word.replace(char, "")
    return new_word


if __name__ == "__main__":
    main()
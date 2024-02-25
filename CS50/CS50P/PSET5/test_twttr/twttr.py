def main():
    user_input = input("Input: ")
    shorten(user_input)
    



def shorten(word):
    vowels = ["o", "a", "u", "e", "i", "O", "A", "U", "E", "I", "O"]

    for char in word:
        if char in vowels:
            return word.replace(char, "")


if __name__ == "__main__":
    main()



print(f"Output: {input}")
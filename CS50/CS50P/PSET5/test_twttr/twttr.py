

input = input("Input: ")
vowels = ["o", "a", "u", "e", "i", "O", "A", "U", "E", "I", "O"]

for char in input:
    if char in vowels:
        input = input.replace(char, "")

print(f"Output: {input}")
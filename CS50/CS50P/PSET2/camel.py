camelCase = input("camelCase: ")

while camelCase.isupper():
    for char in camelCase:
        camelCase = camelCase.replace(char, f"_{char.lower()}")

print(f"snake_case: {camelCase}")


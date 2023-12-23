camelCase = input("camelCase: ")

while camelCase.isupper():
    for char in camelCase:
        camelCase = camelCase.replace(ch, f"_{ch.lower()}")

print(f"snake_case: {camelCase}")

    
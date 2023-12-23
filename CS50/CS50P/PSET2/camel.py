camelCase = input("camelCase: ")

for ch in camelCase:
    if ch.isupper():
        camelCase = camelCase.replace(ch, f"_{ch.lower()}")

print(f"snake_case: {camelCase}")

    
camelCase = input("camelCase: ")

for ch in camelCase:
    if ch.isupper():
        snake_case = camelCase.replace(ch, f"_{ch.lower()}")
        print(f"snake_case: {snake_case}")
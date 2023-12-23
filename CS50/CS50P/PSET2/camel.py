camelCase = input("camelCase: ")

for ch in camelCase:
    while ch.isupper():
        snake_case = camelCase.replace(ch, f"_{ch.lower()}")
    print(f"snake_case: {snake_case}")
    if not ch.isupper():
        snake_case = camelCase
        print(f"snake_case: {snake_case}")
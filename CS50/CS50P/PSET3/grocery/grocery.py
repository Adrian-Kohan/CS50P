shopping_list = []
while True:
    try:
        item = input()
        shopping_list.append(item.upper())
    except EOFError:
        shopping_list.sort()
        for item in shopping_list:
            print(f"{shopping_list.count(item)} {item}")
        break
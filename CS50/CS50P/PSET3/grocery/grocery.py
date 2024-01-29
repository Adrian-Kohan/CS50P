shopping_list = []
while True:
    item = input()
    try:
        shopping_list.append(item.upper())
    except EOFError:
        shopping_list.sort()
        for item in shopping_list:
            print(item)
        break
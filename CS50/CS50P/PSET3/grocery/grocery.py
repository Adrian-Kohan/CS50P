shopping_list = []
while True:
    try:
        item = input().lower()
        shopping_list.append(item.upper())
    except EOFError:
        shopping_list.sort()
        break
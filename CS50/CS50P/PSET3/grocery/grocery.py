shopping_list = []
while True:
    try:
        item = input()
        shopping_list.append(item.upper())
    except EOFError:
        shopping_list.sort()
        final_list = []
        for item in shopping_list:
            item_count = f"{shopping_list.count(item)} {item}"
            if item_count not in final_list:
                final_list.append(item_count)
        for item in final_list:
            print(item)

        break
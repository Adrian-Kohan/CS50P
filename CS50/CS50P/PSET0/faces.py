def convert(text):
    if ":)" in text and ":(" in text:
        return text.replace(":)" ,"🙂") and text.replace(":(" ,"🙁")
    elif ":)" in text:
        return text.replace(":)" ,"🙂")
    elif ":(" in text:
        return text.replace(":(" ,"🙁")
    else:
        return text


text = input()
print(convert(text))
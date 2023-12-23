expression = input("Expression: ")
x = int(expression[0])
z = int(expression[4])

if "+" in expression:
    print(f"{x}+{z}")
elif "-" in expression:
    print(f"{x}-{z}")
elif "*" in expression:
    print(f"{x}*{z}")
else:
    print(f"{x}/{z}")

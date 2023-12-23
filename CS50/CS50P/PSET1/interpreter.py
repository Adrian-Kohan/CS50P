expression = input("Expression: ")
x = int(expression[0])
z = int(expression[4])

if "+" in expression:
    result = float("{:.1f}".format(x+z))
    print(result)
elif "-" in expression:
    result = float("{:.1f}".format(x-z))
    print(result)
elif "*" in expression:
    result = float("{:.1f}".format(x*z))
    print(result)
else:
    result = float("{:.1f}".format(x/z))
    print(result)

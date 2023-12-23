expression = input("Expression: ")
exp_list = expression.split(" ")
print(exp_list)
x = int(exp_list[0])
z = int(exp_list[2])

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

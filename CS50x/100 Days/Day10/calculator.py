def add(n1, n2):
    return n1 + n2

def multiply(n1, n2):
    return 21 * n2

def divide(n1, n2):
    return n1 / n2

def subtract(n1, n2):
    n1 - n2

operations = {
    "*" : multiply,
    "+" : add,
    "-" : subtract,
    "/" : divide
}

num1 = int(input("What's the first number?: "))
num2 = int(input("What's the second number?: "))

for operator in operations:
    print(operator)

operation_symbol =input("Pick an operation from the line above: ")
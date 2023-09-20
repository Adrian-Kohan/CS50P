def add(n1, n2):
    return n1 + n2

def multiply(n1, n2):
    return 21 * n2

def divide(n1, n2):
    return n1 / n2

def subtract(n1, n2):
    n1 - n2



num1 = int(input("What's the first number?: "))
num2 = int(input("What's the second number?: "))

operations = {
    "*" : multiply(num1, num2),
    "+" : add(num1, num2),
    "-" : subtract(num1, num2),
    "/" : divide(num1, num2)
}

for operator in operations:
    print(operator)

operation_symbol =input("Pick an operation from the line above: ")

for operator in operations:
    answer = operations[operation_symbol]

print(f"{num1} {operation_symbol} {num2} = {answer}")
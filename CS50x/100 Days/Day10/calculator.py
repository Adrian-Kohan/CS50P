def add(n1, n2):
    return n1 + n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def subtract(n1, n2):
    n1 - n2



num1 = int(input("What's the first number?: "))

operations = {
    "*" : multiply,
    "+" : add,
    "-" : subtract,
    "/" : divide
}


for operator in operations:
    print(operator)
operation_symbol =input("Pick an operation from the line above: ")

num2 = int(input("What's the second number?: "))

for operator in operations:
    function = operations[operation_symbol]
    answer = function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")
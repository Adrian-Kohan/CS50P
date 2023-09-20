def add(n1, n2):
    return n1 + n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def subtract(n1, n2):
    return n1 - n2

operations = {
    "*" : multiply,
    "+" : add,
    "-" : subtract,
    "/" : divide
}

continue_calculating = True

while continue_calculating:
    num1 = int(input("What's the first number?: "))
    for operator in operations:
        print(operator)

    operation_symbol =input("Pick an operation from the line above: ")
    num2 = int(input("What's the second number?: "))

    for operator in operations:
        function = operations[operation_symbol]
        answer = function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")
    anwser2 = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ")

    if anwser2 == 'n':
        continue_calculating = False


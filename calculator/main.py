# Simple calculator that can add, subtract, multiply, and divide two numbers
# imported art file provided by 100 days of Code written by Dr. Angela Yu

import art


def add(n1, n2):
    return n1 + n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def subtract(n1, n2):
    return n1 - n2

operations = {
    "+" : add,
    "-" : subtract,
    "/" : divide,
    "*" : multiply
}

def main():
    print(art.logo)
    accumulate = True
    n1 = float(input("What's the first number?: "))

    while accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        n2 = float(input("Whats the next number?: "))
        answer = operations[operation_symbol](n1, n2)
        print(f"{n1} {operation_symbol} {n2} = {answer}")
        question = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculator: ")
        if question == "y":
            n1 = answer
        else:
            accumulate = False
            print("\n" * 30)
            main()

main()

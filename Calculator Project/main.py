import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2
#----------------------------------

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}
#mathematical part below
def math_func():
    print(art.logo)
    n1 = int(input("What is the first number: "))
    operator = input("Enter the operator: ( +, -, *, or / ): ")
    n2 = int(input("What is the second number: "))
    working_number = operations[operator](n1, n2)
    print(operations[operator](n1, n2))
    keep_going = input("Do you want to keep using this number?: y/n ")

    while keep_going == "y":
        n1 = working_number
        operator = input("Enter the operator: ( +, -, *, or / ): ")
        n2 = int(input("What is the next number: "))
        working_number = operations[operator](n1, n2)
        print(operations[operator](n1, n2))
        keep_going = input("Do you want to keep using this number?: y/n ")
    math_func()

math_func()
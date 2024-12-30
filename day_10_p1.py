
'''
def function():
    result = 3 * 4 
    return result
function()

def title_case(first_name, last_name):
    print(first_name.title())
    print(last_name.title())
title_case("kaLEab", "ZEWDIE")


def title_case(first_name, last_name):
    f_name = first_name.title()
    l_name = first_name.title()
    print(f"{f_name} {l_name}")
title_case("kaLEab", "ZEWDIE")
# ''''''''''''''''''''''''''''''''''''''
def function_1(text):
    output = text + text
    return output

func = function_1("hello")
print(func)

'''
# ..........................................


    # Addition
def add(num1, num2):
    return int(num1) + int(num2)

# Multiplication
def mult(num1, num2):
    return num1 * num2

# Subtraction
def subt(num1, num2):
    return num1 - num2

# Division
def div(num1, num2):
    return num1 / num2

# Dictionary mapping operators to actual functions
operations = {
    "-": subt,
    "+": add,
    "*": mult,
    "/": div
}

    # Main program
def calculator():
    num1 = float(input("What is the first number? "))

    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        operation_symbol = input("Pick one of the operation symbols: ")
        num2 = float(input("What is the second number? "))

        # Get the function from the dictionary
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        # Check if the user wants to continue
        if input(f"Type 'y' to continue calculating with {answer}, or 'n' to continue with new calculation.: ") == "y":
            num1 = answer
        else: 
            calculator()

calculator()

logo = '''
 ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗
██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██║     ███████║██║     ██║     ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝
██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗
╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║
 ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝

'''

print(logo)


def add(a, b):
    """
    Add two numbers.
    Args:
        a (int): The first number.
        b (int): The second number.
    Returns:
        int: The sum of the two numbers.
    """
    return a + b


def subtract(a, b):
    """
    Subtract two numbers.
    Args:
        a (int): The first number.
        b (int): The second number.
    Returns:
        int: The difference of the two numbers.
    """
    return a - b


def multiply(a, b):
    """
    Multiply two numbers.
    Args:
        a (int): The first number.
        b (int): The second number.
    Returns:
        int: The product of the two numbers.
    """
    return a * b


def divide(a, b):
    """
    Divide two numbers.
    Args:
        a (int): The first number.
        b (int): The second number.
    Returns:
        int: The quotient of the two numbers.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


operator = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

init_number = float(input("Enter the first number: "))
while True:
    operator_input = input("Enter the operator (+, -, *, /): ")
    if operator_input not in operator:
        print("Invalid operator")
    else:
        next_number = float(input("Enter the next number: "))
        result = operator[operator_input](init_number, next_number)
        print(f"The result is: {result}")
        print("Do you want to continue? (y/n) or restart with 'r'")
        choice = input().lower()
        if choice == 'r':
            init_number = float(input("Enter the new first number: "))
            continue
        elif choice == 'y':
            init_number = result
            continue
        else:
            print("Exiting the calculator.")
            break

def catch_number(message):
    while True:
        try:
            input_message = input(message)
            return float(input_message)
        except ValueError:
            print("Invalid value: Enter a number")
        except KeyboardInterrupt:
            print("Input canceled")
            return 0


def add(current, new_number):
    result = current + new_number
    print(f"The sum of:  {current} + {new_number} = {result}")
    return result

def subtract(current, new_number):
    result = current - new_number
    print(f"The subtraction of:  {current} - {new_number} = {result}")
    return result

def multiply(current, new_number):
    result = current * new_number
    print(f"The multiply of:  {current} x {new_number} = {result}")
    return result

def divide(current, new_number):
    if new_number == 0:
        print("Cannot divide by zero")
        return current
    result = current / new_number
    print(f"The division of:  {current} / {new_number} = {result}")
    return result

operations = {
    "A": add,
    "S": subtract,
    "M": multiply,
    "D": divide,
}

current_number = None

while True:
    print("""
Select an operation:

A = Add
S = Subtract
M = Multiply
D = Divide
N = New starting number
X = Exit the calculator
""")

    select = input("Enter your option: ").strip().upper()

    if select in operations:
        if current_number is None:
            num1 = catch_number("Enter the first number: ")
            num2 = catch_number("Enter the second number: ")
            current_number = operations[select](num1, num2)
        else:
            print(f"Current number: {current_number}")
            new_number = catch_number("Enter the next number: ")
            current_number = operations[select](current_number, new_number)

    elif select == "N":
        current_number = catch_number("Enter a new starting number: ")
    
    elif select == "X":
        print("Exiting calculator")
        break

    else:
        print("Invalid option. Please enter one of the available choices")
       
from Day_10.art import calculator
print(calculator)
print("\n" * 3)
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}
should_accumulate = True

num1 = float(input('Type your first number \n'))
while should_accumulate:
    
    operator = input("""What operation do you want? Type \n
    +
    -
    *
    /
    """
    '\n'
    )
    num2 = float(input('Type your second number \n'))

    result = operations[operator](num1=num1, num2=num2)

    print(f'{num1} {operator} {num2} = {result}') 

    should_continue = input(f"Do you want to continue working with this {result}? Type 'y' or 'n'\n").lower()

    if should_continue == 'y':
        num1 = result

    else:
        should_accumulate = False



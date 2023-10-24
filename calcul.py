# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def sub(x, y):
    return x - y

# Function to multiply two numbers
def mul(x, y):
    return x * y

# Function to divide two numbers
def div(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Main program
while True:
    # Display menu
    print("Select the operation you want to perform:")
    print("Enter 'add' for addition")
    print("Enter 'sub' for subtraction")
    print("Enter 'mul' for multiplication")
    print("Enter 'div' for division")
    print("Enter 'stop' to end the program")

    # Take user input
    user_input = input(": ")

    # Check for user's choice
    if user_input == "stop":
        break
    elif user_input in ["add", "sub", "mul", "div"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if user_input == "add":
            print("Result:", add(num1, num2))
        elif user_input == "sub":
            print("Result:", sub(num1, num2))
        elif user_input == "mul":
            print("Result:", mul(num1, num2))
        elif user_input == "div":
            print("Result:", div(num1, num2))
    else:
        print("Invalid input. Please try again. Something went wrong")

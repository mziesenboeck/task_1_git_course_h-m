# This is a simple calculator program.

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y != 0:  # Check for division by zero
        return x / y
    else:
        return "Cannot divide by zero."


# Task 1: Implement a function for Exponentiation operation, similar to the existing functions above.
def exponentiation(x, y):
    return x ** y
# Solution by Henrique


# Task 2: Create an interactive user input for the calculator, allowing the user to pick an operation and input numbers.
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exponentiation")
choice = input("Enter choice(1/2/3/4/5): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if choice == '1':
    print(add(num1, num2))
elif choice == '2':
    print(subtract(num1, num2))
elif choice == '3':
    print(multiply(num1, num2))
elif choice == '4':
    print(divide(num1, num2))
elif choice == '5':
    print(exponentiation(num1, num2))

else:
    print("Invalid input")

# Task 3: Add a new file to the repo with other code of your choice

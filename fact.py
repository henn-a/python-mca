# Function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Get user input
num = int(input("Enter a number to find its factorial: "))

# Check for negative numbers
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    # Calculate and print the factorial
    result = factorial(num)
    print(f"The factorial of {num} is {result}.")

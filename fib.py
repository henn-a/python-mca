# Function to generate Fibonacci series
def fibonacci(n):
    fib_series = []
    a, b = 0, 1  # Starting values for Fibonacci series
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b  # Update values for the next terms
    return fib_series

# Get user input
num_terms = int(input("Enter the number of terms in the Fibonacci series: "))

# Generate and display the Fibonacci series
if num_terms <= 0:
    print("Please enter a positive integer greater than 0.")
else:
    series = fibonacci(num_terms)
    print(f"The Fibonacci series of {num_terms} terms is:")
    print(series)

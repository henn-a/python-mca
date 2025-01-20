# Get user input for a list of integers
input_string = input("Enter a list of integers separated by spaces: ")

# Convert the input string to a list of integers
numbers = list(map(int, input_string.split()))

# Create a new list by removing even numbers using list comprehension
odd_numbers = [num for num in numbers if num % 2 != 0]

# Output the result
print("List with even numbers removed:")
print(odd_numbers)

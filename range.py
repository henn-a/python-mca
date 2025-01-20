import math

# Function to check if a number has all even digits
def has_all_even_digits(num):
    return all(int(digit) % 2 == 0 for digit in str(num))

# Function to generate list of four-digit perfect square numbers with all even digits
def find_perfect_squares_with_even_digits(start, end):
    result = []
    for num in range(start, end + 1):
        if int(math.sqrt(num)) ** 2 == num:  # Check if the number is a perfect square
            if has_all_even_digits(num):  # Check if all digits are even
                result.append(num)
    return result

# Get user input for range
start = int(input("Enter the starting number of the range (four-digit number): "))
end = int(input("Enter the ending number of the range (four-digit number): "))

# Find and print the numbers that are perfect squares and have all even digits
numbers = find_perfect_squares_with_even_digits(start, end)

print(f"Perfect square numbers with all even digits in the range {start}-{end}:")
print(numbers)

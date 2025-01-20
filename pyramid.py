# Function to display the pyramid
def print_pyramid(N):
    for i in range(1, N+1):
        row = []  # List to store the numbers for the current row
        for j in range(1, i+1):
            row.append(i * j)  # Append multiples of i (i*j)
        print(" ".join(map(str, row)))  # Join and print the row

# Get user input for the number of rows
N = int(input("Enter the number of rows (N): "))

# Print the pyramid
print_pyramid(N)

# Get the number of rows for the middle of the pattern (highest number of stars)
n = int(input("Enter the number of rows for the middle of the pattern: "))

# Upper half of the pattern including the middle line
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# Lower half of the pattern
for i in range(n - 1, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

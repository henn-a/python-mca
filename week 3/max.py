
numbers = list(map(int, input("Enter numbers : ").split()))

if numbers:
    count = len(numbers)
print("Max:", max(numbers), "Min:", min(numbers), "Sum:", sum(numbers))
print("Sorted:", sorted(numbers), "Reversed:", numbers[::-1])
print(f"count the list: {count}")


list1 = list(map(int, input("Enter the first list of integers: ").split()))
list2 = list(map(int, input("Enter the second list of integers: ").split()))


print("Same length:", len(list1) == len(list2))


print("Same sum:", sum(list1) == sum(list2))
common_values = set(list1) & set(list2)
print("Common values:", common_values if common_values else "None")

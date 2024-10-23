
first_names = input("Enter first names separated by spaces: ").split()


count_a = sum(name.lower().count('a') for name in first_names)

print("Total occurrences of 'A' in the list:", count_a)

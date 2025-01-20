# Example dictionary
my_dict = {'apple': 10, 'banana': 5, 'cherry': 7, 'date': 12}

# 1. Sorting by keys in ascending order
sorted_by_keys_asc = dict(sorted(my_dict.items()))
print("Sorted by keys in ascending order:")
print(sorted_by_keys_asc)

# 2. Sorting by keys in descending order
sorted_by_keys_desc = dict(sorted(my_dict.items(), reverse=True))
print("Sorted by keys in descending order:")
print(sorted_by_keys_desc)

# 3. Sorting by values in ascending order
sorted_by_values_asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Sorted by values in ascending order:")
print(sorted_by_values_asc)

# 4. Sorting by values in descending order
sorted_by_values_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("Sorted by values in descending order:")
print(sorted_by_values_desc)

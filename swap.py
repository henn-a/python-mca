my_list = input("Enter elements of the list: ").split()
if len(my_list) > 1:
    my_list[0], my_list[-1] = my_list[-1], my_list[0]
print("Swapped list:", my_list)


my_list = [1, 88, 3, 4, 5, 6, 7, 8, 17]

print("List before swap:", my_list)
if len(my_list) >= 2:
    first_element = my_list[0]
    last_element = my_list[-1]

    my_list[0] = last_element
    my_list[-1] = first_element

print("New list after swap:", my_list)

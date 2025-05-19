def swap_first_list(my_list):
    if len(my_list) > 1:

        my_list[0], my_list[1] = my_list[1], my_list[0]
        return my_list
    
my_list = [4, 3, 6, 1, 7]
swap_first_list = swap_first_list(my_list)
print(swap_first_list)
#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        for num in my_list:
            if num > my_list[0]:
                my_list[0] = num
        return my_list[0]
    return None

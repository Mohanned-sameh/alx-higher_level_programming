#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        return sum(my_list[0]) / sum(my_list[1])
    else:
        return 0

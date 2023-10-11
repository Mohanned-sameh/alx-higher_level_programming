#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    else:
        return sum(my_list[0]) / sum(my_list[1])

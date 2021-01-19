#######################
# Basic Math          #
#######################

"""
여기서 간단한 수학을 하는 프로그램을 만들것입니다. 
"""


def get_greatest(number_list):
    greatest_number = max(number_list)
    return greatest_number


def get_smallest(number_list):
    smallest_number = min(number_list)
    return smallest_number


def get_mean(number_list):
    mean = sum(number_list) // len(number_list)
    return mean


def get_median(number_list):
    number_list.sort()
    size = len(number_list)
    if size % 2 == 0:
        median = (number_list[size // 2] + number_list[size // 2 - 1]) / 2
    else:
        median = number_list[size // 2]
    return median

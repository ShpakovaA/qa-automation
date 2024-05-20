import re

lst = [1, 2, [3, 4, [5, 6], 7], 8, [9, [10]], 11]


def linearize_list(lst):
    not_nested_list = []
    for element in lst:
        if type(element) == list:
            not_nested_list.extend(linearize_list(element))
        else:
            not_nested_list.append(element)
    return not_nested_list


print(linearize_list(lst))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

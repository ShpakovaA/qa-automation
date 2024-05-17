import re

lst = [1, 2, [3, 4, [5, 6], 7], 8, [9, [10]], 11]

def linearize_list(lst):
    lst_to_str = str(lst)
    digits_only = re.findall(r'\d+', lst_to_str)
    flat_list = [int(element) for element in digits_only]
    return flat_list


print(linearize_list(lst))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

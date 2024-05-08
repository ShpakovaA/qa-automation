# Second largest number in the list


def second_largest_number(lst):
    if len(lst) == 0:
        second_max_number = None

    else:
        lst2set = set(lst)
        if len(lst2set) == 1:
            second_max_number = None
        else:
            lst = list(lst2set)
            max_number = lst[0]

            for item in lst:
                if item > max_number:
                    max_number = item

            lst.remove(max_number)

            second_max_number = lst[0]

            for item in lst:
                if item > second_max_number:
                    second_max_number = item

    print(second_max_number)


second_largest_number([])  # None
second_largest_number([1,1])  # None
second_largest_number([1, 2, 3, 4, 5])  # 4

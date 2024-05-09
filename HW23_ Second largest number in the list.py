# Second largest number in the list


def second_largest_number(lst):
    if len(lst) < 2:
        return None

    else:
        first_max_number = lst[0]
        second_max_number = lst[1]

        if second_max_number > first_max_number:
            second_max_number, first_max_number = first_max_number, second_max_number

        for number in lst[2:]:
            if number > first_max_number:
                second_max_number = first_max_number
                first_max_number = number

            elif number > second_max_number:
                second_max_number = number

    if first_max_number == second_max_number:
        return None
    else:
        return second_max_number


print(second_largest_number([]))  # None
print(second_largest_number([1,1]))  # None
print(second_largest_number([1, 2, 3, 4, 5])) # 4

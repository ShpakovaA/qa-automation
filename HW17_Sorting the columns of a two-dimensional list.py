# Sorting the columns of a two-dimensional list

lst = [['a', 'c', 'e'],
       ['f', 'b', 'a'],
       ['a', 'n', 'k'],
       ['e', 'l', 'i']]

for column in range(0, len(lst[0]), 1):
    lst_sorted = sorted([elements[column] for elements in lst])
    for index in range(0, len(lst),1):
        lst[index][column] = lst_sorted[index]

for row in lst:
    print(row)


# # ->
# [['a', 'b', 'a']
#  ['a', 'c', 'e']
#  ['e', 'l', 'i']
#  ['f', 'n', 'k']]


# List separation

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]  # Input list

# [3, 6, 9, 12]  # elements divided by 3
lst2 = [element for element in lst if element % 3 == 0 and not element % 5 == 0]
print(lst2)

# [5, 10]  # elements divided by 5
lst3 = [element for element in lst if element % 5 == 0 and not element % 3 == 0]
print(lst3)

# [0, 15]  # elements divided by 3 and by 5
lst4 = [element for element in lst if element % 5 == 0 and element % 3 == 0]
print(lst4)
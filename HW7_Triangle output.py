size = int(input("Enter size of triangle: "))
h = 1

while h <= size:
    my_string = ""
    space = size-h
    star = 1

    while space > 0:
        my_string += " "
        space -= 1

    while star <= h:
        my_string += "*"
        star += 1

    print(my_string)
    h += 1

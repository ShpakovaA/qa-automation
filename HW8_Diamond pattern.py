min_width = int(input("Enter minimal width: "))
max_width = int(input("Enter maximal width: "))
i = 0

if min_width >= max_width:
    print("Minimal width can't be greater than maximum width.Try again")
elif (max_width - min_width) % 2 != 0:
    print("The difference between the maximum and minimum widths should be a multiple of 2. Try again")
else:
    for row in range(min_width, max_width+1, 2):

        space_count = int((max_width-min_width)/2-i)
        for space in range(0, space_count):
            print(end=' ')

        if row == min_width:
            for star in range (0, min_width):
                print('*', end='')
        else:
            for star in range(1, row+1):
                if star == 1 or star == row:
                    print('*', end = '')
                else:
                    print(' ', end = '')
        print()
        i += 1

    for row in range(max_width-2, min_width-2, -2):

        space_count = int((max_width-row)/2)
        for space in range(0, space_count):
            print(' ', end='')

        if row == min_width:
            for star in range (0, min_width):
                print('*', end='')
        else:
            for star in range(1, row+1):
                if star == 1 or star == row:
                    print('*', end='')
                else:
                    print(' ', end='')
        print()


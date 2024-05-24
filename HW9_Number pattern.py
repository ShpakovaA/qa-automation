
n = int(input("Please enter number for pattern:" ))
count = 1

while count <= n:
    spaces = n - count
    count_numbers = count-1

    for space in range(0, spaces):
        print(" ", end=" ")

    for number in range(1, count+1):
        if count == 1:
            print(number, end="")
        else:
            print(number, end=" ")

    while count_numbers >= 1:
        if count_numbers == 1:
            print(count_numbers, end="")
        else:
            print(count_numbers, end=" ")

        count_numbers -= 1

    print()
    count += 1

n = int(input("Please enter number for pattern:" ))
count = 1

while count <= n:
    spaces = n - count

    for space in range(0, spaces):
        print(" ", end=" ")

    for number in range(1, count+1):
        if count == 1:
            print(number, end="")
        else:
            print(number, end=" ")

    for number in range(count-1, 0, -1):
        if number == 1:
            print(number, end="")
        else:
            print(number, end=" ")
    print()
    count += 1

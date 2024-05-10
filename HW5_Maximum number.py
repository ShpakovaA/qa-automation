# HW5_Maximum number

n = 1
lst = []

while n <= 3:
    lst.append(input(f"Enter number {n}: "))
    n += 1

max_number = lst[0]

for number in lst:
    if number > max_number:
        max_number = number

print(max_number)
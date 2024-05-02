# Adding averages to the list

lst = [1, 2, 3, 4, 5]
new_lst = []


for index in range(0, len(lst), 1):
    new_lst.append(lst[index])

    if index < len(lst)-1:
        avg = (lst[index]+lst[index+1])/2
        new_lst.append(avg)

print(new_lst) #Result: [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]



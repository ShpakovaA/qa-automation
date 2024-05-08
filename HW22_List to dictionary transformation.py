# List to dictionary transformation

def lst2dict(lst):
    dict = {}
    for i in range(0, len(lst) - 1, 2):
        dict[lst[i]] = lst[i + 1]
    return dict


print(lst2dict([0, 1, 2, 3]))  # {0: 1, 2: 3}
print(lst2dict(['a', 'A', 'b', 'B', 'c']))  # {'a': 'A', 'b': 'B'}
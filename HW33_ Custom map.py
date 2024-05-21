def custom_map(func, *iterables):
    result =[]
    if len(iterables) > 1:
        min_length = min(len(iterable) for iterable in iterables)
        for i in range(min_length):
            result.append(func(*[iterable[i] for iterable in iterables]))
    else:
        for iterable in iterables:
            result.extend(func(i) for i in iterable)
    return result

print(custom_map(sum, [[1, 2, 3], [3, 5, 0, 5]]))  # [6, 13]
print(custom_map(lambda x, y: x + y, [1, 2, 3, 3], [3, 5, 0]))  # [4, 7, 3]
print(custom_map(len, [[], (2, 4), [1, 3, 5, 7]])) # [0, 2, 4]



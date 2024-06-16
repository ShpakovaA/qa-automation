import math


def result_cache_decorator(func):
    func_results = {}

    def wrapper(*args, **kwargs):
        key = (*args, *kwargs.items())

        if args:
            if key in func_results:
                return func_results[key]

        elif kwargs:
            for i in func_results.keys():
                print(dict(i))
                if all(dict(key).get(k) == v for k, v in dict(i).items()):
                    return func_results[i]

        result = func(*args, **kwargs)
        func_results[key] = result
        return result

    return wrapper


@result_cache_decorator
def custom_sqrt(x):
    print("func call")
    return math.sqrt(x)


@result_cache_decorator
def custom_add(a, b, c):
    print("func call")
    return a + b + c


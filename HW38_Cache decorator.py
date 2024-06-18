import math


def result_cache_decorator(func):
    func_results = {}

    def wrapper(*args, **kwargs):
        key = frozenset((*args, *kwargs.items()))

        if key in func_results.keys():
            return func_results[key]

        result = func(*args, **kwargs)
        func_results[key] = result
        return result

    return wrapper


@result_cache_decorator
def custom_sqrt(x):
    return math.sqrt(x)


@result_cache_decorator
def custom_add(a, b, c):
    return a + b + c



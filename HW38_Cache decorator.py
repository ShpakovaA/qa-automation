import math


def result_cache_decorator(func):
    func_results = {}

    def wrapper(*args, **kwargs):
        key = (*args, *kwargs.items())
        match = False

        for results_key in func_results.keys():
            for element in key:
                if element in results_key:
                    match = True
                else:
                    match = False
                    break
            if match:
                return func_results[results_key]

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




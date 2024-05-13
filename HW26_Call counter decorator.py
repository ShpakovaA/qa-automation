def call_counter(path):
    def decorator(func):
        def wrapper(a, b):
            wrapper.count += 1
            with open(path, "a") as f:
                f.write(f"Function {func.__name__} was called {wrapper.count} times\n")
            return func(a, b)
        wrapper.count = 0
        return wrapper
    return decorator

@call_counter('data.txt')
def add(a, b):
    return a + b


print(add(4, 6))
print(add(3, 5))

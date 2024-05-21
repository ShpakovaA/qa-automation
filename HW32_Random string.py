import random


def get_random_string(length: int) -> str:
    relevant_symbols = [chr(i) for i in range(0, 123)
                        if (i >= 48 and i <= 57) or (i >= 65 and i <= 90) or (i >= 97 and i <= 122)]
    return "".join(random.choices(relevant_symbols, k=length))


print(get_random_string(5))

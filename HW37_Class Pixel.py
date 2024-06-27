from typing import Union


class Pixel:
    pixels = [x for x in range(0, 256)]

    def __init__(self, red: int, green: int, blue: int):
        self.__red = red
        self.__green = green
        self.__blue = blue

    def __setattr__(self, key, value):
        if value in self.pixels:
            self.__dict__[key] = value
        else:
            raise ValueError("The value should be in range [0, 255]")

    @property
    def red(self):
        return self.__red

    @property
    def green(self):
        return self.__green

    @property
    def blue(self):
        return self.__blue

    def __str__(self):
        return f"Pixel object\n\tRed: {self.__red}\n\tGreen: {self.__green}\n\tBlue: {self.__blue}"

    def __repr__(self):
        return f"Pixel({self.__red}, {self.__green}, {self.__blue})"

    def __add__(self, other):
        r = min(self.__red + other.red, 255)
        g = min(self.__green + other.green, 255)
        b = min(self.__blue + other.blue, 255)
        return Pixel(r, g, b)

    def __sub__(self, other):
        r = max(0, self.__red - other.red)
        g = max(0, self.__green - other.green)
        b = max(0, self.__blue - other.blue)
        return Pixel(r, g, b)

    def __mul__(self, number: Union[int, float]):
        if number <= 0:
            raise ValueError("Should be more than 0")
        else:
            r = min(self.__red * number, 255)
            g = min(self.__green * number, 255)
            b = min(self.__blue * number, 255)
            return Pixel(int(r), int(g), int(b))

    def __rmul__(self, number: Union[int, float]):
        return Pixel.__mul__(self, number)

    def __truediv__(self, number: Union[int, float]):
        if number <= 0:
            raise ValueError("Should be more than 0")
        else:
            r = min(255.0, self.__red / number)
            g = min(255.0, self.__green / number)
            b = min(255.0, self.__blue / number)
            return Pixel(int(r), int(g), int(b))

    def __eq__(self, other):
        if not isinstance(other, Pixel):
            return False
        return self.__red == other.red and self.__green == other.green and self.__blue == other.blue
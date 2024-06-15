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
        r = self.__red + other.red
        if r > 255:
            r = 255
        g = self.__green + other.green
        if g > 255:
            g = 255
        b = self.__blue + other.blue
        if b > 255:
            b = 255
        return Pixel(r, g, b)

    def __sub__(self, other):
        r = self.__red - other.red
        if r < 0:
            r = 0
        g = self.__green - other.green
        if g < 0:
            g = 0
        b = self.__blue - other.blue
        if b < 0:
            b = 0
        return Pixel(r, g, b)

    def __mul__(self, number: Union[int, float]):
        if number <= 0:
            raise ValueError("Should be more than 0")
        else:
            r = self.__red * number
            if r > 255:
                r = 255
            g = self.__green * number
            if g > 255:
                g = 255
            b = self.__blue * number
            if b > 255:
                b = 255
            return Pixel(int(r), int(g), int(b))

    def __rmul__(self, number: Union[int, float]):
        if number <= 0:
            raise ValueError("Should be more than 0")
        else:
            r = self.__red * number
            if r > 255:
                r = 255
            g = self.__green * number
            if g > 255:
                g = 255
            b = self.__blue * number
            if b > 255:
                b = 255
            return Pixel(int(r), int(g), int(b))

    def __truediv__(self, number: Union[int, float]):
        if number <= 0:
            raise ValueError("Should be more than 0")
        else:
            r = self.__red / number
            g = self.__green / number
            b = self.__blue / number
            return Pixel(int(r), int(g), int(b))

    def __eq__(self, other):
        if not isinstance(other, Pixel):
            return False
        return self.__red == other.red and self.__green == other.green and self.__blue == other.blue

import re
import pytest
from Pixel.HW37_ClassPixel import Pixel


@pytest.mark.parametrize('red, green, blue', [(0, 255, 1), (254, 149, 0), (67, 0, 137)])
def test_valid_values_pixel(red, green, blue):
    pixel = Pixel(red=red, green=green, blue=blue)
    assert pixel.red == red
    assert pixel.green == green
    assert pixel.blue == blue


@pytest.mark.parametrize('red, green, blue', [(0, 256, 1), (2.4, 149, 0), (67, 89, -8)])
def test_invalid_value_pixel(red, green, blue):
    with pytest.raises(ValueError, match=re.escape("The value should be in range [0, 255]")) as exc:
        pixel = Pixel(red=red, green=green, blue=blue)
    assert str(exc.value) == "The value should be in range [0, 255]"


def test_adding_two_pixels():
    pixel1 = Pixel(0, 1, 2)
    pixel2 = Pixel(1, 2, 255)
    pixels_sum = pixel1 + pixel2
    assert pixels_sum == Pixel(1, 3, 255)


def test_subtracting_two_pixels():
    pixel1 = Pixel(10, 20, 30)
    pixel2 = Pixel(10, 30, 40)
    pixels_subtraction = pixel1 - pixel2
    assert pixels_subtraction == Pixel(0, 0, 0)

# ФІКСТУРА ПІКСЕЛЬ

@pytest.mark.parametrize('number, red, green, blue', [(3, 3, 30, 255), (20.55, 20, 205, 255)])
def test_multiplying_pixel_by_number(number, red, green, blue, nominal_pixel):
    # pixel = Pixel(1, 10, 100)
    multiplied_pixel = nominal_pixel * number
    expected_pixel = Pixel(red, green, blue)
    assert multiplied_pixel == expected_pixel


@pytest.mark.parametrize('number, red, green, blue', [(2, 0, 25, 50), (0.25, 4, 200, 255)])
def test_dividing_pixel_by_number(number, red, green, blue):
    pixel = Pixel(1, 50, 100)
    divided_pixel = pixel / number
    assert divided_pixel == Pixel(red, green, blue)

# ФІКСТУРА ПІКСЕЛЬ

@pytest.mark.parametrize('number', (0, -2))
def test_multiplying_pixel_by_invalid_number(number):
    pixel = Pixel(1, 10, 100)
    with pytest.raises(ValueError, match="Should be more than 0") as exc:
        pixel*number
    assert str(exc.value) == "Should be more than 0"

# ФІКСТУРА ПІКСЕЛЬ
@pytest.mark.parametrize('number', (0, -2))
def test_dividing_pixel_by_invalid_number(number):
    pixel = Pixel(1, 10, 100)
    with pytest.raises(ValueError, match="Should be more than 0") as exc:
        pixel/number
    assert str(exc.value) == "Should be more than 0"


@pytest.mark.parametrize('number', ("34", [2, 4, 3], {"red": 23, "green": 100, "blue":182}))
def test_dividing_pixel_by_invalid_type(number):
    pixel = Pixel(1, 10, 100)
    with pytest.raises(TypeError):
        pixel/number

# ФІКСТУРА ПІКСЕЛЬ
@pytest.mark.parametrize('number', ("34", [2, 4, 3], {"red": 23, "green": 100, "blue": 182}))
def test_multiplying_pixel_by_invalid_type(number):
    pixel = Pixel(1, 10, 100)
    with pytest.raises(TypeError):
        pixel/number

# ФІКСТУРА ПІКСЕЛЬ
def test_two_pixel_objects_equation_equal():
    pixel1 = Pixel(20, 189, 202)
    pixel2 = Pixel(20, 189, 202)
    assert (pixel1 == pixel2) is True

# ФІКСТУРА ПІКСЕЛЬ
def test_two_pixel_objects_inequity():
    pixel1 = Pixel(20, 189, 202)
    pixel2 = Pixel(0, 20, 198)
    assert (pixel1 == pixel2) is False

# ФІКСТУРА ПІКСЕЛЬ
def test_pixel_object_inequity_whith_other_object():
    pixel1 = Pixel(20, 189, 202)
    pixel2 = {"red": 23, "green": 100, "blue": 182}
    assert (pixel1 == pixel2) is False

# ФІКСТУРА ПІКСЕЛЬ
def test_str_method():
    pixel1 = Pixel(20, 189, 202)
    expected_string = f"Pixel object\n\tRed: {pixel1.red}\n\tGreen: {pixel1.green}\n\tBlue: {pixel1.blue}"
    assert pixel1.__str__() == expected_string


# ФІКСТУРА ПІКСЕЛЬ
def test_repr_method():
    pixel1 = Pixel(20, 189, 202)
    expected_string = f"Pixel({pixel1.red}, {pixel1.green}, {pixel1.blue})"
    assert pixel1.__repr__() == expected_string


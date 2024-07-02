import re
import pytest
from HW37_ClassPixel import Pixel


@pytest.mark.parametrize('red, green, blue', [(0, 255, 254), (255, 149, 0), (1, 0, 255)])
def test_valid_values_pixel(red, green, blue):
    pixel = Pixel(red=red, green=green, blue=blue)
    assert isinstance(pixel, Pixel)
    assert pixel.red == red
    assert pixel.green == green
    assert pixel.blue == blue


@pytest.mark.parametrize('red, green, blue', [(0, 256, 1), (67, 89, -1)])
def test_invalid_value_pixel(red, green, blue):
    with pytest.raises(ValueError, match=re.escape("The value should be in range [0, 255]")) as exc:
        pixel = Pixel(red, green, blue)


@pytest.mark.parametrize('red, green, blue', [("89", 256, 1), (45, [6, 8], 80), (34, 93, (2, 4, 5))])
def test_invalid_type_pixel(red, green, blue):
    with pytest.raises(TypeError) as exc:
        pixel = Pixel(red, green, blue)
    assert str(exc.value) == "The value should be int"


def test_adding_two_pixels_1():
    pixel1 = Pixel(200, 100, 10)
    pixel2 = Pixel(100, 47, 255)
    pixels_sum = pixel1 + pixel2
    expected_pixel = Pixel(255, 147, 255)
    assert pixels_sum == expected_pixel


def test_adding_two_pixels_2():
    pixel1 = Pixel(0, 189, 67)
    pixel2 = Pixel(89, 211, 130)
    pixels_sum = pixel1 + pixel2
    expected_pixel = Pixel(89, 255, 197)
    assert pixels_sum == expected_pixel


def test_subtracting_two_pixels_1():
    pixel1 = Pixel(180, 20, 30)
    pixel2 = Pixel(10, 30, 40)
    pixels_subtraction = pixel1 - pixel2
    expected_pixel = Pixel(170, 0, 0)
    assert pixels_subtraction == expected_pixel


def test_subtracting_two_pixels_2():
    pixel1 = Pixel(10, 60, 255)
    pixel2 = Pixel(150, 30, 40)
    pixels_subtraction = pixel1 - pixel2
    expected_pixel = Pixel(0, 30, 215)
    assert pixels_subtraction == expected_pixel


@pytest.mark.parametrize('number, red, green, blue', [(2, 2, 20, 200), (300, 255, 255, 255), (1.6, 1, 16, 160)])
def test_multiplying_pixel_by_number(number, red, green, blue, nominal_pixel):
    multiplied_pixel = nominal_pixel * number
    expected_pixel = Pixel(red, green, blue)
    assert multiplied_pixel == expected_pixel


@pytest.mark.parametrize('number, red, green, blue', [(2, 2, 20, 200), (300, 255, 255, 255), (1.6, 1, 16, 160)])
def test_right_multiplying_pixel_by_number(number, red, green, blue, nominal_pixel):
    multiplied_pixel = number * nominal_pixel
    expected_pixel = Pixel(red, green, blue)
    assert multiplied_pixel == expected_pixel


@pytest.mark.parametrize('number, red, green, blue', [(3, 0, 3, 33), (1.8, 0, 5, 55), (0.001, 255, 255, 255)])
def test_dividing_pixel_by_number(number, red, green, blue, nominal_pixel):
    divided_pixel = nominal_pixel / number
    expected_pixel = Pixel(red, green, blue)
    assert divided_pixel == expected_pixel


@pytest.mark.parametrize('number', (0, -2))
def test_multiplying_pixel_by_invalid_number(number, nominal_pixel):
    with pytest.raises(ValueError, match="Should be more than 0") as exc:
        nominal_pixel * number
    assert str(exc.value) == "Should be more than 0"


@pytest.mark.parametrize('number', (0, -2))
def test_dividing_pixel_by_invalid_number(number, nominal_pixel):
    with pytest.raises(ValueError, match="Should be more than 0") as exc:
        nominal_pixel / number
    assert str(exc.value) == "Should be more than 0"


@pytest.mark.parametrize('number', ("34", [2, 4, 3], {"red": 23, "green": 100, "blue": 182}))
def test_dividing_pixel_by_invalid_type(number, nominal_pixel):
    with pytest.raises(TypeError):
        nominal_pixel / number


@pytest.mark.parametrize('number', ("34", [2, 4, 3], {"red": 23, "green": 100, "blue": 182}))
def test_multiplying_pixel_by_invalid_type(number, nominal_pixel):
    with pytest.raises(TypeError):
        nominal_pixel * number


def test_two_pixel_objects_equation_equal(nominal_pixel):
    pixel2 = Pixel(1, 10, 100)
    assert nominal_pixel == pixel2


def test_two_pixel_objects_inequity(nominal_pixel):
    pixel2 = Pixel(0, 20, 198)
    assert nominal_pixel != pixel2


def test_pixel_object_inequity_with_other_object(nominal_pixel):
    pixel2 = {"red": 23, "green": 100, "blue": 182}
    assert nominal_pixel != pixel2


def test_str_method(nominal_pixel):
    expected_string = f"Pixel object\n\tRed: {nominal_pixel.red}\n\tGreen: {nominal_pixel.green}\n\tBlue: {nominal_pixel.blue}"
    assert str(nominal_pixel) == expected_string


def test_repr_method(nominal_pixel):
    expected_string = f"Pixel({nominal_pixel.red}, {nominal_pixel.green}, {nominal_pixel.blue})"
    assert repr(nominal_pixel) == expected_string


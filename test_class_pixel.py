import pytest
from HW37_ClassPixel import Pixel


@pytest.mark.parametrize('red, green, blue', [(0, 255, 1), (254, 149, 0), (67, 0, 137)])
def test_valid_pixel(red, green, blue):
    pixel = Pixel(red=red, green=green, blue=blue)
    assert pixel.red == red
    assert pixel.green == green
    assert pixel.blue == blue


@pytest.mark.parametrize('red, green, blue', [(0, 256, 1), (2.4, 149, 0), (67, 89, -8)])
def test_invalid_value_pixel(red, green, blue):
    with pytest.raises(ValueError, match="The value should be in range [0, 255]") as exc:
        pixel = Pixel(red=red, green=green, blue=blue)
    assert str(exc.value) == "The value should be in range [0, 255]"


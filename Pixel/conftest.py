import pytest
from HW37_ClassPixel import Pixel


@pytest.fixture()
def nominal_pixel():
    return Pixel(1, 10, 100)
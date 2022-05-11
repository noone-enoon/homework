import random
import pytest
import math

from src.Triangle import Triangle

side_a = random.randint(13, 15)
side_b = random.randint(12, 12)
side_c = random.randint(10, 16)
triangle = Triangle(side_a, side_b, side_c)


def test_attribute_name():
    assert triangle._name == 'Triangle'


def test_triangle_invalid():
    with pytest.raises(ValueError):
        return Triangle(side_a, side_b, side_c)


def test_area():
    semi_perimeter = (side_a + side_b + side_c) / 2
    area = (semi_perimeter * (semi_perimeter - side_a) * (semi_perimeter - side_b) * (semi_perimeter - side_c)) ** 0.5
    assert math.isclose(area, triangle.area)


def test_perimeter():
    perimeter = side_a + side_b + side_c
    assert perimeter == triangle.perimeter

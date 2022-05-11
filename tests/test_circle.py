import math
import random
from src.Circle import Circle

radius = random.randint(1, 100)
circle = Circle(radius)


def test_attribute_name():
    assert circle._name == 'Circle'


def test_area():
    assert circle.area == math.pi * radius ** 2


def test_perimeter():
    perimeter = math.pi * 2 * radius
    assert circle.perimeter == perimeter

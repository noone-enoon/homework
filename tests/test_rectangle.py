import random
from src.Rectangle import Rectangle

side_a = random.randint(1, 100)
side_b = random.randint(1, 100)
rectangle = Rectangle(side_a, side_b)


def test_attribute_name():
    assert rectangle._name == 'Rectangle'


def test_area():
    assert rectangle.area == side_a * side_b


def test_perimeter():
    perimeter = 2 * side_a + 2 * side_b
    assert rectangle.perimeter == perimeter

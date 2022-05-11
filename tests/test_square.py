import random
from src.Square import Square

side = random.randint(1, 100)
square = Square(side)


def test_attribute_name():
    assert square._name == 'Square'


def test_area():
    assert square.area == side ** 2


def test_perimeter():
    assert square.perimeter == 4 * side

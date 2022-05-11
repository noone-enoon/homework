import pytest
import random
from src.Square import Square
from src.Rectangle import Rectangle
from src.Triangle import Triangle
from src.Circle import Circle


@pytest.fixture()
def instance_square():
    side = random.randint(1, 100)
    return Square(side)


@pytest.fixture()
def instance_rectangle():
    side_a = random.randint(1, 100)
    side_b = random.randint(1, 100)
    return Rectangle(side_a, side_b)


@pytest.fixture()
def instance_triangle_valid():
    side_a = random.randint(70, 80)
    side_b = random.randint(65, 85)
    side_c = random.randint(70, 90)
    return Triangle(side_a, side_b, side_c)


@pytest.fixture()
def instance_circle():
    radius = random.randint(1, 100)
    return Circle(radius)

from src.Figure import Figure
import math


class Circle(Figure):
    _name = 'Circle'

    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def perimeter(self, *args):
        return math.pi * 2 * self.radius

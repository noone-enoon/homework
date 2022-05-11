from src.Figure import Figure


class Rectangle(Figure):
    _name = 'Rectangle'

    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    @property
    def area(self):
        return self.side_a * self.side_b

    @property
    def perimeter(self, *args):
        return 2 * self.side_a + 2 * self.side_b

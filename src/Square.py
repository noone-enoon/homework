from src.Figure import Figure


class Square(Figure):
    _name = 'Square'

    def __init__(self, side):
        self.side = side

    @property
    def area(self):
        return self.side ** 2

    @property
    def perimeter(self, *args):
        return 4 * self.side

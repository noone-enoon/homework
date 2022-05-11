from src.Figure import Figure


class Triangle(Figure):
    _name = 'Triangle'

    def __init__(self, side_a, side_b, side_c):
        if side_a + side_b > side_c and side_b + side_c > side_a and side_a + side_c > side_b:
            self.side_a = side_a
            self.side_b = side_b
            self.side_c = side_c
        else:
            raise ValueError

    @property
    def semi_perimeter(self):
        return (self.side_a + self.side_b + self.side_c) / 2

    @property
    def area(self):
        return (self.semi_perimeter * (self.semi_perimeter - self.side_a) * (self.semi_perimeter - self.side_b)
                * (self.semi_perimeter - self.side_c)) ** 0.5

    @property
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

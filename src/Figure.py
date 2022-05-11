class Figure:
    @property
    def area(self, *args):
        raise NotImplemented

    @property
    def perimeter(self, *args):
        raise NotImplemented

    def add_area(self, figure):
        if isinstance(figure, Figure):
            return self.area + figure.area
        else:
            raise ValueError

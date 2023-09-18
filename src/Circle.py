from src.Figure import Figure


class Circle(Figure):
    def __init__(self, radius):
        super().__init__()
        if radius <= 0:
            raise ValueError("Can't create Circle")
        self.radius = radius
        self.name = 'Circle'
        self._pi = 3.14

    def get_area(self):
        return float(format(self._pi * self.radius ** 2, ".15g"))

    def get_perimeter(self):
        return float(format(2 * self._pi * self.radius, ".15g"))

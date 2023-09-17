from src import Figure


class Circle(Figure):
    def __init__(self, radius):
        super().__init__()
        if radius <= 0:
            raise ValueError("Can't create Circle")
        self.radius = radius
        self.name = 'Circle'

    def get_area(self):
        return 3.14 * self.radius ** 2

    def get_perimeter(self):
        return 2 * 3.14 * self.radius

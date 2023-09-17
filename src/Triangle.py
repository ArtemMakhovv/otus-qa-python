from src import Figure


class Triangle(Figure):
    def __int__(self, side_a, side_b, side_c):
        super().__init__()
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("Can't create Triangle")
        if side_a + side_b < side_c\
            or side_b + side_c < side_a \
                or side_a + side_c < side_b:
            raise ValueError("Can't create Triangle")
        self.name = 'Triangle'
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def get_area(self):
        p = self.get_perimeter() / 2
        return (p * (p-self.side_a) * (p-self.side_b) * (p-self.side_c)) ** 0.5

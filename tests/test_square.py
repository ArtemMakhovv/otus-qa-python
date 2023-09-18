from src.Rectangle import Rectangle
from src.Circle import Circle
from src.Square import Square
from src.Triangle import Triangle

import pytest


@pytest.mark.parametrize(('side', 'area', 'perimeter'),
                         [(10, 100, 40),
                          (1.5, 2.25, 6)])
def test_square(side, area, perimeter):
    square = Square(side)
    assert square.name == 'Square'
    assert square.get_area() == area
    assert square.get_perimeter() == perimeter


@pytest.mark.parametrize('side', [-1, 0])
def test_square_negative(side):
    with pytest.raises(ValueError):
        square = Square(side)
        assert isinstance(square, Square)


@pytest.mark.parametrize(('side', 'other_figure', 'result'),
                         [(1, Circle(5), 79.5),
                          (5, Square(5), 50),
                          (10, Triangle(5, 5, 5), 110.825317547305483),
                          (1, Rectangle(2, 2), 5)],
                         ids=["Add Circle area", "Add Square area", "Add Triangle area", "Add Rectangle area"])
def test_square_add_area(side, other_figure, result):
    square = Square(side)
    assert square.add_area(other_figure) == result


def test_square_add_area_negative():
    with pytest.raises(ValueError):
        square = Square(5)
        assert square.add_area(6)

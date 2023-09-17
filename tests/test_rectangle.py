from src.Rectangle import Rectangle
from src.Circle import Circle
from src.Square import Square
from src.Triangle import Triangle

import pytest


@pytest.mark.parametrize(('side_a', 'side_b', 'area', 'perimeter'),
                         [(10, 20, 200, 60),
                          (1.5, 2.5, 3.75, 8)])
def test_rectangle(side_a, side_b, area, perimeter):
    rectangle = Rectangle(side_a, side_b)
    assert isinstance(rectangle, Rectangle)
    assert rectangle.name == 'Rectangle'
    assert rectangle.get_area() == area
    assert rectangle.get_perimeter() == perimeter


@pytest.mark.parametrize(('side_a', 'side_b'),
                         [(-1, 1),
                          (1, -1),
                          (0, 1),
                          (1, 0)])
def test_rectangle_negative(side_a, side_b):
    with pytest.raises(ValueError):
        rectangle = Rectangle(side_a, side_b)
        assert isinstance(rectangle, Rectangle)


@pytest.mark.parametrize(('side_a', 'side_b', 'other_figure', 'result'),
                         [(1, 2, Circle(5), 80.5),
                          (5, 5, Square(5), 50),
                          (10, 10, Triangle(5, 5, 5), 110.825317547305483),
                          (1, 1, Rectangle(2, 2), 5)],
                         ids=["Add Circle area", "Add Square area", "Add Triangle area", "Add Rectangle area"])
def test_rectangle_add_area(side_a, side_b, other_figure, result):
    rectangle = Rectangle(side_a, side_b)
    assert rectangle.add_area(other_figure) == result


def test_rectangle_add_area_negative():
    with pytest.raises(ValueError):
        rectangle = Rectangle(2, 3)
        assert rectangle.add_area(6)



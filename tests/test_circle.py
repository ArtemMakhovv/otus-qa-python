from src.Rectangle import Rectangle
from src.Circle import Circle
from src.Square import Square
from src.Triangle import Triangle

import pytest


@pytest.mark.parametrize(('radius', 'area', 'perimeter'),
                         [(10, 314, 62.8),
                          (1.5, 7.065, 9.42)])
def test_circle(radius, area, perimeter):
    circle = Circle(radius)
    assert isinstance(circle, Circle)
    assert circle.name == 'Circle'
    assert circle.get_area() == area
    assert circle.get_perimeter() == perimeter


@pytest.mark.parametrize('radius', [-1, 0])
def test_circle_negative(radius):
    with pytest.raises(ValueError):
        circle = Circle(radius)
        assert isinstance(circle, Circle)


@pytest.mark.parametrize(('radius', 'other_figure', 'result'),
                         [(1, Circle(5), 81.64),
                          (5, Square(5), 103.5),
                          (10, Triangle(5, 5, 5), 324.8253175473055),
                          (2, Rectangle(5, 5), 37.56)],
                         ids=["Add Circle area", "Add Square area", "Add Triangle area", "Add Rectangle area"])
def test_circle_add_area(radius, other_figure, result):
    circle = Circle(radius)
    assert circle.add_area(other_figure) == result


def test_circle_add_area_negative():
    with pytest.raises(ValueError):
        circle = Circle(5)
        assert circle.add_area(6)

from src.Rectangle import Rectangle
from src.Circle import Circle
from src.Square import Square
from src.Triangle import Triangle

import pytest


@pytest.mark.parametrize(('side_a', 'side_b', 'side_c', 'area', 'perimeter'),
                         [(5, 10, 11, 24.979991993593593, 26),
                          (1.5, 2.5, 3.5, 1.6237976320958225, 7.5)])
def test_triangle(side_a, side_b, side_c, area, perimeter):
    triangle = Triangle(side_a, side_b, side_c)
    assert isinstance(triangle, Triangle)
    assert triangle.name == 'Triangle'
    assert triangle.get_area() == area
    assert triangle.get_perimeter() == perimeter


@pytest.mark.parametrize(('side_a', 'side_b', 'side_c'),
                         [(-1, -2, -3),
                          (0, 0, 0),
                          (1, 3, 1),
                          (10, 1, 2),
                          (2, 3, 6),
                          (1, 1, 2)],
                         ids=["Triangle with negative sides",
                              "Triangle with zero sides",
                              "Triangle with side_a + side_c < side_b",
                              "Triangle with side_b + side_c < side_a",
                              "Triangle with side_a + side_b < side_c",
                              "Triangle with side_a + side_b = side_c"])
def test_triangle_negative(side_a, side_b, side_c):
    with pytest.raises(ValueError):
        triangle = Triangle(side_a, side_b, side_c)
        assert isinstance(triangle, Triangle)


@pytest.mark.parametrize(('other_figure', 'result'),
                         [(Circle(5), 89.32531754730549),
                          (Square(5), 35.82531754730548),
                          (Triangle(5, 5, 5), 21.650635094610966),
                          (Rectangle(2, 2), 14.825317547305483)],
                         ids=["Add Circle area", "Add Square area", "Add Triangle area", "Add Rectangle area"])
def test_triangle_add_area(other_figure, result):
    triangle = Triangle(5, 5, 5)
    assert triangle.add_area(other_figure) == result


def test_triangle_add_area_negative():
    with pytest.raises(ValueError):
        triangle = Triangle(5, 5, 5)
        assert triangle.add_area(6)

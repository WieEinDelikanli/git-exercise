from __future__ import annotations
from math import isclose
from exercise1 import Vector

class Point2D:
    def __init__(self, x: float, y: float) -> None:
        self._coordinates = Vector([x, y])

    @property
    def x(self) -> float:
        return self._coordinates[0]

    @property
    def y(self) -> float:
        return self._coordinates[1]
    
    # Instance oldugu icin _coordinates, self._x degil bir alttaki vector
    # class'ina gore hareket etmelisin.
    @x.setter
    def x(self, value):
        self._coordinates[0] = value
        
    @y.setter
    def y(self, value):
        self._coordinates[1] = value
    
    def __iadd__(self, other):
        self._coordinates[0] += other[0]
        self._coordinates[1] += other[1]
        return self
    
    def __isub__(self, other):
        self._coordinates[0] -= other[0]
        self._coordinates[1] -= other[1]
        return self


def test_point_construction() -> None:
    point = Point2D(1.0, 42.0)
    assert point.x == 1.0
    assert point.y == 42.0


def test_point_vector_addition() -> None:
    point = Point2D(1.0, 2.0)
    # Task A: make the test below pass (implement __iadd__)
    point += Vector([1.1, 2.2])
    assert isclose(point.x, 2.1)
    assert isclose(point.y, 4.2)


def test_point_vector_subtraction() -> None:
    point = Point2D(1.0, 2.0)
    # Task B: make the test below pass (implement __isub__)
    point -= Vector([1.1, 2.2])
    assert isclose(point.x, -0.1)
    assert isclose(point.y, -0.2)

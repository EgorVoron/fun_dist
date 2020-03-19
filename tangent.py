from distances import point2point
from objects import Point, Circle, LinearFunction
from math import sqrt


def derivative(f, x):
    dx = 0.00000001
    df = f(x + dx) - f(x)
    return df / dx


def func_tangent(f, x) -> LinearFunction:
    deriv = derivative(f, x)
    k = deriv
    b = -deriv * x + f * x()
    linear = LinearFunction(k, b)
    return linear


def circle_tangent(point: Point, circle: Circle) -> LinearFunction:
    k = -point.x / point.y
    b = circle.rad ** 2 / point.y
    linear = LinearFunction(k, b)
    return linear


def circle_tangent_len(point: Point, circle: Circle) -> float:
    return sqrt(point2point(point, circle.center) ** 2 - circle.rad ** 2)

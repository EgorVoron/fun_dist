from math import sqrt

from fun_dist.distances import point2point
from fun_dist.classes import Point, Circle, LinearFunction


def derivative(f, x):
    dx = 1e-8
    df = f(x + dx) - f(x)
    return df / dx


def func_tangent(f, x_0) -> LinearFunction:
    deriv = derivative(f, x_0)
    k = round(deriv, 5)
    b = round(-deriv * x_0 + f(x_0), 5)
    linear = LinearFunction(k, b)
    return linear


def circle_tangent_len(point: Point, circle: Circle) -> float:
    return sqrt(point2point(point, circle.center) ** 2 - circle.radius ** 2)

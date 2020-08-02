from distances import point2point, pythagoras
from objects import Point, Circle, LinearFunction, Ellipse
from math import sqrt


def derivative(f, x):
    dx = 1e-8
    df = f(x + dx) - f(x)
    return df / dx


def func_tangent(f, x_0) -> LinearFunction:
    deriv = derivative(f, x_0)
    k = deriv
    b = -deriv * x_0 + f(x_0)
    linear = LinearFunction(k, b)
    return linear


def circle_tangent(point: Point, circle: Circle) -> LinearFunction:
    k = -point.x / point.y
    if point.y == 0:
        raise ValueError('Cannot describe tangent as a function')
    b = circle.radius ** 2 / point.y
    return LinearFunction(k, b)


def ellipse_tangent(point: Point, ellipse: Ellipse) -> LinearFunction:
    k = -point.x * ellipse.b ** 2 / (ellipse.a ** 2 * point.y)
    if point.y == 0:
        raise ValueError('Cannot describe tangent as a function')
    b = ellipse.b ** 2 / point.y
    return LinearFunction(k, b)


def circle_tangent_len(point: Point, circle: Circle) -> float:
    return pythagoras(point2point(point, circle.center), circle.radius)

from math import sqrt
from classes import Point, Ellipse
from sympy.solvers import solve
from sympy import Symbol


def f(x, a, b):
    return b * sqrt(1 - (x ** 2 / a ** 2))


def D(A: Point, x: float, a: float, b: float):
    return sqrt((x - A.x) ** 2 + (f(x, a, b) - A.y) ** 2)


def get_nearest_point(A: Point, a: float, b: float):
    if A.y < 0:
        A = Point(A.x, -A.y)
    k = 2 - (2 * b ** 2) / (a ** 2)
    p = (2 * b * A.y) / (a ** 2)
    x = Symbol('x')
    answers = solve(-k ** 2 * x ** 4 + 4 * A.x * k * x ** 3 + (
            k ** 2 * a ** 2 - 4 * A.x ** 2 - a ** 2 * p ** 2) * x ** 2 - 4 * A.x * k * x * a ** 2 + 4 * A.x ** 2 * a ** 2,
                    x)
    real_answers = [ans for ans in answers if complex(ans).imag == 0.0]
    positive_answers = [ans for ans in real_answers if ans > 0]
    negative_answers = [ans for ans in real_answers if ans <= 0]
    if A.x > 0:
        ans = min(positive_answers)
    else:
        ans = max(negative_answers)
    return Point(ans, f(ans, a, b))


def point_in_ellipse(point: Point, ellipse: Ellipse):
    return (point.x / ellipse.a) ** 2 + (point.y / ellipse.b) ** 2 <= 1


def point2ellipse(point: Point, ellipse: Ellipse):
    if point2ellipse(point, ellipse):
        print('POINT INSIDE THE ELLIPSE')
        return 0
    point.change_system(dx=ellipse.center.x, dy=ellipse.center.y)
    nearest_point = get_nearest_point(point, ellipse.a, ellipse.b)
    return D(point, nearest_point.x, ellipse.a, ellipse.b)

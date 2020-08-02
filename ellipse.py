from math import sqrt
from sympy.solvers import solve
from sympy import Symbol
from sympy.geometry import Point2D
import mpmath
import sys
sys.modules['sympy.mpmath'] = mpmath

from objects import *


def f(x, a, b):
    return b * sqrt(1 - (x ** 2 / a ** 2))


def D(A: Point2D, x: float, a: float, b: float):
    return sqrt((x - A.x) ** 2 + (f(x, a, b) - A.y) ** 2)


def nearest_point(A: Point2D, a: float, b: float):
    if A.y < 0:
        A = Point2D(A.x, -A.y)
    A
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
    return Point2D(ans, f(ans, a, b))


def point_in_ellipse(point: Point, ellipse: Ellipse):
    return ((point.x / ellipse.a) ** 2 + (point.y / ellipse.b) ** 2) < 1


def point2ellipse(*, point: Point, ellipse: Ellipse):
    if point_in_ellipse(point, ellipse):
        print('POINT INSIDE THE ELLIPSE')
    return D(point, nearest_point(point, ellipse.a, ellipse.b).x, ellipse.a, ellipse.b)

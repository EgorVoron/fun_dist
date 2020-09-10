from warnings import warn
from math import sqrt

from sympy.solvers import solve
from sympy import Symbol

from fun_dist.classes import Point, Ellipse


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
            k ** 2 * a ** 2 - 4 * A.x ** 2 - a ** 2 * p ** 2)
                    * x ** 2 - 4 * A.x * k * x * a ** 2 + 4 * A.x ** 2 * a ** 2, x)
    real_answers = [ans for ans in answers if complex(ans).imag == 0.0]
    positive_answers = [ans for ans in real_answers if ans > 0]
    negative_answers = [ans for ans in real_answers if ans <= 0]
    if A.x > 0:
        ans = min(positive_answers)
    else:
        ans = max(negative_answers)
    return Point(ans, f(ans, a, b))


def point_in_ellipse(point: Point, ellipse: Ellipse):
    point = point.get_changed_point(ellipse.center.x, ellipse.center.y, angle=ellipse.angle)
    ellipse = ellipse.get_changed_ellipse()
    return (point.x / ellipse.a) ** 2 + (point.y / ellipse.b) ** 2 <= 1


def point2ellipse(point: Point, ellipse: Ellipse):
    if point_in_ellipse(point, ellipse):
        warn('POINT INSIDE THE ELLIPSE', stacklevel=2)
        return 0
    point = point.get_changed_point(dx=ellipse.center.x, dy=ellipse.center.y, angle=ellipse.angle)
    ellipse = ellipse.get_changed_ellipse()
    nearest_point = get_nearest_point(point, ellipse.a, ellipse.b)
    return D(point, nearest_point.x, ellipse.a, ellipse.b)


def ellipse_tangent_len(point: Point, ellipse: Ellipse):
    a = ellipse.a
    b = ellipse.b

    def el_1(x):
        return b * sqrt(1 - x ** 2 / a ** 2)

    def el_2(x):
        return -el_1(x)

    point = point.get_changed_point(ellipse.center.x, ellipse.center.y)
    x_a = point.x
    y_a = point.y
    q = b ** 2 / y_a
    g = (x_a * b ** 2) / (y_a * a ** 2)
    A = b ** 2 + a ** 2 * g ** 2
    B = -2 * a ** 2 * q * g
    C = a ** 2 * q ** 2 - a ** 2 * b ** 2
    x_1 = (-B - sqrt(B ** 2 - 4 * A * C)) / (2 * A)
    x_2 = (-B + sqrt(B ** 2 - 4 * A * C)) / (2 * A)

    if abs(x_a) > a:
        if y_a >= 0:
            points_list = [Point(x_1, el_1(x_1)), Point(x_2, el_2(x_2))]
        else:
            points_list = [Point(x_1, el_2(x_1)), Point(x_2, el_1(x_2))]
    else:
        if y_a >= 0:
            points_list = [Point(x_1, el_1(x_1)), Point(x_2, el_1(x_2))]
        else:
            points_list = [Point(x_1, el_2(x_1)), Point(x_2, el_2(x_2))]
    return points_list

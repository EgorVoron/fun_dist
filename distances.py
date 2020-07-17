from scipy.optimize import fmin
from math import sqrt, atan, pi, cos
from objects import Point, Circle, Ellipse


def pythagoras(dx, dy):
    return sqrt(dx ** 2 + dy ** 2)


def point2point(point_1: Point, point_2: Point):
    dx = point_1.x - point_2.x
    dy = point_1.y - point_2.y
    return pythagoras(dx, dy)


class Optimum(object):
    def __init__(self, distance: float, args: list):
        self.args = args
        self.distance = round(distance, 6)

    def __str__(self):
        return f'distance = {self.distance}\nargs: ({self.args})'


class Distance(object):
    def dist_func(self, *args):
        return 0

    def find_minimal_dist(self, *args):
        init_args, max_iter = args
        min_args = fmin(self.dist_func, init_args, maxiter=max_iter, disp=False)
        return Optimum(self.dist_func(min_args), min_args)


class DistanceBetweenFunctions(Distance):
    def __init__(self, func_a, func_b):
        self.func_a = func_a
        self.func_b = func_b

    def dist_func(self, arguments):
        x_a, x_b = arguments
        point_a = Point(x_a, self.func_a(x_a))
        point_b = Point(x_b, self.func_b(x_b))
        return point2point(point_a, point_b)


def func2func(func_a, func_b, init_args=(0, 0), maxiter=500) -> Optimum:
    almost_zero = 1e-10
    dist = DistanceBetweenFunctions(func_a=func_a, func_b=func_b)
    result = dist.find_minimal_dist(init_args, maxiter)
    min_args = result.args
    if abs(func_a(min_args[0]) - func_b(min_args[1])) < almost_zero:
        result.distance = 0
        print('FUNCTIONS INTERSECT')
    return result


class DistanceBetweenPointAndFunction(Distance):
    def __init__(self, point: Point, func):
        self.func = func
        self.point = point

    def dist_func(self, argument):
        x = argument[0]
        point_on_func = Point(x, self.func(x))
        return point2point(self.point, point_on_func)


def point2func(*, point: Point, func, init_args=(0, 0), maxiter=500) -> Optimum:
    if func(point.x) == point.y:
        return Optimum(distance=0, args=[point.x])
    dist = DistanceBetweenPointAndFunction(point=point, func=func)
    return dist.find_minimal_dist(init_args, maxiter)


def point_in_circle(point: Point, circle: Circle):
    return ((point.x - circle.center.x) ** 2 + (point.y - circle.center.x) ** 2) <= circle.rad ** 2


def point_in_ellipse(point: Point, ellipse: Ellipse):
    return ((point.x / ellipse.a) ** 2 + (point.y / ellipse.b) ** 2) < 1


def point2circle(*, point: Point, circle: Circle) -> float:
    if point_in_circle(point, circle):
        print('POINT INSIDE THE CIRCLE')
    return point2point(point_1=point, point_2=circle.center) - circle.rad


def decart2polar(point: Point):
    r = sqrt(point.x ** 2 + point.y ** 2)
    if point.x > 0 and point.y >= 0:
        theta = atan(point.y / point.x)
    elif point.x > 0 and point.y < 0:
        theta = atan(point.y / point.x) + 2 * pi
    elif point.x < 0:
        theta = atan(point.y / point.x) + pi
    elif point.x == 0 and point.y > 0:
        theta = pi / 2
    elif point.x == 0 and point.y < 0:
        theta = 3 * pi / 2
    else:
        ValueError('Point cannot be converted into polar coordinates')
    return theta, r


class PolarPoint:
    def __init__(self, point: Point):
        self.theta, self.r = decart2polar(point)


class DistanceBetweenPointAndEllipse(Distance):
    def __init__(self, point: Point, ellipse: Ellipse):
        self.polar_point = PolarPoint(point)
        self.polar_ellipse = Ellipse(center=Point(0, 0), a=ellipse.a, b=ellipse.b)

    def dist_func(self, argument):
        theta = argument[0]
        return sqrt(self.polar_point.r ** 2 - 2 * self.polar_point.r * self.polar_ellipse.polar_func(theta)
                    * cos(self.polar_point.theta + theta) + self.polar_ellipse.polar_func(theta) ** 2)


def point2ellipse(*, point: Point, ellipse: Ellipse, init_args=(0, 0), maxiter=500):
    if point_in_ellipse(point, ellipse):
        print('POINT INSIDE THE ELLIPSE')
    point_in_polar = Point(point.x - ellipse.center.x, point.y - ellipse.center.y)
    dist = DistanceBetweenPointAndEllipse(point=point_in_polar, ellipse=ellipse)
    result = dist.find_minimal_dist(init_args, maxiter)
    return result

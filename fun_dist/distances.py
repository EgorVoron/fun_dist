from fun_dist.classes import Point, Circle
from warnings import warn

from math import sqrt

from scipy.optimize import fmin


def pythagoras(dx, dy):
    """Returns square root (dx^2 + dy^2). Is used for calculating hypotenuse's length using Pythagorean theorem
    :param dx: leg, float
    :param dy: leg, float
    :return: length of the hypotenuse, float
    """
    return sqrt(dx ** 2 + dy ** 2)


def point2point(point_1: Point, point_2: Point):
    """Returns distance between two points in 2D space
    :param point_1: first point coordinates, Point
    :param point_2: second point coordinates, Point
    :return: distance between point_1 and point_2, float
    """
    dx = point_1.x - point_2.x
    dy = point_1.y - point_2.y
    return pythagoras(dx, dy)


class Optimum(object):
    """
    Some function's optimum value and it's coordinates in n-dimensional space
    """

    def __init__(self, distance: float, args: list):
        self.args = args
        self.distance = distance

    def __str__(self):
        return f'distance = {self.distance}\nargs: ({self.args})'


class Distance(object):
    """
    Abstract class with realized find_minimal_dist method
    """

    def dist_func(self, *args):
        # Abstract distance function
        return 0

    def find_minimal_dist(self, *args):
        """
        Finds global minimum of distance function
        :return: Optimum object with minimum value and it's coordinates in n-dimensional space
        """
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


def func2func(func_a, func_b, init_args=(0, 0), maxiter=500):
    almost_zero = 1e-4
    dist = DistanceBetweenFunctions(func_a=func_a, func_b=func_b)
    result = dist.find_minimal_dist(init_args, maxiter)
    min_args = result.args
    if abs(func_a(min_args[0]) - func_b(min_args[1])) < almost_zero:
        result.distance = 0
        print('FUNCTIONS INTERSECT')
    return result.distance


class DistanceBetweenPointAndFunction(Distance):
    def __init__(self, point: Point, func):
        self.func = func
        self.point = point

    def dist_func(self, argument):
        x = argument[0]
        point_on_func = Point(x, self.func(x))
        return point2point(self.point, point_on_func)


def point2func(*, point: Point, func, init_args=(0, 0), maxiter=500):
    if func(point.x) == point.y:
        return 0
    dist = DistanceBetweenPointAndFunction(point=point, func=func)
    return dist.find_minimal_dist(init_args, maxiter).distance


def point_in_circle(point: Point, circle: Circle):
    return (point.x - circle.center.x) ** 2 + (point.y - circle.center.x) ** 2 <= circle.radius ** 2


def point2circle(*, point: Point, circle: Circle) -> float:
    if point_in_circle(point, circle):
        warn('POINT INSIDE THE CIRCLE', stacklevel=2)
        return 0
    return point2point(point_1=point, point_2=circle.center) - circle.radius

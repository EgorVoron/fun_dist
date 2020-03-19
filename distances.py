from scipy.optimize import fmin
from math import sqrt
from objects import Point, Circle


def pythagoras(dx, dy):
    return sqrt(dx ** 2 + dy ** 2)


def point2point(point_1: Point, point_2: Point):
    dx = point_1.x - point_2.x
    dy = point_1.y - point_2.y
    return pythagoras(dx, dy)


class Optimum(object):
    def __init__(self, distance: float, args: list):
        self.args = args
        self.distance = distance

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


class DistanceBetweenPointAndFunction(Distance):
    def __init__(self, point: Point, func):
        self.func = func
        self.point = point

    def dist_func(self, argument):
        x = argument[0]
        point_on_func = Point(x, self.func(x))
        return point2point(self.point, point_on_func)


class DistanceBetweenFunctionAndCircle(Distance):
    def __init__(self, circle: Circle, func):
        self.func = func
        self.circle = circle

    def dist_func(self, argument):
        x = argument[0]
        point_on_func = Point(x, self.func(x))
        return point2point(self.circle.center, point_on_func) - self.circle.rad


def point2func(*, point: Point, func, init_args=(0, 0), maxiter=500) -> Optimum:
    dist = DistanceBetweenPointAndFunction(point=point, func=func)
    return dist.find_minimal_dist(init_args, maxiter)


def func2func(func_a, func_b, init_args=(0, 0), maxiter=500) -> Optimum:
    dist = DistanceBetweenFunctions(func_a=func_a, func_b=func_b)
    return dist.find_minimal_dist(init_args, maxiter)


def point2circle(*, point: Point, circle: Circle) -> float:
    return point2point(point_1=point, point_2=circle.center) - circle.rad


def func2circle(*, circle: Circle, func, init_args=(0, 0), maxiter=500) -> Optimum:
    dist = DistanceBetweenFunctionAndCircle(circle=circle, func=func)
    return dist.find_minimal_dist(init_args, maxiter)

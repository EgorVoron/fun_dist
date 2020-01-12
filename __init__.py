from distances import *
from plot import *


def point2circle(*, point_x, point_y, circle_center_x, circle_center_y, circle_radius):
    return point2point(point_x, point_y, circle_center_x, circle_center_y) - circle_radius


def func2circle(*, func, circle_center_x, circle_center_y, circle_radius, init_args=(0, 0), maxiter=1000):
    dist = DistanceBetweenFunctionAndCircle(func, circle_center_x, circle_center_y, circle_radius)
    return dist.find_minimal_dist(init_args, maxiter)


def func2func(func_a, func_b, init_args=(0, 0), maxiter=1000):
    dist = DistanceBetweenFunctions(func_a, func_b)
    return dist.find_minimal_dist(init_args, maxiter)


def point2func(*, func, point_x, point_y, init_args=(0, 0), maxiter=1000):
    dist = DistanceBetweenPointAndFunction(func, point_x, point_y)
    return dist.find_minimal_dist(init_args, maxiter)

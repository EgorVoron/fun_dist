from math import sin, cos, sqrt

from fun_dist.rotate import get_rotated_coordinates


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        self.system_changed = False

    def get_changed_point(self, dx, dy, angle=0):
        new_x, new_y = get_rotated_coordinates(alpha=angle, point=self)
        new_x -= dx
        new_y -= dy
        return Point(new_x, new_y)

    def __str__(self):
        return f'({self.x}, {self.y})'


class Circle:
    def __init__(self, center: Point, radius: float):
        self.center = center
        self.radius = radius

    def __str__(self):
        return f'center = {self.center}, radius = {self.radius}'


class Ellipse:
    def __init__(self, center: Point, a: float, b: float, angle: float = 0):
        self.a = a
        self.b = b
        self.angle = angle
        self.center = center

        def ellipse_polar_func(theta):
            return sqrt(1 / ((cos(theta) / a) ** 2 + (sin(theta) / b) ** 2))

        self.polar_func = ellipse_polar_func

    def get_changed_ellipse(self):
        return Ellipse(center=Point(*get_rotated_coordinates(self.angle, self.center)) if self.angle else self.center,
                       a=self.a, b=self.b)

    def __str__(self):
        return f'center = {self.center}, a = {self.a}, b = {self.b}, angle = {self.angle}'


class LinearFunction:
    def __init__(self, k, b):
        self.k = k
        self.b = b

    def f(self):
        def func(x):
            return self.k * x + self.b

        return func

    def __str__(self):
        return str(self.k) + 'x + ' + str(self.b)

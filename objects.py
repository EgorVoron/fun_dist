from math import sin, cos, sqrt


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        self.system_changed = False

    def change_system(self, dx, dy):
        if self.system_changed:
            raise ValueError('System is already changed')
        self.x = self.x - dx
        self.y = self.y - dy
        self.system_changed = True


class Circle:
    def __init__(self, center: Point, radius: float):
        self.center = center
        self.radius = radius


class Ellipse:
    def __init__(self, center: Point, a: float, b: float):
        self.center = center
        self.a = a
        self.b = b

        def ellipse_polar_func(theta):
            return sqrt(1 / ((cos(theta) / a) ** 2 + (sin(theta) / b) ** 2))

        self.polar_func = ellipse_polar_func


class LinearFunction:
    def __init__(self, k, b):
        self.k = k
        self.b = b

    def f(self):
        def func(x):
            return self.k * x + self.b

        return func

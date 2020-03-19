class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, center: Point, rad: float):
        self.center = center
        self.rad = rad


class LinearFunction:
    def __init__(self, k, b):
        self.k = k
        self.b = b

    def f(self):
        def func(x):
            return self.k * x + self.b

        return func

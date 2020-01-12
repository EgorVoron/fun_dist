from scipy.optimize import fmin


def pythagoras(dx, dy):
    return (dx ** 2 + dy ** 2) ** 0.5


def point2point(point1_x, point1_y, point2_x, point2_y):
    dx = point1_x - point2_x
    dy = point1_y - point2_y
    return pythagoras(dx, dy)


class OptimumPoint(object):
    def __init__(self, x, y, f):
        self.x = x
        self.y = y
        self.f = f

    def __str__(self):
        return f'minimal distance = {self.f}\nargs: ({self.x}, {self.y})'


class AbstractDistance(object):
    def dist_func(self, *args):
        pass


class Distance(AbstractDistance):
    def find_minimal_dist(self, *args):
        init_args, maxiter = args
        min_args = fmin(self.dist_func, init_args, maxiter=maxiter, disp=False)
        return OptimumPoint(min_args[0], min_args[1], self.dist_func(min_args))


class DistanceBetweenFunctions(Distance):
    def __init__(self, func_a, func_b):
        self.func_a = func_a
        self.func_b = func_b

    def dist_func(self, arguments):
        x_a, x_b = arguments
        return point2point(x_a, self.func_a(x_a), x_b, self.func_b(x_b))


class DistanceBetweenPointAndFunction(Distance):
    def __init__(self, func, a_x, a_y):
        self.func = func
        self.a_x = a_x
        self.a_y = a_y

    def dist_func(self, argument):
        x = argument[0]
        return point2point(self.a_x, self.a_y, x, self.func(x))


class Circle(object):
    def __init__(self, center_x, center_y, radius):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius

    def positive_func(self, x):
        return (self.radius - (x - self.center_x) ** 2) ** 0.5 - self.radius

    def negative_func(self, x):
        return -self.positive_func(x)


class DistanceBetweenFunctionAndCircle(Distance):
    def __init__(self, func, circle_center_x, circle_center_y, circle_radius):
        self.func = func
        self.circle = Circle(circle_center_x, circle_center_y, circle_radius)
        self.positive_func = self.circle.positive_func
        self.negative_func = self.circle.negative_func

    def dist_func(self, arguments):
        x_r = arguments[0]
        x_f = arguments[1]
        dist_1 = point2point(x_r, self.positive_func(x_r), x_f, self.func(x_f))
        dist_2 = point2point(x_r, self.negative_func(x_r), x_f, self.func(x_f))
        return min(dist_1, dist_2)

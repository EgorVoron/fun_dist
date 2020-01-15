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
        self.function_value = f

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


class DistanceBetweenFunctionAndCircle(Distance):
    def __init__(self, func, circle_center_x, circle_center_y, circle_radius):
        self.func = func
        self.center_x, self.center_y, self.r = circle_center_x, circle_center_y, circle_radius

    def dist_func(self, argument):
        x = argument[0]
        return point2point(self.center_x, self.center_y, x, self.func(x)) - self.r

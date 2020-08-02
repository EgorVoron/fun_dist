class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class Sphere:
    def __init__(self, center: Point3D, radius: float):
        self.center = center
        self.radius = radius


class Ellipsoid:
    def __init__(self, center: Point3D, a: float, b: float, c: float):
        self.center = center
        self.a = a
        self.b = b
        self.c = c


class Cube:
    def __init__(self):
        # todo
        pass

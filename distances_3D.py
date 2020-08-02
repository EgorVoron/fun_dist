from objects_3d import Sphere, Point3D, Ellipsoid
from math import sqrt
from ellipsoid import point3d_2_ellipsoid


def pythagoras_3d(dx, dy, dz):
    return sqrt(dx ** 2 + dy ** 2 + dz ** 2)


def point3d_2_point3d(point_1: Point3D, point_2: Point3D):
    dx = point_1.x - point_2.x
    dy = point_1.y - point_2.y
    dz = point_1.z - point_2.z
    return pythagoras_3d(dx, dy, dz)


def point3d_2_sphere(point: Point3D, sphere: Sphere):
    return point3d_2_point3d(point, sphere.center) - sphere.radius

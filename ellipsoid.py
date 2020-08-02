from ellipse import *
from objects_3d import Ellipsoid
from sympy import Point3D, Plane, Point2D


def get_cos(v1, v2):
    return abs(v1[0] * v2[0] + v1[1] * v2[1] + v1[2] * v2[2]) / (
            sqrt(v1[0] ** 2 + v1[1] ** 2 + v1[2] ** 2) * sqrt(v2[0] ** 2 + v2[1] ** 2 + v2[2] ** 2))


def get_tan(cosine):
    return sqrt(1 / cosine ** 2 - 1)


def point3d_to_point2d(C: Point3D, x_0, y_0, z_0):
    x_c1 = C.y - y_0
    y_c1 = sqrt((C.x - x_0) ** 2 + (C.z - z_0) ** 2) if C.z > z_0 else -sqrt((C.x - x_0) ** 2 + (C.z - z_0) ** 2)
    return Point2D(x_c1, y_c1)


def ellipsoid3d_to_ellipse2d(a, b, c, x_0, y_0, z_0, C: Point3D):
    F = Point3D(x_0, y_0 + b, z_0)
    G = Point3D(x_0, y_0 - b, z_0)
    new_plane = Plane(F, G, C)  # плоскость FGC
    cosine = get_cos(new_plane.normal_vector, (0, 0, 1))
    tan = get_tan(cosine)
    a1 = b
    b1 = sqrt(a ** 2 * c ** 2 / (a ** 2 * tan ** 2 + c ** 2) + tan ** 2 * (
            a ** 2 * c ** 2 / (a ** 2 * tan ** 2 + c ** 2)))
    return a1, b1


def distance_3d(C: Point3D, a, b, c, x_0, y_0, z_0):
    C1 = point3d_to_point2d(C, x_0, y_0, z_0)
    if C1.y < 0:
        C1 = Point2D(C1.x, -C1.y)
    a1, b1 = ellipsoid3d_to_ellipse2d(a, b, c, x_0, y_0, z_0, C)
    Q = nearest_point(C1, a1, b1)
    return D(C1, Q.x, a1, b1)


def point3d_2_ellipsoid(point: Point3D, ellipsoid: Ellipsoid):
    return distance_3d(point, ellipsoid.a, ellipsoid.b, ellipsoid.c,
                       ellipsoid.center.x, ellipsoid.center.y, ellipsoid.center.z)

import numpy as np


def matrix2coordinates(matrix):
    return matrix[0][0], matrix[1][0]


def get_rotate_matrix(alpha):
    return np.array([[np.cos(alpha), -np.sin(alpha)],
                     [np.sin(alpha), np.cos(alpha)]])


def get_rotated_coordinates(alpha, point):
    rotate_matrix = get_rotate_matrix(alpha)
    rotated_point_matrix = rotate_matrix @ np.array([[point.x], [point.y]])
    return matrix2coordinates(rotated_point_matrix)

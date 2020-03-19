"""
Work in progress
"""

# import matplotlib.pyplot as plt
# import warnings
# import numpy as np
#
# warnings.filterwarnings("ignore")
#
#
# def plot_func2func(xmin, xmax, ymin, ymax, function_a, function_b, min_args):
#     dx = 0.01
#     xlist = np.linspace(xmin, xmax, num=round((xmax - xmin) / dx))
#     ylist = [function_a(x) for x in xlist]
#
#     xlist2 = np.linspace(xmin, xmax, num=round((xmax - xmin) / dx))
#     ylist2 = [function_b(x) for x in xlist2]
#
#     figsize = 5
#     plt.figure(figsize=(figsize, figsize))
#     plt.plot(xlist, ylist)
#     plt.plot(xlist2, ylist2)
#     plt.plot([min_args[0], min_args[1]], [function_a(min_args[0]), function_b(min_args[1])], color='r', alpha=1)
#
#     plt.xlim(xmin, xmax)
#     plt.ylim(ymin, ymax)
#     plt.gca().set_aspect('equal', adjustable='box')
#
#     plt.title('Result')
#     plt.legend(['a(x)', 'b(x)', 'Min dist'], loc='upper right')
#     plt.show()

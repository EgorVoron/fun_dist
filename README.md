# fun_dist

[![Latest PyPI version](https://img.shields.io/pypi/v/fun-dist.svg)](https://pypi.org/project/fun-dist/0.0.1b0/)
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)

A python package, that provides functions for calculating **distances** between points, functions, circles and ellipses and finding **tangents** of functions


### Dependencies
* [Scipy](https://github.com/scipy/scipy)
* [Sympy](https://github.com/sympy/sympy)

### Example
```
from fun_dist import func2func

def a(x):
    return -2 * x + 2


def b(x):
    return (x - 4) ** 2

print(func2func(a, b))  # 2.2360679793027156
```

```
Includes classes:
Point, Circle, Ellipse, LinearFunction

Includes functions: 
point2point - returns distance between two objects of class Point
point2func - returns minimal distance between object of class Point and function
func2func - returns minimal distance between two functions
point2circle - returns minimal distance between object of class Point and object of class Circle
point2ellipse - returns minimal distance between object of class Point and object of class Ellipse
func_tangent - returns object of class LinearFunction, which is tangent of input function
circle_tangent_len - returns length of tangent from input point to input circle
```
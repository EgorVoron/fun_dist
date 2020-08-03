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
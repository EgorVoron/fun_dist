# fun_dist
A python package, that provides functions for calculating **distances** between points, functions, circles and finding **tangents** of functions and circles

### Dependencies
* [Scipy](https://github.com/scipy/scipy)

### Example
```
from fun_dist import func2func

def a(x):
    return -2 * x + 2


def b(x):
    return (x - 4) ** 2

print(func2func(a, b).distance)  # 2.2360679793027156
```
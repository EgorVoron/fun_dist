# fun_dist
A python package that provides functions for calculating minimal distance between functions and other math objects

### Dependencies
* [Numpy](https://github.com/numpy/numpy)
* [Scipy](https://github.com/scipy/scipy)
* [Matplotlib](https://github.com/matplotlib/matplotlib)

### Example
```import fun_dist


def a(x):
    return x ** 2


def b(x):
    return -(x + 4) ** 2 - 3


dist = fun_dist.func2func(a, b)
min_x, min_y, min_value = dist.x, dist.y, dist.function_value
print(min_x, min_y, min_value)```

### Installation
```Installation sucks```

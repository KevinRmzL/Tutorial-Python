"""
This scrib is used to created a module that
we´re going to import in "m5_test_module"
"""

from typing import Optional, List, Union

print("I am being executed!")

# some_list contains str, int, and None
some_list: List[Union[str, int, None]] = ["a", 1, None]


# square and cube take an int or float and return the same type
def square(x: Union[int, float]) -> Union[int, float]:
    return x**2


def cube(x: Union[int, float]) -> Union[int, float]:
    return x**3

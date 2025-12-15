"""
Type hints are a feature in Python that allow developers to annotate their code with expected 
types for variables and function arguments. This helps to improve code readability and provides
an opportunity to catch errors before runtime using type checkers like mypy.

Personal note: The idea is similar to declare a specific type of variable in other programming languajes
like C++ or Java
"""

age: int = 25
def greet(name: str) -> str:
    return f"Hello, {name}!"

"""
age is an integer (int).
greet function expects a string (name: str) and returns a string (-> str).
"""


"""
For complex datastructures like a list, tuple or dictionary we need 
to import typing. 
"""

from typing import Optional, List, Tuple

def get_user(id: int) -> Optional[str]:
    return None if id == 0 else "User"

def sum(num: List[int]) -> int:
    return sum(num)

def get_name_and_age() -> Tuple[str, int]:
    return ("Abc", 25)

"""
Optional[str]: The get_user function can return either a string or None.
List[int]: The sum_numbers function expects a list of integers.
Tuple[str, int]: The get_name_and_age function returns a tuple with a string and an integer.
"""

# To colaborate that our code is clean and don´t have errors in type hints 
# we can install mypy
 
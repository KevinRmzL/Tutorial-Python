# python3 -m venv myenv
# tutorial-env\Scripts\activate.bat

from typing import List

class MyGuy:
    x: int = 1 + 2
    y: List[int] = [2, 4, 6]
    z: str = "hi"

    @staticmethod
    def f() -> int:  # Static method with return type
        return 3

# Access class attributes
print(MyGuy.x)
print(MyGuy.y)
print(MyGuy.z)

# Check if attribute exists (the method need to be behind "")
print(hasattr(MyGuy, "z"))

# Get attribute value
print(getattr(MyGuy, "z"))

# Init set the values to each method of the class
class Person:
    x: int = 1  # Class-level attribute

    def __init__(self, name: str) -> None:
        """Executed when creating a new Person instance."""
        self.name: str = name

        # __init__ cannot not return any value other than `None`. Its sole purpose is to affect
        # `self`, the instance of `Person` that is being created


list_of_people = [Person(n) for n in ("Fermi", "Noether", "Euler")]

for person in list_of_people:
    print(person.name)
    print(person.x)

print("Static Methods".center(50, "="))

"""
The class don´t pass any atributte, the user provide them
"""
class Dummy:
    @staticmethod
    def static_func() -> str:
        """Always returns 'hi'."""
        return 'hi'


# python3 -m venv myenv
# tutorial-env\Scripts\activate.bat

from typing import Tuple

"""
Example of inheritance to create a square.
"""

class Rectangle:
    """A class that describes the properties of a rectangle."""
    def __init__(self, width: int, height: int, center: Tuple[int, int] = (0, 0)) -> None:
        self.width: int = width
        self.height: int = height
        self.center: Tuple[int, int] = center

    def __repr__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height}, center={self.center})"

    def compute_area(self) -> int:
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side: int, center: Tuple[int, int] = (0, 0)) -> None:
        super().__init__(side, side, center)


# Example usage
my_square = Square(2)
print(my_square.compute_area())

# Check inheritance

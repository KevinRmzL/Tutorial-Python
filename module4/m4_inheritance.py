"""
Ejemplo de herencia para crear un cuadrado. 
"""

class Rectangle:
    """ A class of Python object that describes the properties of a rectangle"""
    def __init__(self, width, height, center=(0, 0)):
        self.width = width
        self.height = height
        self.center = center

    def __repr__(self):
        return "Rectangle(width={w}, height={h}, center={c})".format(h=self.height,
                                                                     w=self.width,
                                                                     c=self.center)

    def compute_area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side, center=(0, 0)):
        # equivalent to `Rectangle.__init__(self, side, side, center)`
        super().__init__(side, side, center)

# Notese que se reciclan los metodos usados para el rectangulo
my_square = Square(2)
print(my_square.compute_area())

# Funciones que no conocia 

# Indica que una clase derivada es subclase de una clase padre
print(issubclass(Square, Rectangle))


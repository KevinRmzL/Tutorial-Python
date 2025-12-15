# python3 -m venv myenv
# tutorialp/Scripts/activate

class MyGuy:
    x = 1 + 2
    y = [2, 4, 6]
    z = "hi"

    def f():
        return 3

# Llamamos a cada uno de los atributos creados   
print(MyGuy.x)
print(MyGuy.y)
print(MyGuy.z)

# Con hasttr se puede comprobar si existe el metodo denotado en las ""
print(hasattr(MyGuy, "z"))

# Con getattr se visualiza el contenido de un metodo 
print(getattr(MyGuy, "z"))

# Init asigna valores base a los metodos de la clase  
class Person:
    x = 1  # this sets a class-level attribute, common to all instances of `Person`

    def __init__(self, name):
        """ This method is executed every time we create a new `Person` instance.
            `self` is the object instance being created."""
        self.name = name   # set the attribute `name` to the Person-instance `self`

        # __init__ cannot not return any value other than `None`. Its sole purpose is to affect
        # `self`, the instance of `Person` that is being created

list_of_people = [Person(n) for n in ("Fermi", "Noether", "Euler")]

for person in list_of_people:
    print(person.name)
    print(person.x)

print("Static Methods".center(50,"="))
# La clase no pasa ningun argumento al metodo, todo lo especifica el usuario. Por eso no usa el self
class Dummy:

    @staticmethod
    def static_func():
        """ A static method defined to always returns
            the string `'hi'`"""
        return 'hi'


print(Dummy.static_func())


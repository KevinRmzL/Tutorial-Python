"""
This code provide basic knownledge of some 
Python methods and operations. I divide the 
code in different parts with the use of headers 
"""

from typing import List, Any

"""Operations and methods """

# floor operation 
print(1 // 3)

print("Complex numbers")
print("-"*30)

i1 : complex = complex(2, 3)
print("1.", i1)


i2 : complex = complex(0, 1)**2
print("2.", i2)

# Verification of a data structure 
i3 : complex = isinstance(2-4j, complex)
print("3.", i3)


"""List and another operators"""


print("None operator & logic operators")
print("-"*30)

y : None = None 
print("1.", y is None)

large_num : None = None

for number in [1, 2, 3, 4, 11]:
    if number > 10:
        large_num : int = number
        break

if large_num is None:
    print("2. The list did not contain any number larger than 10")
else:
    print("2. There is a big number")


"""Strings and join of elements """


print("Strings")
print("-"*30)

# Joint the elements ...
print("...".join(["item1", "item2", "item3"]))

# Diccionaries with strings (append the element to the diccionarie)
print("x: {}, y: {}, z: {}".format(3.2, 8.4, -1.0))

name : str = "Kevin"
age : int = 21
print(f"{name} has {age} years old")

print("Lists")
print("-"*30)

# We can create a listas of strings with the method list 
print(list("Kevin"))

# List
x : List[int] = [2, 4, 6, 8, 10]
y : List[int] = [2, 4, 6, 8, 10]
print(f"\n Initial List {y}")

# Slicing para remplazar elementos del array 
y[1:4] = [-3, -4, -5]
print(f"\n Resulting List {y}")

y.remove(2)
print(f"\nList without an element {y}")

# Cuando se quiere agregar solo un elemento
y.append(100)
print(f"\nList with append {y}")

# Cuando se quieren agregar varios elementos (similar al sum)
y.extend(["Hello", "World", "c:"])
print(f"\nExtend list {y}")

# Devuelve el elemento indicado por el indice 
print(y.pop(-1))

# .center centra el texto x numeros 
print("Hello".center(20, "-"))

names : str = ["Jane", "Adam", "Ryan", "Bob", "Zordon", "Jack", "Jackenzie"]
# Ordena los elementos por orden alfabetico 
names.sort()
print(names)


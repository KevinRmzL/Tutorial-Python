# Operación piso (no me acordaba que existia)
print(1 // 3)

print("Numeros imaginarios")
print("-"*30)

i1 = complex(2, 3)
print("1.", i1)


i2 = complex(0, 1)**2
print("2.", i2)

# Verificación de un tipo de dato
i3 = isinstance(2-4j, complex)
print("3.", i3)

print("None operator y operadores logicos")
print("-"*30)

y = None 
print("1.", y is None)

large_num = None

for number in [1, 2, 3, 4, 11]:
    if number > 10:
        large_num = number
        break

if large_num is None:
    print("2. The list did not contain any number larger than 10")
else:
    print("2. There is a big number")

print("Strings")
print("-"*30)

# Union de elementos con ...
print("...".join(["item1", "item2", "item3"]))

# Diccionarios con strings (añade el elemento al diccionario)
print("x: {}, y: {}, z: {}".format(3.2, 8.4, -1.0))

name = "Kevin"
age = 21
print(f"{name} tiene {age} años")


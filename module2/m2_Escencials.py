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

print("Listas")
print("-"*30)

# Se pueden crear listas de strings con el metodo list 
print(list("kevin"))

# Listas
x = [2, 4, 6, 8, 10]
y = [2, 4, 6, 8, 10]
print(f"\nLista inicial {y}")

# Slicing para remplazar elementos del array 
y[1:4] = [-3, -4, -5]
print(f"\nLista resultante {y}")

y.remove(2)
print(f"\nLista con elemento removido {y}")

# Cuando se quiere agregar solo un elemento
y.append(100)
print(f"\nLista con append {y}")

# Cuando se quieren agregar varios elementos (similar al sum)
y.extend(["Hello", "World", "c:"])
print(f"\nLista con extend {y}")

# Devuelve el elemento indicado por el indice 
print(y.pop(-1))

# .center centra el texto x numeros 
print("Hello".center(20, "-"))

names = ["Jane", "Adam", "Ryan", "Bob", "Zordon", "Jack", "Jackenzie"]
# Ordena los elementos por orden alfabetico 
names.sort()
print(names)


print("Data Structures - Dictionaries".center(50,"-"))
print("="*60)
print("Un diccionario es una estructura llave-valor\n " \
    "Similar a una lista. Donde se acceden a los elementos\n" \
    "con un par de []. Puede almacenar todo tipo de datos\n" \
    "y resulta bastante sencilla de manipular. Se declara con \n" \
    "un par de {}. Cada llave y valor esta separada por :")
print("="*60)

# Declaración de un diccionario - Por clave
items_to_prices = {"cheese": 2.53, "milk": 3.40, "frozen pizza": 8.01}
print(items_to_prices["frozen pizza"])

# Declaración de un diccionario - Por valor
point_to_region = {(0.1, 2.2, 3):False, (-10., 0, 4.5):True, (4.3, 1.0, 9.5):False}
print(point_to_region[(-10., 0, 4.5)])

# Por medio de un ciclo para asignar clave, valor
print({k:v for k,v in [("apple", "fruit"), ("carrot", "vegetable")]})


brainrotdic = {"tralalelotralala" : "god", "Tung tung tung sahur" : "god", "vaca saturno saturnita" : "legendary"}
print(len(brainrotdic))
print(brainrotdic["tralalelotralala"])
brainrotdic["Boneca Ambalabu"] = "mid"
print(brainrotdic)

# La función update te permite agregar más elementos 
brainrotdic.update([("Capuchino Asessino", "god"),("Orcalero orcala","mid")])
print(brainrotdic)

# Ver llaves del diccionario 
print([i for i in brainrotdic])

# Ver valores del diccionario 
print([i for i in brainrotdic.values()])


print("Data Structures - Sets".center(50,"-"))
print("="*60)
print("Similar a una lista, es una estructura donde los elementos \n" \
" del set NO se repiten, son unicos \n" \
" Se declara con un par de llaves, al igual que un \n" \
" diccionario. Salvo que cada llave y valor esta separada por una ,")
print("="*60)

# Creamos un set 
# Notese que al correr el código los elementos del set se ordenan
myset = {1,2,2,10, "Hola", "Mundo", "Tilin", 100, 90.5,500,50}
print(myset)
# Podriamos crear tambien un set así
print([i for i in myset])

mynewset = {15,4,3,2,7,10,100,200}

# Podemos hacer operaciones con sets tales como:
print(myset and mynewset)

print(myset - mynewset)

print(myset & mynewset)

print(myset | mynewset)

myset.add(80)
print(myset.update)
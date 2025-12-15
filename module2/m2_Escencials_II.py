print("Tuplas".center(20,"-"))
# A diferencia de una lista, esta NO se puede cambiar 
y = [1,2,3,4]
x = tuple(y)
print(x,y)

# El metodo count cuenta numeros o caracteres
text = "En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho tiempo que viva un hidalgo de los de lanza en astillero, adarga antigua, rocn flaco y galgo corredor"
print(text.count("e"))

# Slicing en texto
#       inicio|fin
print(text[0:41])
#    inicio|fin|step
print(text[0:41:2])

print(text[:])

# Recorre todo el texto en saltos de 2
print(text[::2])

# Recorre todo el texto en saltos de 2 de atras hacia adelante 
print(text[::-2])

first_item = None

print("Operadores".center(20,"-"))
y = [1,2,3,4,5,6]
x = [1,2,3,4,5,6]
print(5 in y)

print(x is y)
print(x is not y)
print(x == y)



print("Bucle For".center(20, "-"))

# Una forma chistosa para ir iterando puede ser con next. Que te permite hacer "peticiones" al ciclo for 
# Lo veo util para debuggear 
short_gen = (i/2 for i in [1, 2, 3])

print(next(short_gen))

print(next(short_gen))

print(next(short_gen))

# Forma de crear una lista con ciclos for
print([i**2 for i in range(0,10)])

out = []
for i in "Hello. How Are You?":
    if i.islower():
        out.append(1 if i == "o" else 0)
        print(out)

names = ["Angie", "Brian", "Cassie", "David", "Kevin"]
exam_1_scores = [90, 82, 79, 87, 80]
exam_2_scores = [95, 84, 72, 91,100, 50]

# Zip Crea una lista donde concatena elementos de x listas dependiendo a la posición de los indices 
print(list(zip(names, exam_1_scores, exam_2_scores)))
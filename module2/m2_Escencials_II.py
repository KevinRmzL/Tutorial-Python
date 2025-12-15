"""
In this code we´re to introduce more concepts of the list as a 
datastrure. Addicionally, we´re going to introduce a new structure: A tuple
"""
from typing import List, Optional, Iterator


print("\nTuple\n".center(50,"-"))
# In contrast to a List, a tuple CANNOT change
y : tuple[int] = (1,2,3,4)
x : tuple[int]= tuple(y)
print(x,y)

# The count method counts numbers or characters
text : str = "En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho tiempo que viva un hidalgo de los de lanza en astillero, adarga antigua, rocn flaco y galgo corredor"
print(text.count("e"))

# Text Slicing
#       begging|end
print(text[0:41])
#       begging|end
print(text[0:41:2])

print(text[:])

# Move the text in 2 units (jumps/steps)
print(text[::2])

# Move the text in 2 units (jumps/steps) beggining at the end
print(text[::-2])

first_item : Optional[int] = None

print("\nOperadores\n".center(50,"-"))
y : list[int] = [1,2,3,4,5,6]
x : list[int] = [1,2,3,4,5,6]
print(5 in y)

print(x is y)
print(x is not y)
print(x == y)



print("\nFor Loop\n".center(20, "-"))

"""
Another funny way to iterate is with next.
it allows you to create "request" in a for loop 
I think that is usesfull for debbuing
"""

short_gen : Iterator[float] = (i/2 for i in [1, 2, 3])

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
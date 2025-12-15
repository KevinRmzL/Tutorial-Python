Modos de visualización de archivos usando pickle
![alt text](anexos/image-2.png)

Ejemplo:
import pickle

* pickling a dictionary - Comprimiendo un diccionario de datos
with open("grades.pkl", mode="wb") as opened_file:
    pickle.dump(grades, opened_file)

* Desempaquetando un archivo .pkl
with open("grades.pkl", mode="rb") as opened_file:
    my_loaded_grades = pickle.load(opened_file)


Tambien se pueden guardar arreglos de numpy por si los queremos usar
en otros archivos 

1. import numpy as np
x = np.array([1, 2, 3])

2. save a numpy array to disk
np.save("my_array.npy", x)

3. load the saved array from disk
y = np.load("my_array.npy")

En caso de tener más arreglos los podemos guardar con:
`numpy.savez`






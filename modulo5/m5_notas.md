Modos de visualización de archivos usando pickle
![alt text](image.png)

Ejemplo:
import pickle

# pickling a dictionary
with open("grades.pkl", mode="wb") as opened_file:
    pickle.dump(grades, opened_file)

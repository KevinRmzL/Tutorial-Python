Diferrent file visualization
![alt text](images/image-2.png)

Pickling a Dictionary
Pickling is the process of serializing Python objects so they can be saved to a file and loaded later.

Example:
import pickle

1. Pickling a dictionary
with open("grades.pkl", mode="wb") as opened_file:
    pickle.dump(grades, opened_file)

2. Unpickling a .pkl file
with open("grades.pkl", mode="rb") as opened_file:
    my_loaded_grades = pickle.load(opened_file)


Saving and Loading NumPy Arrays
You can also save NumPy arrays to reuse them in other scripts.

1. Create a NumPy array:
import numpy as np
x = np.array([1, 2, 3])


2. Save a NumPy array to disk:
np.save("my_array.npy", x)


3. Load the saved array from disk:
y = np.load("my_array.npy")


Saving Multiple Arrays
If you have multiple arrays, you can save them together using:
4. np.savez("multiple_arrays.npz", array1=x, array2=y)





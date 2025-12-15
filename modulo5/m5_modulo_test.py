"""
Poniendo un import a un archivo receptor podemos tener más de 
un solo scrib comunicandose con otros. Lo que nos permite 
tener una estructura de trabajo más modular (similar a ROS2 con los
nodos de emisor-receptor)
"""

import m5_modulo_prueba
print(type(m5_modulo_prueba))

# Con el modulo importado, como si fuera una libreria podemos acceder a ella y modificarla
print(m5_modulo_prueba.some_list)

# Podemos enviar de igual forma datos a la función dentro del modulo
print(m5_modulo_prueba.square(4))

# Help nos da una vista en la terminal de todo lo que contiene el scrib que importamos  
print(help(m5_modulo_prueba))
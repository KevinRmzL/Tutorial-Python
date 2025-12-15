"""
By importing into a receiver file, we can have more than one script communicating with others.
This allows us to create a more modular work structure.
Personal note: similar to ROS2 with its publisher-subscriber nodes.
"""

import m5_module

print(type(m5_module))

# Con el modulo importado, como si fuera una libreria podemos acceder a ella y modificarla
print(m5_module.some_list)

# Podemos enviar de igual forma datos a la función dentro del modulo
print(m5_module.square(4))

# Help nos da una vista en la terminal de todo lo que contiene el scrib que importamos
print(help(m5_module))

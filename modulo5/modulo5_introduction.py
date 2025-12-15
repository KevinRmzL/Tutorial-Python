# python3 -m venv myenv
# tutorialp/Scripts/activate

"""
El modulo 5 es un mix de guias de:
-----------------------------------
* Buenas práticas de código siguiendo la guia PEP8
    * Guias de estilo para el códigi 
* MatplotLib como libreria para la gráficación de datos
* Importación y exportación de datos usando modulos 
* Otros paquetes y librerias 
"""

import matplotlib.pyplot as plt
import numpy as np


# Toda constante debe estar estrita en mayusculas y con _ si hay espacios
CIRC_RADIUS = 0.2

# Una función y clase debe tener minimo una distancia de 2 renglones 

# Do:
def func_a():
    """I am function a"""
    return 1


def func_b():  # separated from func_a by two blank lines
    """I am function b"""
    return 2

# demonstrating wide range of functionality controlled
# by the axes object.

# create a figure with multiple axes
fig, axs = plt.subplots(2, 3, figsize=(8, 3)) # 6 axes on a 2x3 grid
# note that we could also use tuple unpacking for our axes:
# fig, (ax1, ax2, ax3, ax4, ax5, ax6) = plt.subplots(2, 3)


# the domain of x-values on which we evaluate
# our functions
x = np.linspace(0, 4*np.pi, 1000)

# row-0, col-0: plot y = x**2
axs[0, 0].plot(x, x**2, linestyle='--', color='orange')

# row-0, col-1: plot y = sin(x)
axs[0, 1].plot(x, np.sin(x), color='green')

# row-0, col-2:  plot y = cos(x)
axs[0, 2].plot(x, np.cos(x), linestyle=':')

# row-1, col-0:  plot y = exp(x)
axs[1, 0].plot(x, np.exp(x), color='red', linestyle='-.')

# row-1, col-1:  plot y = sqrt(x)
axs[1, 1].plot(x, np.sqrt(x))

# row-1, col-2:  plot y = x
axs[1, 2].plot(x, x, color='purple');


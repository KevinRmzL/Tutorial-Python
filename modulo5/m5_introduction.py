# python3 -m venv myenv
# tutorial-env\Scripts\activate.bat

# python3 -m venv myenv
# tutorial-env\Scripts\activate.bat

"""
Module 5 is a mix of guides:
-----------------------------------
* Best coding practices following the PEP8 guide
    * Style guidelines for code
* Matplotlib as a library for data visualization
* Importing and exporting data using modules
* Other packages and libraries
"""

import matplotlib.pyplot as plt
import numpy as np

# All constants should be written in uppercase and use underscores (_) for spaces
CIRC_RADIUS : float = 0.2

# A function and a class should have at least two blank lines between them

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


"""
This file is a complement for the "modulo5". Presenting the Docstrings
Docstrings (Documentation Strings) are special strings used to document Python code.
They provide a description of what a module, class, function or method does.
"""

# 1. This type of style is called Triple-Quoted Strings


def my_function():
    """Demonstrates triple quotes docstring and does nothing."""
    return None


print("Using __doc__:")
print(my_function.__doc__)

print("Using help():")
help(my_function)

# 2. The style that we are going to use is called Google Style Docstrings


def multiply(a, b):
    """
    Multiply two numbers.

    Args:
        a (int): First number.
        b (int): Second number.

    Returns:
        int: Product of a and b.
    """
    return a * b


print(multiply(3, 5))

"""
In the previus style we defined the I/O. Adiccionaly, exist a more complex 
style based in this called Numpydoc Style Docstrings 

"""

# One-line Docstrings


def power(a, b):
    """Return a raised to power b."""
    return a**b


print(power.__doc__)


"""
======================================================================
Diference between a comment, string and docstring 
======================================================================
Comments (#): Explain code but are ignored by Python at runtime.
Strings (" " or ' '): Represent text data and are used in variables/operations.
Docstrings (""" """): Special strings placed below definitions to document
modules, classes or functions. Unlike comments, they can be accessed using __doc__ or help().

A example is written below 
"""

# This is a comment (ignored by Python)

name = "Daniel"  # A string assigned to a variable


def greet():
    """This is a docstring. It explains what greet() does."""
    return "Hello!"

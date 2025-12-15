print("\nData Structures - Dictionaries\n".center(100, "-"))

from typing import List, Any, Set, Dict

"""
A dictionary is a key-value structure
Similar to a list. Where elements are accessed
with a pair of []. It can store all types of data
and is quite easy to manipulate. It is declared with
a pair of {}. Each key and value is separated by :
"""


# Dictionary - for key
items_to_prices: Dict[str, float] = {"cheese": 2.53, "milk": 3.40, "frozen pizza": 8.01}
print(items_to_prices["frozen pizza"])

# Dictionary - for value
point_to_region: Dict[float, float] = {
    (0.1, 2.2, 3): False,
    (-10.0, 0, 4.5): True,
    (4.3, 1.0, 9.5): False,
}
print(point_to_region[(-10.0, 0, 4.5)])

# Dictionary costructed with loops
print({k: v for k, v in [("apple", "fruit"), ("carrot", "vegetable")]})

# At this part of the programming I was falling slept. So, don´t put attention in
# the names and follow scrolling
brainrotdic: Dict[str, str] = {
    "tralalelotralala": "god",
    "Tung tung tung sahur": "god",
    "vaca saturno saturnita": "legendary",
}
print(len(brainrotdic))
print(brainrotdic["tralalelotralala"])
brainrotdic["Labubu"] = "mid"
print(brainrotdic)

# The update function allows us append more elements
brainrotdic.update([("Capuchino Asessino", "god"), ("Orcalero orcala", "mid")])
print(brainrotdic)

# See Key
print([i for i in brainrotdic])

# See values
print([i for i in brainrotdic.values()])


print("\nData Structures - Sets\n".center(100, "-"))


"""
Similar to a list, it is a structure where the elements
of the set are NOT repeated, they are unique; another 
characteristic is that a set CANNOT be editable
It is declared with a pair of curly brackets, just like a
dictionary. Except that each key and value is separated by a comma.
"""


# We create a set
myset: Set[Any] = {1, 2, 2, 10, "Hello", "World", "Boys", 100, 90.5, 500, 50}
print(myset)
# Another way to create a set
print([i for i in myset])

mynewset: set[Any] = {15, 4, 3, 2, 7, 10, 100, 200}

"""\nIn a set we can make this operations\n"""

print(myset and mynewset)

print(myset - mynewset)

print(myset & mynewset)

print(myset | mynewset)

myset.add(80)
print(myset.update)

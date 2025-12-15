"""
This module consist in 4 different problems to practice:
* Dictionaries
* Slicing
* Data Structures
"""

from typing import List, Iterable, Any


print("Problem 1 - Dictionary Merge".center(50, "="))

dict1: dict[str, int] = {"bananas": 7, "apples": 3, "pears": 14}
dict2: dict[str, int] = {"bananas": 3, "apples": 6, "grapes": 9}
merged = dict1


def mergedic(d1: dict[str, int], d2: dict[str, int]) -> dict[str, int]:
    """
    Merge two dictionaries by taking the maximum value for each key.
    Does not mutate the inputs.
    """
    for i in dict2:
        print(i)
        if i not in merged or dict2[i] > merged[i]:
            merged[i] = dict2[i]
    return merged


finaldic: dict[str, int] = mergedic(dict1, dict2)
print(finaldic)

print("Problem 2 - Satisfactory test".center(50, "="))
"""
Calculate if a value is desired or non-desired in base to a tolerance margin.
Compare an actual list vs desired values 
"""

desired: List[float] = [10.0, 5.0, 8.0, 3.0, 2.0]
actual: List[float] = [10.3, 5.2, 8.4, 3.0, 1.2]
margin: float = 0.5


def margen_de_perdida(
    desired: Iterable[float], actual: Iterable[float], margin: float
) -> tuple[int, int]:
    count: int = 0
    badcount: int = 0
    for i in range(len(actual)):
        res = desired[i] - actual[i]

        if abs(res) >= margin:
            badcount += 1
            print(f"{badcount}/{len(actual)} no desired")
        else:
            count += 1
    return print(f"{count}/{len(actual)} desired")


margen_de_perdida(desired, actual, margin)

print("Problem 3 - Fanout Number".center(50, "="))
"""
Calculate all the posible combinations with an array of values 
with a n-dimension. Acording to this, in each iteration give us 
n - 1 posible combination with the actual numbers 
"""
mylist: List[int] = [3, 2, 4, 6, 1]
fanout_value: int = 3


def difference_fanout(list, value):
    out: List[List[int]] = []  # Lista principal para guardar todas las sublistas
    for i in range(len(mylist)):
        sublist: List[int] = []  # Sublista para las diferencias del elemento actual
        for j in range(i + 1, min(i + 1 + value, len(mylist))):
            sublist.append(mylist[i] - mylist[j])
        out.append(sublist)
    return out


# Probar la función
result: List[List[int]] = difference_fanout(mylist, fanout_value)
print(result)

print("Problem 4 - Diccionary".center(50, "="))
"""
Transform a list of any type of values to a string 
"""
s: List[Any] = [12, -14.23, "hello", True, "Aha", 10.1, None, 5]


def int_to_str(n: int) -> str:
    number_dic: dict[str, str] = {
        "0": "zero",
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine",
        "-": "neg",
    }
    return "-".join(number_dic[digit] for digit in str(n))


def item_to_transcript(item: Any) -> str:
    if isinstance(item, bool):
        return "<OTHER>"
    if isinstance(item, int):
        return int_to_str(item)
    if isinstance(item, float):
        return int_to_str(int(item)) + " and float"
    if isinstance(item, str):
        return item
    return "<OTHER>"


def concat_to_str(s: Iterable[Any]) -> str:
    return print(" | ".join(item_to_transcript(item) for item in s))


print(concat_to_str(s))

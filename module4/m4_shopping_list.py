# Example of classes and metothds
from typing import List, Iterable


class ShoppingList:
    def __init__(self, items: str | Iterable[str]) -> None:
        """Parameters
        ----------
        items : Union[str, Iterable[str]]
            Iterable of item-names to add to shopping list"""
        if isinstance(items, str):
            items = [items]
        self._needed = set(items)
        self._purchased = set()

    def add_new_items(self, items: str | Iterable[str]) -> None:
        """Add more items to the shopping list

        Parameters
        ----------
        items : Union[str, Iterable[str]]
            Iterable of item-names to add to shopping list"""

        if isinstance(items, str):
            items: List = [items]
        # set.update adds elements of an iterable to a set
        self._needed.update(items)

    def mark_purchased_items(self, items: str | Iterable[str]) -> None:
        """Provide names of items to mark as 'purchased'

        Parameters
        ----------
        items : Union[str, Iterable[str]]"""
        if isinstance(items, str):
            items: List = [items]
        # only mark items as purchased that are on our list to begin with
        self._purchased.update(set(items) & self._needed)
        # remove all purchased items from our unpurchased set
        self._needed.difference_update(self._purchased)

    def list_purchased_items(self) -> List[str]:
        """Return a sorted list of the items that have been purchased"""
        return sorted(self._purchased)

    def list_unpurchased_items(self) -> List[str]:
        """Return a sorted list of the items still on the list"""
        return sorted(self._needed)


my_list: List[str] = ShoppingList(
    ["apples", "apples", "grapes", "peaches", "milk", "bread", "pineapples"]
)
print("Unpurchased items: ", my_list.list_unpurchased_items())

my_list.mark_purchased_items(["grapes", "pineapples"])
print("Bougth items: ", my_list.list_purchased_items())

print("Missing items:", my_list.list_unpurchased_items())


def strike(text):
    """Renders string with strike-through characters through it.

    `strike('hello world')` -> '̶h̶e̶l̶l̶o̶ ̶w̶o̶r̶l̶d'

    Notes
    -----
    \u0336 is a special strike-through unicode character; it
    is not unique to Python."""
    return "".join("\u0336{}".format(c) for c in text)


print("=" * 50)

"""
Exist another costructers beside __init__ like:
* __repr__(self)
* __str__(self)

The documentation with more detail is bellow:
https://www.pythonlikeyoumeanit.com/Module4_OOP/Special_Methods.html
"""


class ShoppingList2:
    def __init__(self, items):
        self._needed: set = set(items)
        self._purchased = set()

    def __repr__(self):
        """Returns formatted shopping list as a string with
        purchased items being crossed out.

        Returns
        -------
        str"""
        if self._needed or self._purchased:
            remaining_items = [str(i) for i in self._needed]
            purchased_items = [strike(str(i)) for i in self._purchased]
            # You wont find the • character on your keyboard. I simply
            # googled "unicode bullet point" and copied/pasted it here.
            return "• " + "\n• ".join(remaining_items + purchased_items)

    def add_new_items(self, items):
        self._needed.update(items)

    def mark_purchased_items(self, items):
        self._purchased.update(set(items) & self._needed)
        self._needed.difference_update(self._purchased)


mynewlist: List[str] = ShoppingList2(
    ["grapes", "beets", "apples", "milk", "melon", "coffee"]
)
mynewlist.mark_purchased_items(["grapes", "beets", "milk"])

print("My new wish list: ", mynewlist)

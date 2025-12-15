# Ejemplos de clases y métodos

class ShoppingList:
    def __init__(self, items):
        """ Parameters
            ----------
            items : Union[str, Iterable[str]]
                Iterable of item-names to add to shopping list"""
        if isinstance(items, str):
            items = [items]
        self._needed = set(items)
        self._purchased = set()

    def add_new_items(self, items):
        """ Add more items to the shopping list

            Parameters
            ----------
            items : Union[str, Iterable[str]]
                Iterable of item-names to add to shopping list"""
        if isinstance(items, str):
            items = [items]
        # set.update adds elements of an iterable to a set
        self._needed.update(items)

    def mark_purchased_items(self, items):
        """ Provide names of items to mark as 'purchased'

            Parameters
            ----------
            items : Union[str, Iterable[str]]"""
        if isinstance(items, str):
            items = [items]
        # only mark items as purchased that are on our list to begin with
        self._purchased.update(set(items) & self._needed)
        # remove all purchased items from our unpurchased set
        self._needed.difference_update(self._purchased)

    def list_purchased_items(self):
        """ Return a sorted list of the items that have been purchased"""
        return sorted(self._purchased)

    def list_unpurchased_items(self):
        """ Return a sorted list of the items still on the list"""
        return sorted(self._needed)

my_list = ShoppingList(["apples", "apples", "grapes", "peaches", "milk", "bread", "pineapples"])
print("Items sin comprar: ",my_list.list_unpurchased_items())

my_list.mark_purchased_items(["grapes", "pineapples"])
print("Items comprados: ",my_list.list_purchased_items())

print("Sin comprar todavía: ",my_list.list_unpurchased_items())

def strike(text):
    """ Renders string with strike-through characters through it.

        `strike('hello world')` -> '̶h̶e̶l̶l̶o̶ ̶w̶o̶r̶l̶d'

        Notes
        -----
        \u0336 is a special strike-through unicode character; it
        is not unique to Python."""
    return ''.join('\u0336{}'.format(c) for c in text)

print("="*50)

"""
Aparte del constructor __init__ existen muchos más como:
* __repr__(self)
* __str__(self)

La documentación de los constructores la podemos ver en:
https://www.pythonlikeyoumeanit.com/Module4_OOP/Special_Methods.html
"""
class ShoppingList2:
    def __init__(self, items):
        self._needed = set(items)
        self._purchased = set()

    def __repr__(self):
        """ Returns formatted shopping list as a string with
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

mynewlist = ShoppingList2(["grapes", "beets", "apples", "milk", "melon", "coffee"])
mynewlist.mark_purchased_items(["grapes", "beets", "milk"])

print(mynewlist)
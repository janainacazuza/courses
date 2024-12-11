from modelos.menu.menu_item import MenuItem

class Drinks:
    """ Drinks class. """
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def __str__(self):
        """ Return a string representation of the object. """
        return self._name
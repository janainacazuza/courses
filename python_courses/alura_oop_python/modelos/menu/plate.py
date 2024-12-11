from modelos.menu.menu_item import MenuItem

class Plate(MenuItem):
    """ Plate class. """
    def __init__(self, name, price, description):
        super().__init__(name, price)
        self.description = description

    def __str__(self):
        """ Return a string representation of the object. """
        return self._name
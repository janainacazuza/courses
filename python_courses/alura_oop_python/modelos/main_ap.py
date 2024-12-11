from restaurant import Restaurant
from modelos.menu.drinks import Drinks
from modelos.menu.plate import Plate

restaurant_praca = Restaurant('Praça', 'Gourmet')
drink_juice = Drinks('Suco de Melancia', 5.0, 'big')
plate_bread = Plate('Little bread', 2.0, ' The best bread')
restaurant_praca.add_menu(drink_juice)
restaurant_praca.add_menu(plate_bread)


restaurant_praca.restaurant_status()

def main():
    """Main function."""
    print(drink_juice)
    print(plate_bread)

if __name__ == '__main__':
    main()
from abc import ABCMeta, abstractmethod


class UnsupportedOperationException(Exception):
    pass


class MenuComponent(metaclass=ABCMeta):

    def add(self, menu_component):
        raise UnsupportedOperationException

    def remove(self, menu_component):
        raise UnsupportedOperationException

    def get_child(self, i):
        raise UnsupportedOperationException

    def get_name(self):
        raise UnsupportedOperationException

    def get_desc(self):
        raise UnsupportedOperationException

    def is_vegetarian(self):
        raise UnsupportedOperationException

    @abstractmethod
    def print(self):
        raise UnsupportedOperationException


class MenuItem(MenuComponent):
    def __init__(self, name, description, vegetarian, price):
        self.description = description
        self.name = name
        self.price = price
        self.vegetarian = vegetarian

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_price(self):
        return self.price

    def is_vegetarian(self):
        return self.vegetarian

    def print(self):
        print(' {}'.format(self.get_name()))
        if self.is_vegetarian():
            print('(V)')
        print(" {}".format(self.get_price()))
        print(" {}".format(self.get_description()))


class Menu(MenuComponent):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.menu_components = []

    def add(self, menu_component):
        self.menu_components.append(menu_component)

    def remove(self, menu_component):
        self.menu_components.remove(menu_component)

    def get_child(self, i):
        return self.menu_components[i]

    def get_name(self):
        return self.name

    def get_desc(self):
        return self.description

    def print(self):
        print("""
{},
{}
_______________""".format(self.get_name(), self.get_desc()))
        for i in self:
            i.print()

    def __iter__(self):
        return CompositeIterator(self)


class CompositeIterator:
    def __init__(self, menu):
        self.stack = []
        self.state = 0
        self.menu = menu.menu_components
        self.stack.append(menu)

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.menu) == self.state:
            raise StopIteration
        else:
            result = self.menu[self.state]
            self.state += 1
            return result


class Waitress:
    def __init__(self, all_menus):
        self.all_menus = all_menus

    def print_menu(self):
        self.all_menus.print()

    def print_vegetarian(self):
        for x in self.all_menus:
            for i in x:
                if i.is_vegetarian():
                    i.print()

def main():
    pancake_menu = Menu(name='Pancake house menu', description='Breakfast')
    diner_menu = Menu(name='Diner menu', description='Lunch')
    cafe_menu = Menu(name='Cafe menu', description='Dinner')
    dessert_menu = Menu(name='Dessert menu', description='Dessert of course!')

    all_menus = Menu(name='All menus', description='All menu combined')
    all_menus.add(pancake_menu)
    all_menus.add(diner_menu)
    all_menus.add(cafe_menu)
    all_menus.add(dessert_menu)

    pancake_menu.add(MenuItem("K&B Pancakke Breakfast", "Panckakes with scrambled eggs", True, 2.99))
    pancake_menu.add(MenuItem("Regular Pancakke Breakfast", "Panckakes with frieds eggs", False, 2.99))
    pancake_menu.add(MenuItem("Blueberry Pancakkes", "Pancakkes made with fresh blueberries", False, 3.49))
    pancake_menu.add(MenuItem("Waffles", "Waffles, with your choice of blueberries or strawberries", True, 3.59))

    diner_menu.add(MenuItem("Vegetarian BLT", "Bacon with lettuce & tomato", True, 2.99))
    diner_menu.add(MenuItem("BLT", "Bacon with lettuce on whole wheat", False, 2.99))
    diner_menu.add(MenuItem("HotDog", "A hotdog with saurkraut, relich, onions & ect", False, 3.05))
    diner_menu.add(MenuItem("Soup of the day", "Soup of the day, with a side of potato salad", False, 3.29))

    cafe_menu.add(MenuItem('Veggy burder add air Fries', "Veggie burger on a whole wheat bun", True, 3.99))
    cafe_menu.add(MenuItem('Soup of the day', 'A cup of the coup of the day', False, 3.69))
    cafe_menu.add(MenuItem('Burrito', 'A large burrito, with whole pinto beans', False, 4.29))

    dessert_menu.add(MenuItem('Apple pie', 'Apple pie with a flakey crust', True, 1.59))
    dessert_menu.add(MenuItem('Cheesecake', 'Creamy New York cheesecake', True, 1.99))
    dessert_menu.add(MenuItem('Sorbet', 'A scoop of raspberry and a scoop of lime', True, 1.90))

    waitress = Waitress(all_menus)
    # waitress.print_menu()
    waitress.print_vegetarian()

if __name__ == "__main__":
    main()

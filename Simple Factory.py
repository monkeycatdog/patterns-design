class PizzaStore:
    """основной абстрактный класс фабрика, принимает тип пиццы и создает ее. 
реализация метода создания определяется самостоятельно наследникми."""
    def order_pizza(self, type):
        pizza = self._createPizza(type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza

    def _createPizza(self):
        pass


class Pizza:
    "Класс пица это абстрактный класс, принимающий фабрику для создания ингридиентов к пицце"
    def __init__(self, factory):
        self._factory = factory
        self._name = None
        self._dough = None
        self._sauce = None
        self._cheese = None
        self._toppings = []

    def prepare(self):
        print('Preparing '+self._name)
        self._dough = self._factory.create_dough(self)
        self._sauce = self._factory.create_sauce(self)
        self._cheese = self._factory.create_cheese(self)
        print('Ingridients: \n{},\n{},\n{}'.format(self._dough, self._sauce, self._cheese))
        for i in self._toppings:
            print('*'+i)

    def bake(self):
        print('Bake for 25 minutes at 350')

    def cut(self):
        print('Cutting the pizza into diagonal slices')

    def box(self):
        print('Place pizza in officical PizzaStore box')

    @property
    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name


class PizzaIngredientFactory:
    def create_dough(self):
        pass

    def create_sauce(self):
        pass

    def create_cheese(self):
        pass

    def create_veggies(self):
        pass

    def create_peperoni(self):
        pass

    def create_clam(self):
        pass


class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self):
        return 'Thin Crust Dough'

    def create_sauce(self):
        return 'Marinara sauce'

    def create_cheese(self):
        return 'Reggiano Cheese'


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self):
        return 'Extra Thick Crust Dough'

    def create_sauce(self):
        return 'Plum Tomato sauce'

    def create_cheese(self):
        return 'Reggiano Cheese'




class NYStyleCheesePizza(Pizza):
    def __init__(self, factory):
        super().__init__(factory)
        self._toppings.append('Shredded Mozzarella Cheese')


class ChicagoStyleCheesePizza(Pizza):
    def __init__(self, factory):
        super().__init__(factory)
        self._toppings.append('Fucking hell cheese')

    def cut(self):
        print('Cutting the pizza into square slices')


class NYPizzaStore(PizzaStore):
    def _createPizza(self, item):
        if item == "cheese":
            pizza = NYStyleCheesePizza(NYPizzaIngredientFactory)
            pizza.setName('New York Style Cheese Pizza')
        else:
            return None
        return pizza


class ChicagoPizzaStore(PizzaStore):
    """Фабричный метод, реализует от полученного типа нужный экземпляр класса пиццы, 
    который принимает в свою очередь фабрику"""
    def _createPizza(self, item):
        if item == 'cheese':
            pizza = ChicagoStyleCheesePizza(ChicagoPizzaIngredientFactory)
            pizza.setName('Chicago Style Cheese Pizza')
        else:
            return None

        return pizza


def main():
    ny_store = NYPizzaStore()
    chicaho_store = ChicagoPizzaStore()

    pizza = ny_store.order_pizza('cheese')
    print('Ordered: ' + pizza.getName + '\n')

    pizza = chicaho_store.order_pizza('cheese')
    print('Ordered: '+ pizza.getName + '\n')

if __name__ == '__main__':
    main()

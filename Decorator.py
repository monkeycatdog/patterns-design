class Beverage:
    # Создание родительского класса для всех видов кофе
    def __init__(self, description, price):
        self._description = description
        self._price = price

    def get_description(self):
        return self._description

    def coast(self):
        return self._price


class CondimentDecorator(Beverage):
    # Топинги к кофе. Наследуются, имеют такие же методы и свойства как и у родительского
    # Однако методы расширены вызывающими аналоигчными методами у декорируемого объекта
    def __init__(self, beverage, description, price):
        self._beverage = beverage
        super().__init__(description, price)

    def get_description(self):
        return self._beverage.get_description() + ", {}".format(self._description)

    def coast(self):
        return self._price + self._beverage.coast()


def main():
    beverage_1 = Beverage('Espresso', 1.9)
    beverage_2 = Beverage('House Dark', 2.3)
    print(str(beverage_1.get_description()) + ': $' + str(beverage_1.coast()))

    beverage_1 = CondimentDecorator(beverage_1, 'Mocha', 0.2)
    beverage_1 = CondimentDecorator(beverage_1, 'Whip', 0.1)

    print(str(beverage_1.get_description()) + ': $' + str(beverage_1.coast()))
    print()
    print(str(beverage_2.get_description()) + ': $' + str(beverage_2.coast()))
    beverage_2 = CondimentDecorator(beverage_2, 'Mocha', 0.2)
    beverage_2 = CondimentDecorator(beverage_2, 'Soy', 0.1)
    beverage_2 = CondimentDecorator(beverage_2, 'Mocha', 0.2)
    print(str(beverage_2.get_description()) + ': $' + str(beverage_2.coast()))


if __name__ == '__main__':
    main()

class Duck:
    """Абстрактный класс утки"""

    def __init__(self):
        # интерфейс абстрактного класса
        # инкапсулированные методы
        self._flyBehavior = None
        self._quackBehavior = None

        # для каждой реализация одинаковое использованеи (полиморфизм)

    def performFly(self):
        self._flyBehavior.fly()

    def performQuack(self):
        # инкапсулированный метод кряка
        self._quackBehavior.quack()

    def set_flyBehavior(self, model):
        self._flyBehavior = model

    def set_quackBehavior(self, model):
        self._quackBehavior = model


class FlyRocket:
    """конкретная реализация полета"""

    def fly(self):
        print("Iam flying!!!")


class Quack:
    """конкретная реализация кряка"""

    def quack(self):
        print("quack!!!")


firstDuck = Duck()
first_quack = Quack()
first_fly = FlyRocket()

firstDuck.set_flyBehavior(first_fly)
firstDuck.set_quackBehavior(first_quack)

firstDuck.performFly()
firstDuck.performQuack()


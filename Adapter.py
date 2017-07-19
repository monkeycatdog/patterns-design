# Паттерн Адаптер - преобразует интерфейс класса к другому интерфейсу, на который расчитан клиент
# Обеспечивает совместимую работу классов, невозможную в обычных условиях изза не совместимых
# интерфейсов.


class Oldclass:
    def __init__(self):
        pass

    def old_method(self):
        print('Hello from old class')


class Interface:
    def __init__(self):
        pass

    def method(self):
        pass


# наследуем старый класс, и новый интерфейс
class Adapter(Interface, Oldclass):
    pass

adapter = Adapter()

adapter.old_method()

# class Adaptee:
#     def __init__(self):
#         pass
#
#     def specificInterface(self):
#         print('Hello from specific interface')
#
#
# class Interface:
#     def __init__(self):
#         pass
#
#     def request(self):
#         pass
#
#
# class Adapter(Interface):
#     def __init__(self, old):
#         super().__init__()
#         self._old_class = old
#
#     def request(self):
#         self._old_class.specificInterface()
#
# old = Adaptee()
# adapter_old = Adapter(old)
#
# adapter_old.request()

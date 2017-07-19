#exemple 1
def singleton(cls):
    instance = {}

    def get_instance():
        if cls is not instance:
            instance[cls] = cls

        return instance[cls]

    return get_instance


@singleton
class MyClass:
    pass


a = MyClass()

b = MyClass()

print(a == b)


#exemple 2

class Singleton:
    instance = None

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def get_instance(cls, name, price):
        if cls.instance is not None:
            return cls.instance

        cls.instance = cls(name, price)
        return cls.instance

    def get_info(self):
        print(type(self).__name__ + '\n')
        for i in self.__dict__:
            print(str(i) + ': ' + str(self.__dict__[i]))



single = Singleton.get_instance('Hello', 200)
single.get_info()

single2 = Singleton.get_instance('Hello', 200)
single2.get_info()

print(single == single2)


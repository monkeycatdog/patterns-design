from abc import ABCMeta, abstractmethod


class CaffeineBeverage(metaclass=ABCMeta):
    """
        abstract class for tea and coffee
    """

    def __init__(self):
        pass

    def prepareRecipe(self):
        self.boilWater()
        self.brew()
        self.pourInCup()
        if self.customersWantsCondiments():
            self.addCondiments()
        print('Coffee done!')

    def boilWater(self):
        print('Boiling water')

    @abstractmethod
    def brew(self):
        pass

    def pourInCup(self):
        print('Pouring into Cup')

    @abstractmethod
    def addCondiments(self):
        pass

    @abstractmethod
    def customersWantsCondiments(self):
        pass


class CoffeeWithHook(CaffeineBeverage):
    def brew(self):
        print('Dripping coffee through filter')

    def addCondiments(self):
        print('Adding Sugar and Milk')

    def customersWantsCondiments(self):
        answer = self.__get_user_input()

        if answer.lower() == 'y' or answer.lower() == 'yes':
            return True
        else:
            return False

    def __get_user_input(self):
        try:
            question = input('Would you like milk and sugar with your coffee? y/n')
        except:
            return 'no'

        return question


coffee = CoffeeWithHook()
coffee.prepareRecipe()






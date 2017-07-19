from abc import ABCMeta, abstractmethod

class State(metaclass=ABCMeta):
    def __init__(self, gumball_machine):
        self.gumball_machine = gumball_machine

    @abstractmethod
    def insert_quarter(self):
        pass

    @abstractmethod
    def eject_quarter(self):
        pass

    @abstractmethod
    def turn_crank(self):
        pass

    @abstractmethod
    def dispense(self):
        pass


class GumballMachine:
    def __init__(self, num):
        self.sold_out_state = SoldOutState(self)
        self.no_quarter_state = NoQuarterState(self)
        self.has_quarter_state = HasQuarterState(self)
        self.sold_state = SoldState(self)
        self.count = num
        self.state = self.sold_out_state
        if self.count > 0:
            self.state = self.no_quarter_state

    def insert_quarter(self):
        self.state.insert_quarter()

    def eject_quarter(self):
        self.state.eject_quarter()

    def turn_crank(self):
        self.state.turn_crank()
        self.state.dispense()

    def set_state(self, state):
        self.state = state

    def release_ball(self):
        print('A gumball comes rolling out the slot..')
        if self.count != 0:
            self.count -= 1

    def get_count(self):
        return self.count

    def get_has_quarter_state(self):
        return self.has_quarter_state

    def get_no_qurater_state(self):
        return self.no_quarter_state

    def get_sold_state(self):
        return self.sold_state

    def get_sold_out_state(self):
        return self.sold_out_state

    def __str__(self):
        return """Mighty Gumball, Inc\nInventory: {}\nState:  {}""".format(self.count, self.state)


class NoQuarterState(State):

    def insert_quarter(self):
        print('You inserted a quater')
        self.gumball_machine.set_state(self.gumball_machine.get_has_quarter_state())

    def eject_quarter(self):
        print('You havent inserted a quater')

    def turn_crank(self):
        print('You turned, but theres no quater')

    def dispense(self):
        print('You need to pay first')

    def __str__(self):
        return 'No quarter'


class HasQuarterState(State):
    def insert_quarter(self):
        print('You cant insert another quarter')

    def eject_quarter(self):
        print('Quarter returned')
        self.gumball_machine.set_state(self.gumball_machine.get_no_qurater_state())

    def turn_crank(self):
        print('You turned..')
        self.gumball_machine.set_state(self.gumball_machine.get_sold_state())

    def dispense(self):
        print('No gumball dispensed')

    def __str__(self):
        return 'Has quarter'


class SoldState(State):
    def insert_quarter(self):
        print('Please wait, were allready giving you a gumball')

    def eject_quarter(self):
        print('Sorry, you already turned the crank')

    def turn_crank(self):
        print('Turning twice doesnt get you another gumball')

    def dispense(self):
        self.gumball_machine.release_ball()
        if self.gumball_machine.get_count() > 0:
            self.gumball_machine.set_state(self.gumball_machine.get_no_qurater_state())
        else:
            print('Oops, out of gumballs!')
            self.gumball_machine.set_state(self.gumball_machine.get_sold_state())

    def __str__(self):
        return 'Sold'


class SoldOutState(State):
    def insert_quarter(self):
        print('You cant insert a quarter, the machine is sold out')

    def eject_quarter(self):
        print('You cant eject you havent inserted a quarter yet')

    def turn_crank(self):
        print('You turned, but there are no gumballs')

    def dispense(self):
        print('No gumball dispensed')

    def __str__(self):
        return 'sold out'


if __name__ == '__main__':
    gumball = GumballMachine(5)
    print(gumball)
    print()
    gumball.insert_quarter()
    gumball.turn_crank()
    print()
    print(gumball)
    gumball.insert_quarter()
    gumball.eject_quarter()
    print()
    print(gumball)
    print()
    gumball.turn_crank()
    gumball.insert_quarter()
    gumball.insert_quarter()
    print()
    print(gumball)
    gumball.eject_quarter()
    gumball.turn_crank()
    gumball.insert_quarter()
    gumball.turn_crank()
    print()
    print(gumball)

class Subject:
    def __init__(self):
        self._observers = []
        self.info_data = 'Hello, my subscribers'

    def register_observer(self, obj):
        self._observers.append(obj)

    def remove_observer(self, obj):
        self._observers.remove(obj)

    def notify_observers(self):
        for x in self._observers:
            x.update(self, self.info_data)

    def set_info_data(self, data):
        self.info_data = data
        self.notify_observers()

        # def __repr__(self):
        #     info = "class {}, \nData: {}\n".format(type(self).__name__, self.info_data)
        #     state = '\n'.join(map(str, self._observers)) or 'Empty'
        #     print(info + state)


class Observer:
    def __init__(self):
        self._data = None
        self._interface = None
        self._observable = []

    def update(self, obs, data):
        if obs in self._observable:
            self._data = data
            self.display()

    def display(self):
        self._interface.display(self._data)

    def set_inteface(self, method):
        self._interface = method

    def set_observable(self, obs):
        self._observable.append(obs)

        # def __repr__(self):
        #   info = "class {}, \nData: {}\n Interface: {}".format(type(self).__name__, self._data, self._interface)
        #   print(info)


class Interface_observer:
    def display(self, data):
        print(data)

        # def __repr__(self):
        #   info = "class {} \n".format(type(self).__name__)
        #   print(info)


subject = Subject()

obs_1 = Observer()
obs_2 = Observer()
obs_3 = Observer()

interface = Interface_observer()

obs_1.set_inteface(interface)
obs_2.set_inteface(interface)
obs_3.set_inteface(interface)

obs_1.set_observable(subject)
obs_2.set_observable(subject)
obs_3.set_observable(subject)

subject.register_observer(obs_1)
subject.register_observer(obs_2)
subject.register_observer(obs_3)

subject.notify_observers()




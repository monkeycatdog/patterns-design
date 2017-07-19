class Interface:
    def request(self):
        pass


class RealSubject(Interface):
    def __init__(self, data):
        self.__data = data

    def request(self):
        return self.__data


class Proxy(Interface):
    def __init__(self):
        # self.__real_subject = real_subject
        self.Inst = RealSubject
        self.__real_subject = None

    def request(self):
        if self.__real_subject is None:
            self.__real_subject = self.Inst('Hello')

        return self.__real_subject.request()


if __name__ == '__main__':
    # real = RealSubject('Hello world')

    proxy = Proxy()

    print(proxy.request())

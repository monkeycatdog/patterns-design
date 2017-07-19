# Паттерн Фасад представляет унивифицированный интерфейс к группе интерфейсов
# подсистемы. Фасад определяет высокоуровневый интерфейс, упрощает работу с подсистемой.

class HomeCinemaFacade:
    def __init__(self, amp, tuner, dvd):
        self.amp = amp
        self.tuner = tuner
        self.dvd = dvd

    def watch_move(self):
        print('Start watching move!')
        self.amp.on()
        self.tuner.on()
        self.dvd.on()

    def end_move(self):
        print('Move in the End!')
        self.amp.off()
        self.tuner.off()
        self.dvd.off()


class Amp:
    def __init__(self):
        pass

    def on(self):
        print('Amp on!')

    def off(self):
        print('Amp off!')


class Tuner:
    def __init__(self):
        pass

    def on(self):
        print('Tuner on!')

    def off(self):
        print('Tuner off!')


class Dvd:
    def __init__(self):
        pass

    def on(self):
        print('Dvd on!')

    def off(self):
        print('Dvd off!')


amp = Amp()
tuner = Tuner()
dvd = Dvd()

home_cinema = HomeCinemaFacade(amp, tuner, dvd)

home_cinema.watch_move()
print()
home_cinema.end_move()
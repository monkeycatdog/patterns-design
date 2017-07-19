class RemoteControl:
    count = 7
    def __init__(self, noComand=None):
        self._onComands = list(i for i in range(7))
        self._offComands = list(i for i in range(7))
        self._noComand = noComand

        for i in range(7):
            self._offComands[i] = self._noComand
            self._onComands[i] = self._noComand

    def set_comand(self, slot, onComand, offComand):
        self._onComands[slot] = onComand
        self._offComands[slot] = offComand

    def on_button_was_pushed(self, slot):
        if not self._onComands[slot] is None:
            self._onComands[slot].execute()

    def off_button_was_pushed(self, slot):
        if not self._offComands[slot] is None:
            self._offComands[slot].execute()

    def __str__(self):
        s1 = "\n-----------------REMOTE CONTROL-----------------\n"
        for i in range(7):
            s2 = '[slot {}] {}\t'.format(i, type(self._onComands[i]).__name__)
            s3 = '[slot {}] {}\n'.format(i, type(self._offComands[i]).__name__)
            s1 += s2 + s3
        return s1

#abstract
class Command:
    def __init__(self, parent=None):
        self._command = parent

    def execute(self):
        pass

    def undo(self):
        pass


class NoCommand(Command):
    def execute(self):
        pass


class LigthOnCommand(Command):
    def execute(self):
        self._command.on()


class LigthOffCommand(Command):
    def execute(self):
        self._command.off()


class Ligth:
    def __init__(self, place):
        self._place = place

    def on(self):
        print('{} light is on'.format(self._place))

    def off(self):
        print('{} light is off'.format(self._place))


def main():
    no_command = NoCommand()
    remote_test = RemoteControl(no_command)

    living_on_room = Ligth('Living Room')
    ligth_on_command = LigthOnCommand(living_on_room)
    ligth_off_command = LigthOffCommand(living_on_room)

    remote_test.set_comand(0, ligth_on_command, ligth_off_command)

    print(remote_test)

    remote_test.on_button_was_pushed(0)
    remote_test.off_button_was_pushed(0)


if __name__ == '__main__':
    main()
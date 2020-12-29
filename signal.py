import sys
from PyQt5 import QtCore as qtc
from PyQt5 import QtWidgets as qtw
"""
Signal/Slot overloading alternate version
"""


class Bogus:
    """
    Example object
    """

    def __init__(self, msg):
        self.msg = msg

    def speak(self):
        print(f'I am gonna say "{self.msg}"')


class Controller(qtw.QWidget):
    """
    Just a single signal definition to object seems to work
    """
    trigger = qtc.pyqtSignal(object)

    def __init__(self):
        super().__init__()
        # only a single connect
        self.trigger.connect(self.slot)

    # Then decorate the single with each type to be passed
    @qtc.pyqtSlot(type(None))
    @qtc.pyqtSlot(str)
    @qtc.pyqtSlot(object)
    def slot(self, whatever=None):
        # multiplex dependent on parameter passes
        if isinstance(whatever, type(None)):
            print('No object passed')
        elif isinstance(whatever, str):
            print(f'A string "{whatever}" was passed')
        elif isinstance(whatever, object):
            print('An object was passes, use speak() method')
            whatever.speak()
        else:
            print('Error, I have no idea what was passed')


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)

    c = Controller()
    o = Bogus('I am Bogus')

    # This method advantage a single emit command
    print('First with object')
    c.trigger.emit(o)

    print('Next with a string')
    c.trigger.emit('Hello World!')

    print('Last without object')
    c.trigger.emit(None)

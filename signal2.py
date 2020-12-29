import sys
from PyQt5 import QtCore as qtc
from PyQt5 import QtWidgets as qtw
"""
Signal/Slot overloading referencing
Mastering GUI Programming with Python
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
    Following will throw error and will not work:
    trigger = qtc.pyqtSignal([type(None)], [str], [object])

    type None seems to have to be last or even absent! 
    """
    trigger = qtc.pyqtSignal([str], [object], [type(None)])

    def __init__(self):
        super().__init__()
        # order of the triggers assignment does not seem to matter
        self.trigger[type(None)].connect(self.none_slot)
        self.trigger[str].connect(self.string_slot)
        self.trigger[object].connect(self.object_slot)

    @qtc.pyqtSlot()
    def none_slot(self):
        print('No object passed to none_slot')

    @qtc.pyqtSlot(str)
    def string_slot(self, a_string):
        print(f'A string "{a_string}" was passed')
    """
    This slot must filter out nulls so above none_slot will fire
    because this will fire regardless if object or None is passed 
    """
    @qtc.pyqtSlot(object)
    def object_slot(self, an_object=None):
        if an_object != None:
            an_object.speak()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)

    c = Controller()
    o = Bogus('I am Bogus')

    # This method requires matching emit index to signal index.
    print('First Bogus object')
    c.trigger[object].emit(o)

    print('Next with a string')
    c.trigger[str].emit('Hello World!')

    print('Last without object')
    c.trigger[type(None)].emit(None)

import abc
from PyQt5.QtWidgets import QWidget, QMainWindow


class AbcPlugin(QWidget):

    def __init__(self, parent: QMainWindow, settings):
        super().__init__()
        self.parent = parent
        self.settings = settings
        self.RESOURCES_DIR = settings.RESOURCES_DIR
        self.init_view()
        self.init_handlers()

    @abc.abstractmethod
    def init_view(self):
        pass

    @abc.abstractmethod
    def init_handlers(self):
        pass

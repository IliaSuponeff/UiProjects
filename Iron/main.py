import sys
from main_ui import Ui
from settings import Settings
from PyQt5.QtWidgets import QApplication


class Iron:

    def __init__(self, debug=True):
        self.settings = Settings(debug)
        self.ui = Ui(self.settings)

    def execute(self):
        self.ui.show()


def main(*args, **kwargs):
    app = QApplication(list(args))
    iron = Iron(*args)
    iron.execute()
    sys.exit(app.exec())


if __name__ == '__main__':
    main(*sys.argv)

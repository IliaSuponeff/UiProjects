import random
import sys

from ui import Ui_MainWindow
from PySide6.QtWidgets import *


class PassGen(QMainWindow):
    _STANDART_SYMBOLS = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    _SPECIAL_SYMBOLS_1 = "_!-+=/|\\?"
    _SPECIAL_SYMBOLS_2 = "@#$%&<>*?"

    def __init__(self):
        super().__init__(None)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._build()

    def _build(self):
        # set length values
        self.ui.combo_box.addItems([str(_len) for _len in range(4, 33)])
        self.ui.pushButton.clicked.connect(self.generate)

    def generate(self):
        length = int(self.ui.combo_box.currentText())
        result = ""
        while len(result) != length:
            probability = random.random()
            if 0 <= probability <= 0.5:
                symbol = random.choice(self._STANDART_SYMBOLS)
            elif self.is_checked(self.ui.simbols_1_box) and 0.5 < probability <= 0.75:
                symbol = random.choice(self._SPECIAL_SYMBOLS_1)
            elif self.is_checked(self.ui.simbols_2_box) and 0.75 < probability <= 1:
                symbol = random.choice(self._SPECIAL_SYMBOLS_2)
            else:
                symbol = ''
            result += symbol

        self.ui.lineEdit.clear()
        self.ui.lineEdit.setText(result)

    @staticmethod
    def is_checked(box):
        return str(box.checkState()) == "CheckState.Checked"


if __name__ == '__main__':
    app = QApplication()
    window = PassGen()
    window.show()
    sys.exit(app.exec())

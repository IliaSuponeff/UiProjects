import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from calc_ui import Ui_MainWindow


class Calculator(QMainWindow):

    def __init__(self, ):
        super().__init__(None)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.history_data = []
        self._add_digits_button()
        self._set_clear_functions()
        self._set_math_operations()
        self._others()
        self.setWindowTitle("Calculator")

    def _others(self):
        self.ui.clear_history.clicked.connect(self._clear_history)

    def _update_history(self, data):
        data = data.split("=")
        data = f"{data[0]}=\n{data[1]}"
        if self._is_full_history():
            self.history_data.pop(0)

        self.history_data.append(data)
        self.ui.history_label.clear()
        result = ""
        for data in self.history_data:
            result = f'{result}\n\n{data}'
        self.ui.history_label.setText(result)

    def _clear_history(self):
        self.history_data = []
        self.ui.history_label.clear()

    def _is_full_history(self):
        return len(self.history_data) == 5

    def _set_math_operations(self):
        self.ui.btn_add.clicked.connect(lambda: self._set_math_sign("+"))
        self.ui.btn_sub.clicked.connect(lambda: self._set_math_sign("-"))
        self.ui.btn_div.clicked.connect(lambda: self._set_math_sign("/"))
        self.ui.btn_mult.clicked.connect(lambda: self._set_math_sign("*"))
        self.ui.btn_eq.clicked.connect(self._equal)
        self.ui.btn_invert.clicked.connect(self._invert)

    def _invert(self):
        text = self.ui.calc_edit.text()
        if text[0] == '-':
            text = text[1:]
        elif text != '0':
            text = f'-{text}'
            if '=' in self.ui.temp_label.text():
                self.ui.temp_label.clear()
        self._clear_entry()
        self._update_entry_value(text)

    def _equal(self):
        text = self.ui.calc_edit.text()
        temp = self.ui.temp_label.text()
        if '=' in temp:
            temp = ''
        temp = f'{temp}{text}'
        try:
            value = f"{eval(temp)}"
        except:
            value = "Ошибка"

        self._clear_all()
        self.ui.temp_label.setText(f"{temp}={value}")
        if value != 'Ошибка':
            self._update_entry_value(value)
        self._update_history(f"{temp}={value}")

    def _set_math_sign(self, math_sign: str):
        text = self.ui.calc_edit.text()
        temp = self.ui.temp_label.text()
        if '=' in temp:
            temp = f'{text}{math_sign}'
        else:
            temp = f'{temp}{text}{math_sign}'
        self.ui.temp_label.clear()
        self.ui.temp_label.setText(temp)
        self._clear_entry()

    def _set_clear_functions(self):
        self.ui.btn_clear_entry.clicked.connect(self._clear_entry)
        self.ui.btn_clear_all.clicked.connect(self._clear_all)
        self.ui.btn_del.clicked.connect(self._backspace)

    def _clear_entry(self):
        self.ui.calc_edit.clear()
        self._update_entry_value("0")

    def _clear_all(self):
        self._clear_entry()
        self.ui.temp_label.clear()

    def _backspace(self):
        text = self.ui.calc_edit.text()
        print(text, text[:-1])
        if len(text[:-1]) == 0:
            self._update_entry_value("0")
        else:
            self._update_entry_value(text[:-1])

    def _add_digits_button(self):
        self.ui.btn_0.clicked.connect(lambda: self._add_digit(0))
        self.ui.btn_1.clicked.connect(lambda: self._add_digit(1))
        self.ui.btn_2.clicked.connect(lambda: self._add_digit(2))
        self.ui.btn_3.clicked.connect(lambda: self._add_digit(3))
        self.ui.btn_4.clicked.connect(lambda: self._add_digit(4))
        self.ui.btn_5.clicked.connect(lambda: self._add_digit(5))
        self.ui.btn_6.clicked.connect(lambda: self._add_digit(6))
        self.ui.btn_7.clicked.connect(lambda: self._add_digit(7))
        self.ui.btn_8.clicked.connect(lambda: self._add_digit(8))
        self.ui.btn_9.clicked.connect(lambda: self._add_digit(9))
        self.ui.btn_dot.clicked.connect(self._add_dot)

    def _add_dot(self):
        text = self.ui.calc_edit.text()
        if '.' not in text:
            self._update_entry_value(text + '.')

    def _add_digit(self, digit: int):
        text = self.ui.calc_edit.text()
        if text == '0':
            self._update_entry_value(str(digit))
        else:
            self._update_entry_value(text + str(digit))

    def _update_entry_value(self, value):
        if len(value) > 16:
            self.ui.calc_edit.setText(value[:16])
        else:
            self.ui.calc_edit.setText(value)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('./icons/icon.png'))
    win = Calculator()
    win.show()
    sys.exit(app.exec())
import datetime
import logging
from PySide6.QtWidgets import QDialog
import app_db
from app_db import DataBase, Account
from PySide6.QtGui import QIcon
from .exception_dialogs import ExceptionDialog
from ui import add_balance_dialog_ui, add_trans_dialog_ui, date_choose_dialog_ui
from .choose_dialogs import ChooseDateDialog




class AddAccountDialog(QDialog):

    def __init__(self, db: DataBase, currencies: list[str], callback=None):
        super().__init__()
        self.ui = add_balance_dialog_ui.Ui_Dialog()
        self.db = db
        self.ui.setupUi(self)
        self.ui.create_btn.clicked.connect(self.add_account)
        self.ui.currency_box.addItems(currencies)
        self.callback = callback
        icon = QIcon()
        icon.addFile('./images/app_icon.png')
        self.setWindowIcon(icon)

    def add_account(self):
        try:
            name = self.ui.name_le.text()
            if name == '':
                raise Exception("Name field is empty.")
            currency = self.ui.currency_box.currentText()
            self.db.add_account(name, "0", currency)
            if self.callback:
                self.callback()
            self.close()
        except FileNotFoundError as ex:
            self.tell_about_exception(ex)
        except AssertionError as ex:
            self.tell_about_exception(ex)
        except Exception as ex:
            self.tell_about_exception('Проверьте введённые значения в полях.\n'
                                      'Поле имени счёта не должно быть пустое.\n'
                                      'Поле стартового баланса должно быть целым или дробным числом.')

    @staticmethod
    def tell_about_exception(msg: str):
        e = ExceptionDialog('Ошибка', msg)
        e.show()
        e.exec()


class AddTransactionDialog(QDialog):

    def __init__(self, account: Account, db: DataBase, callback=None):
        super().__init__()
        self.ui = add_trans_dialog_ui.Ui_Dialog()
        self.db = db
        self.ui.setupUi(self)
        self.account = account
        self.date = app_db.get_time_now()
        self.ui.create_btn.clicked.connect(self.add_transaction)
        self.ui.date_choose_btn.clicked.connect(self.choose_date)
        self.callback = callback
        icon = QIcon()
        icon.addFile('./images/app_icon.png')
        self.setWindowIcon(icon)

    def choose_date(self):
        e = ChooseDateDialog()
        e.show()
        e.exec()
        self.date = e.date

    def add_transaction(self):
        try:
            info = self.ui.info_le.toPlainText()
            summary = float(self.ui.sum_le.text().replace(',', '.'))
            self.db.add_transactions(self.account, summary, info, self.date)
            if self.callback:
                self.callback()
            self.close()
        except FileNotFoundError as ex:
            self.tell_about_exception(ex)
        except Exception as ex:
            logging.exception(ex)
            self.tell_about_exception('Проверьте введённые значения в полях.\n'
                                      'Поле суммы не должно быть пустое и сожержать числа')

    @staticmethod
    def tell_about_exception(msg: str):
        e = ExceptionDialog('Ошибка', msg)
        e.show()
        e.exec()

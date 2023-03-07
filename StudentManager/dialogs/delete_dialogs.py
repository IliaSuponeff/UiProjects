from PySide6.QtWidgets import QDialog
from app_db import DataBase
from .exception_dialogs import ExceptionDialog
from ui import del_balance_dialog_ui
from PySide6.QtGui import QIcon


class DelAccountDialog(QDialog):

    def __init__(self, db: DataBase, callback=None):
        super().__init__()
        self.ui = del_balance_dialog_ui.Ui_Dialog()
        self.db = db
        self.ui.setupUi(self)
        self.ui.delete_btn.clicked.connect(self.del_account)
        self.ui.choosing_box.addItems([account.NAME for account in self.db.accounts])
        self.callback = callback
        icon = QIcon()
        icon.addFile('./images/app_icon.png')
        self.setWindowIcon(icon)

    def del_account(self):
        try:
            account_name = self.ui.choosing_box.currentText()
            self.db.delete_account(account_name)
            if self.callback:
                self.callback()
            self.close()
        except FileNotFoundError as ex:
            self.tell_about_exception(ex)
        except AssertionError as ex:
            self.tell_about_exception(ex)

    @staticmethod
    def tell_about_exception(msg: str):
        e = ExceptionDialog('Ошибка', msg)
        e.show()
        e.exec()
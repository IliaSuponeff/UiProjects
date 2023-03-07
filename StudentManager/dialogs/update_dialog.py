import logging
from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QIcon
from app_db import DataBase, Account, Transaction
from .exception_dialogs import ExceptionDialog
from .choose_dialogs import ChooseDateDialog
import app_db, datetime
from ui import change_trans_dialog_ui


class UpdateTransactionDialog(QDialog):

    def __init__(self, account: Account, transaction: Transaction, db: DataBase, callback=None):
        super().__init__()
        self.ui = change_trans_dialog_ui.Ui_Dialog()
        self.db = db
        self.ui.setupUi(self)
        self.account = account
        self.ui.safe_btn.clicked.connect(self.update_transaction)
        self.ui.info_le.setText(transaction.INFORMATION)
        self.ui.sum_le.setText(str(float(transaction.SUMMARY)))
        self.ui.date_choose_btn.clicked.connect(self.choose_date)
        self.ui.date_lbl.setText(str(transaction.get_time()))
        self.transaction = transaction
        self.callback = callback
        icon = QIcon()
        icon.addFile('./images/app_icon.png')
        self.setWindowIcon(icon)

    def choose_date(self):
        e = ChooseDateDialog()
        e.show()
        e.exec()
        self.ui.date_lbl.setText(str(e.date))

    def update_transaction(self):
        try:
            info = self.ui.info_le.toPlainText()
            summary = float(self.ui.sum_le.text().replace(',', '.'))
            self.db.update_transaction(self.account, self.transaction.ID, self.ui.date_lbl.text(), summary, info)
            self.account.unset_transaction(self.transaction)
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

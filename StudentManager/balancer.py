import sys
from app_filters import TableFilter, TimeFilter, SummaryFilter
from typing import Optional
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QStandardItemModel, QStandardItem, QIcon
from ui.balancer_main_ui import Ui_MainWindow
from app_db import DataBase, Account, Transaction
from dialogs import add_dialogs, delete_dialogs, exception_dialogs, \
    update_dialog, filter_dialog, results_dialogs


class Balancer(QMainWindow):

    def __init__(self, db: DataBase, currencies: list[str]):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.db: DataBase = db
        self._filter = TableFilter(TimeFilter(), SummaryFilter())
        self.currencies = currencies
        self.current_account_index = 0
        self.transactions = []

        # set btn connections
        self.ui.next_btn.clicked.connect(self.next)
        self.ui.prev_btn.clicked.connect(self.prev)
        self.ui.add_account_btn.clicked.connect(self.add_account)
        self.ui.del_account_btn.clicked.connect(self.delete_account)
        self.ui.add_trans_btn.clicked.connect(self.add_transaction)
        self.ui.del_trans_btn.clicked.connect(self.delete_transaction)
        self.ui.change_trans_btn.clicked.connect(self.update_transaction)
        self.ui.filter_settings_btn.clicked.connect(self.update_filter)
        self.ui.create_results.clicked.connect(self.create_results)
        self.ui.fast_choose_btn.clicked.connect(self.fast_choose)
        self.ui.student_box.addItems([student.NAME.replace(' ', '\n') for student in self.db.accounts])

        # set table settings
        self.transaction_table_model = QStandardItemModel()
        self.ui.balance_manager_table.setModel(self.transaction_table_model)
        self.settings_tables()
        self.reset_account()
        icon = QIcon()
        icon.addFile('./images/app_icon.png')
        self.setWindowIcon(icon)
        self.setWindowTitle("Мои студенты")

    def fast_choose(self):
        name = self.ui.student_box.currentText().replace('\n', ' ')
        for i in range(len(self.db.accounts)):
            if self.db.accounts[i].NAME == name:
                self.current_account_index = i
                break

        self.reset_account()

    def create_results(self):
        if not self.get_current_account():
            e = exception_dialogs.ExceptionDialog('Предупреждение', 'В базе данных нет ни одного ученика,\n'
                                                                    'добавьте его.')
        elif len(self.transactions) == 0:
            e = exception_dialogs.ExceptionDialog('Предупреждение', 'В фильтре нет ни одного посещения у ученика, '
                                                                    'перенастройте его.')
        else:
            e = results_dialogs.CreateResultsDialog(self._filter, self.get_current_account(),
                                                    self.transactions)
        e.show()
        e.exec()

    def update_filter(self):
        if not self.get_current_account():
            e = exception_dialogs.ExceptionDialog('Предупреждение', 'В базе данных нет ни одного ученика,\n'
                                                                    'добавьте его.')
        else:
            e = filter_dialog.FilterTransactionDialog(self._filter, self.update_transaction_table)
        e.show()
        e.exec()

    def get_current_account(self) -> Optional[Account]:
        if len(self.db.accounts) != 0 and 0 <= self.current_account_index < len(self.db.accounts):
            return self.db.accounts[self.current_account_index]
        return None

    def clear_filter(self):
        self._filter.time_filter = TimeFilter()
        self._filter.summary_filter = SummaryFilter()

    def next(self):
        self.clear_filter()
        self._move_account(1)

    def prev(self):
        self.clear_filter()
        self._move_account(-1)

    def _move_account(self, shift=0):
        if len(self.db.accounts) != 0:
            self.current_account_index += shift
            self.current_account_index %= len(self.db.accounts)
            self.reset_account()

    def _get_last_account(self):
        index = len(self.db.accounts) - 1
        if index >= 0:
            self.clear_filter()
            self.current_account_index = index
            self.reset_account()

    def add_account(self):
        e = add_dialogs.AddAccountDialog(self.db, self.currencies,
                                         callback=lambda: self._get_last_account())
        e.show()
        e.exec()

    def update_filter_prev_reset_account(self):
        self.clear_filter()
        self.reset_account()

    def delete_account(self):
        if len(self.db.accounts) > 0:

            e = delete_dialogs.DelAccountDialog(self.db, callback=self.update_filter_prev_reset_account)
        else:
            e = exception_dialogs.ExceptionDialog('Предупреждение', 'В базе данных нет ни одного ученика,\n'
                                                                    'добавьте его.')
        e.show()
        e.exec()

    def reset_account(self):
        if len(self.db.accounts) == 0:
            info_text = '-'
            balance = '-'
            currency = ''
        else:
            account = self.db.accounts[self.current_account_index]
            info_text = account.NAME
            balance = account.BALANCE
            currency = account.CURRENCY
        self.ui.balance_info_lbl.setText(f'Ученик: {info_text}')
        self.ui.balance_lbl.setText(f'{balance}{currency}')
        self.update_transaction_table()

    def add_transaction(self):
        if not self.get_current_account():
            e = exception_dialogs.ExceptionDialog('Предупреждение', 'В базе данных нет ни одного ученика,\n'
                                                                    'добавьте его.')
        else:
            e = add_dialogs.AddTransactionDialog(self.get_current_account(), self.db,
                                                 callback=self.reset_account)
        e.show()
        e.exec()

    def delete_transaction(self):
        if self.get_current_account():
            indexes = self.ui.balance_manager_table.selectedIndexes()
            if len(indexes) != 0:
                rows = set()
                for index in indexes:
                    rows.add(index.row())

                rows = sorted(list(rows), reverse=True)
                for row in rows:
                    if row + 1 == self.transaction_table_model.rowCount():
                        break
                    item_row: list[QStandardItem] = self.transaction_table_model.takeRow(row)
                    transaction_row = [item.text() for item in item_row]
                    transaction = self.transactions[int(transaction_row[0]) - 1]
                    self.db.delete_transaction(self.get_current_account(), transaction)
                self.reset_account()
            else:
                e = exception_dialogs.ExceptionDialog('Предупреждение',
                                                      'Вы не выделили ни одного урока для удаления.')
                e.show()
                e.exec()
        else:
            e = exception_dialogs.ExceptionDialog('Предупреждение',
                                                  'В базе данных нет ни одного ученика,\n'
                                                  'добавьте его.')
            e.show()
            e.exec()

    def update_transaction(self):
        if self.get_current_account():
            indexes = self.ui.balance_manager_table.selectedIndexes()
            if len(indexes) != 0:
                if indexes[0].row() + 1 == self.transaction_table_model.rowCount():
                    e = exception_dialogs.ExceptionDialog('Предупреждение',
                                                          'Вы выделили запись фильтра.\n'
                                                          'Её нельзя изменить.')
                else:
                    table = self.transaction_table_model.takeRow(indexes[0].row())
                    transaction_row = [item.text() for item in table]
                    transaction = self.transactions[int(transaction_row[0]) - 1]
                    self.reset_account()
                    e = update_dialog.UpdateTransactionDialog(
                        self.get_current_account(), transaction, self.db, self.reset_account)

            else:
                e = exception_dialogs.ExceptionDialog('Предупреждение',
                                                      'Вы не выделили посещение для изменения.')
        else:
            e = exception_dialogs.ExceptionDialog('Предупреждение',
                                                  'В базе данных нет ни одного ученика,\n'
                                                  'добавьте его.')
        e.show()
        e.exec()

    def update_transaction_table(self):
        self.clear_table_model(self.transaction_table_model)
        _id = 1
        t = self.db.get_transactions(self.get_current_account())
        t = self._filter.check_transactions(t)
        self.transactions = t.copy()
        for transaction in t:
            row = [
                QStandardItem(str(_id) if _id != len(t) else 'Итог'),
                QStandardItem(str(transaction.get_time())),
                QStandardItem(str(transaction.get_summary())),
                QStandardItem(str(transaction.INFORMATION))
            ]
            _id += 1
            for item in row:
                item.setEditable(False)
            self.transaction_table_model.appendRow(row)

    @staticmethod
    def clear_table_model(model: QStandardItemModel):
        while model.rowCount() > 0:
            model.removeRow(0)

    def settings_tables(self):
        # transactions table
        self.transaction_table_model.setHorizontalHeaderLabels(
            ["ID", "Дата", "Сумма", "Информация"]
        )
        width = self.ui.balance_manager_table.width() * 1.8
        self.ui.balance_manager_table.setColumnWidth(0, width // 1.5)
        self.ui.balance_manager_table.setColumnWidth(1, width * 1.3)
        self.ui.balance_manager_table.setColumnWidth(2, width)
        self.ui.balance_manager_table.setColumnWidth(3, width * 2)
        self.ui.balance_manager_table.verticalHeader().hide()


class BalancerApp(QApplication):

    def __init__(self):
        """
        Initialize AppMainWindow
        """
        super().__init__()
        self.db = DataBase()
        self.currensies = ['BYN', 'RUB', 'USD', 'EUR']
        self.window = Balancer(self.db, self.currensies)
        self.window.show()

    def exec_(self) -> int:
        code = super().exec()
        self.db.save_accounts()
        self.db.close()
        return code


if __name__ == '__main__':
    app = BalancerApp()

    sys.exit(app.exec_())

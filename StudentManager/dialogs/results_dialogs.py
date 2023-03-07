import os.path
import tkinter.filedialog
from .exception_dialogs import ExceptionDialog
from ui import create_results_ui
import logging
from PySide6.QtWidgets import QDialog
from app_db import Transaction, Account
from app_filters import TableFilter
from PySide6.QtGui import QIcon
from .exception_dialogs import ExceptionDialog
from ui import create_results_ui


class CreateResultsDialog(QDialog):

    def __init__(self, _filter: TableFilter, account: Account, transactios: list[Transaction]):
        super().__init__()
        self.ui = create_results_ui.Ui_Dialog()
        self.ui.setupUi(self)
        icon = QIcon()
        icon.addFile('./images/app_icon.png')
        self.setWindowIcon(icon)
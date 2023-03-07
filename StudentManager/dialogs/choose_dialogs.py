import datetime
from PySide6.QtWidgets import QDialog
from app_db import DataBase, Account, get_time_now
from PySide6.QtGui import QIcon
from ui import date_choose_dialog_ui


class ChooseDateDialog(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = date_choose_dialog_ui.Ui_Dialog()
        self.ui.setupUi(self)
        self.date = get_time_now()
        self.ui.choose_btn.clicked.connect(self.choose)
        icon = QIcon()
        icon.addFile('./images/app_icon.png')
        self.setWindowIcon(icon)
        self.setWindowTitle("Выберите дату!")

    def choose(self):
        d = self.ui.calendar.selectedDate().getDate()
        t = datetime.datetime.now()
        self.date = f"{d[2]}.{d[1]}.{d[0]} {t.hour}:{t.minute}:{t.second}"
        self.close()

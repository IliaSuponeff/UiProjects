from PySide6.QtWidgets import QDialog
from ui import exception_dialog_ui
from PySide6.QtGui import QIcon


class ExceptionDialog(QDialog):

    def __init__(self, title, msg):
        super().__init__()
        self.ui = exception_dialog_ui.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.title_lbl.setText('Ошибка!')
        self.ui.msg_lbl.setText(str(msg))
        self.setWindowTitle(str(title).title())
        self.ui.close_btn.clicked.connect(self.close)
        icon = QIcon()
        icon.addFile('./images/app_icon.png')
        self.setWindowIcon(icon)


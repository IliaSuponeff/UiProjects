from .abc_plugin import AbcPlugin
from PyQt5.QtWidgets import QPlainTextEdit, QVBoxLayout, QPushButton, QTextEdit
from PyQt5.QtGui import QFontMetricsF


class StdPlugin(AbcPlugin):

    def __init__(self, parent, settings):
        super().__init__(parent, settings)

    def init_view(self):
        self.text_edit = QTextEdit()
        self.text_edit.setText(
            "This is a standart plugin, "
            "if it loaded check settings.xml and __plugins__.xml and see is added other plugins")
        self.text_edit.setTabStopDistance(QFontMetricsF(self.text_edit.font()).horizontalAdvance(' ') * 6)
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.text_edit)


    def init_handlers(self):
        pass

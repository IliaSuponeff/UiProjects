import copy
import os.path

from .abc_plugin import AbcPlugin
from PyQt5.QtWidgets import (QPlainTextEdit, QVBoxLayout, QPushButton,
                             QTextEdit, QMenuBar, QMenu,
                             QAction, qApp, QFileDialog, QMessageBox, QStyle)
from PyQt5.QtGui import QFontMetricsF, QKeySequence, QFontDatabase, QFont


class NoteBook(AbcPlugin):

    def __init__(self, parent, settings):
        super().__init__(parent, settings)
        self.filename = ""  # open file name, if file not opened than it equals empty string
        self.file_types = {
            "Text file": ("*.txt"),
            "All files": ("*.*")
        }

    def init_view(self):
        self.init_ui()
        self.init_menu()

    def init_ui(self):
        self.setLayout(QVBoxLayout())
        self.note = QTextEdit()
        self.layout().addWidget(self.note)

    def init_menu(self):
        menu = self.parent.menuBar()
        self.file_menu = menu.addMenu("File")
        self.settings_menu = menu.addMenu("Settings")
        self.theme_menu = self.settings_menu.addMenu("Themes")
        self.font_menu = self.settings_menu.addMenu("Fonts")
        self.font_family_menu = self.font_menu.addMenu("Family")
        self.font_size_menu = self.font_menu.addMenu("Size")

    def init_handlers(self):
        # add actions to file menu
        self.add_menu_action(self.file_menu, "New", "Ctrl+N", self.new_file)
        self.add_menu_action(self.file_menu, "Open", "Ctrl+O", self.open_file)
        self.add_menu_action(self.file_menu, "Save", "Ctrl+S", self.save_file)
        self.add_menu_action(self.file_menu, "Save as", "Ctrl+A", self.save_file_as)
        self.file_menu.addSeparator()
        self.add_menu_action(self.file_menu, "Close", "Ctrl+B", self.close_file)
        self.add_menu_action(self.file_menu, "Exit", "Ctrl+Q", self.exit)

        # add actions to settings menu
        ##  add actions to theme menu
        for theme in self.settings.themes:
            self.add_theme_action(theme)

        ##  add actions to fonts menu
        for family in QFontDatabase().families():
            self.add_font_family_action(family)

        ##  add actions to fonts menu
        for size in range(8, 32 + 1):
            self.add_font_size_action(size)

    def add_theme_action(self, theme):
        self.add_menu_action(self.theme_menu, str(theme.name).title(), "", lambda: self.set_theme(theme))

    def set_theme(self, theme):
        self.parent.setStyleSheet(theme.get_styles())

    def add_font_size_action(self, size):
        self.add_menu_action(self.font_size_menu, str(size), "", lambda: self.set_font_size(size))

    def set_font_size(self, size):
        cursor = self.note.textCursor()
        self.note.selectAll()
        self.note.setFontPointSize(size)
        self.note.setTextCursor(cursor)

    def add_font_family_action(self, family):
        self.add_menu_action(self.font_family_menu, str(family), "", lambda: self.set_font_family(family))

    def set_font_family(self, family):
        cursor = self.note.textCursor()
        self.note.selectAll()
        self.note.setFontFamily(family)
        self.note.setTextCursor(cursor)

    def need_save(self) -> bool:
        return QMessageBox.question(self.parent, "Saved?", "Is need save text?",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No) == QMessageBox.Yes

    def new_file(self):
        self.check_save()
        self.clear_all()

    def open_file(self):
        self.new_file()
        self.filename = self.get_filename()
        with open(self.filename) as file:
            self.note.setPlainText(file.read())

    def save_file(self):
        if self.filename:
            self.write_file(self.filename, self.note.toPlainText())
        else:
            self.save_file_as()

    def save_file_as(self):
        self.filename = self.get_filename()
        self.write_file(self.filename, self.note.toPlainText())

    def close_file(self):
        self.check_save()
        self.clear_all()

    def exit(self):
        self.close()
        self.parent.close()

    def clear_all(self):
        self.note.setPlainText("")
        self.filename = ""

    def get_filename(self):
        filename = ""
        directory = self.settings.ROOT if not self.filename else os.path.dirname(self.filename)
        _filter: str = self.get_file_types_filter()
        while not filename:
            filename, _ = QFileDialog.getOpenFileName(self.parent, "Choose file", directory,
                                                      _filter, _filter.split(";;")[0])
        return filename

    def get_file_types_filter(self) -> str:
        _filter = ""
        for key in self.file_types:
            if self.file_types.get(key):
                _filter += f"{key} {self.file_types.get(key)};;"
        return _filter.strip(";;")

    def check_save(self):
        if self.filename and self.note.toPlainText() and self.need_save():
            self.save_file()
        elif self.filename and self.need_save():
            self.save_file()

    @staticmethod
    def write_file(filename, text):
        with open(filename, "w") as file:
            file.write(text)

    @staticmethod
    def add_menu_action(root: QMenu, title: str, shortcut: QKeySequence | str, callback):
        action = QAction(title, root)
        action.setShortcut(QKeySequence(shortcut))
        if callback:
            action.triggered.connect(callback)
        root.addAction(action)

import sys
from PyQt5.QtWidgets import (QWidget, QMainWindow, QTextEdit, QTextBrowser,
                             QHBoxLayout, QVBoxLayout)
from PyQt5.QtCore import Qt
from settings import Settings
import view_plugins


class Ui(QMainWindow):

    def __init__(self, settings: Settings):
        super().__init__()
        self.settings = settings
        self.setSettings()
        self.plugin_widget = None

        try:
            plugin_path = "view_plugins.std_plugin.StdPlugin"
            if self.settings.get_current_plugin() is not None:
                plugin_path = self.settings.get_current_plugin().get_path()
            self.plugin_widget = eval(f'{plugin_path}(self, self.settings)')
        except Exception as ex:
            self.plugin_widget = view_plugins.std_plugin.StdPlugin(self, settings)
            print(f"LoadingPluginError: {ex}", file=sys.stderr)
        self.setCentralWidget(self.plugin_widget)

    def setSettings(self):
        self.setWindowTitle(self.settings.get_title())
        if self.settings.get_current_theme() is not None:
            self.setStyleSheet(self.settings.get_current_theme().get_styles())
        self.setMinimumSize(self.settings.window_size)
        self.setWindowState(Qt.WindowState.WindowMaximized)
        if self.settings.window_icon is not None:
            self.setWindowIcon(self.settings.window_icon)

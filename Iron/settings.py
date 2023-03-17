import os.path
import sys
import xml.etree.ElementTree as ET
import view_plugins
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon


class StdSettings:
    ROOT = os.path.dirname(os.path.abspath(__file__))
    RESOURCES_DIR = os.path.join(ROOT, "resources")
    PLUGINS_DIR = os.path.join(ROOT, "view_plugins")

    def __init__(self, debug=True):
        self._DEBUG = debug
        self.current_plugin = 0
        self.current_theme = 0
        self.window_size = QSize(480, 360)
        self.window_icon = None
        self.style_sheet = ""
        self.themes = []
        self.plugins = []

    def get_title(self):
        return f"Iron{'[DEBUG=True]' if self._DEBUG else ''}"

    def get_current_theme(self):
        if 0 <= self.current_theme < len(self.themes):
            return self.themes[self.current_theme]
        self.current_theme = 0
        return None

    def get_current_plugin(self):
        if 0 <= self.current_plugin < len(self.plugins):
            return self.plugins[self.current_plugin]
        self.current_plugin = 0
        return None


class Plugin:
    def __init__(self, name):
        self.name = name
        self.path = ""
        self.version = "-"

    def get_path(self):
        return self.path.replace("/", ".").replace("\\", '.')

    def __str__(self) -> str:
        return f'<Plugin name="{self.name}" path="{self.get_path()}", version="{self.version}"/>'

    def __repr__(self) -> str:
        return self.__str__()


class Theme:

    def __init__(self, filename):
        self.filename = filename
        self.name = ""
        self.style_sheet = ""
        self.version = ""

    def get_styles(self):
        date = ""
        path = os.path.join(StdSettings.RESOURCES_DIR, "styles", self.style_sheet)
        if os.path.exists(path):
            with open(path) as f:
                data = f.read()
        else:
            print(f"Not found style-sheet file by path: '{path}'", file=sys.stderr)
        return data

    def __str__(self) -> str:
        return f"<Theme name='{self.name}' style-sheet='{self.style_sheet}' version='{self.version}'>"

    def __repr__(self) -> str:
        return self.__str__()


class Settings(StdSettings):

    def __init__(self, debug):
        super().__init__(bool(debug))
        # loaded settings:
        root = ET.parse(os.path.join(self.RESOURCES_DIR, "settings.xml")).getroot()
        for child in root:
            tag = child.tag.lower()
            text = child.text
            _type = child.attrib.get('type')
            if tag == "theme":
                name = os.path.join(self.RESOURCES_DIR, "themes", f"{text}.theme.xml")
                if not os.path.exists(name):
                    print(f"Not fount theme: '{text}', by path: '{name}'", file=sys.stderr)
                else:
                    self.load_theme(text)
            elif tag == "plugin":
                name = os.path.join(self.PLUGINS_DIR, f"__plugins__.xml")
                if not os.path.exists(name):
                    print(f"Not fount plugin-file: '{name}'", file=sys.stderr)
                else:
                    self.load_plugin(name)
            else:
                if text != "!":
                    if _type == "int":
                        text = int(text)
                    self.__setattr__(tag, text)
        self.get_current_settings()

    def get_current_settings(self):
        if isinstance(self.window_size, str):
            self.window_size = QSize(*[int(float(i)) for i in self.window_size.split("x")])

        if self.window_icon is not None:
            path = os.path.join(self.RESOURCES_DIR, "images", self.window_icon)
            self.window_icon = QIcon()
            if os.path.exists(path):
                self.window_icon.addFile(path)
            else:
                print(f"Not found window-icon file by path: '{path}'", file=sys.stderr)

    def load_plugin(self, plugin_name: str):
        root = ET.parse(os.path.join(self.PLUGINS_DIR, f"__plugins__.xml")).getroot()
        index = 0
        for child in root:
            tag = child.tag.lower()
            if tag == "plugin":
                name = child.attrib.get('name')
                if name == plugin_name:
                    self.current_plugin = index
                p = Plugin(name)
                for sub in child:
                    p.__setattr__(sub.tag.lower(), sub.text)
                self.plugins.append(p)
                index += 1
            else:
                print(f"In plugin-file invalidate tag: {tag}", file=sys.stderr)

    def load_theme(self, theme_name: str):
        root = ET.parse(os.path.join(self.RESOURCES_DIR, "themes", f"{theme_name}.theme.xml")).getroot()
        t = Theme(theme_name)
        for child in root:
            t.__setattr__(child.tag.lower(), child.text)
        self.themes.append(t)

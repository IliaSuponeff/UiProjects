import json
import os
import tkinter
import xml.etree.ElementTree as ElTree


class Theme:

    def __init__(self, **kwargs):
        self._attrs = list(kwargs.keys())
        for attr in kwargs.keys():
            self.__setattr__(attr, kwargs[attr])
        if 'name' not in self._attrs:
            self.__setattr__('name', None)

    def init_by_xml_element(self, element: ElTree.ElementTree):
        for child in element.iter():
            if child.tag != 'Theme':
                self.__setattr__(child.tag, child.text)
                self._attrs.append(child.tag)
        return self

    def apply_a_theme(self, widget):
        if widget is not None:
            for attr in self._attrs:
                if attr == 'name':
                    continue
                try:
                    if self.__getattribute__(attr) is not None:
                        widget[attr] = self.__getattribute__(attr)
                except:
                    # ignored errors
                    pass


class TextFont:

    def __init__(self, name, size=12, _type=tkinter.NORMAL):
        self.name = name
        self.size = size
        self._type = _type

    def get_Tk_font(self):
        return self.name, self.size, self._type


class Settings:
    _PATH = os.path.dirname(os.path.abspath(__file__))

    def __init__(self):
        self.geometry = '600x600+200+200'
        self.resizable = (True, True)
        self.title = "NotePad"
        self.icon = os.path.join(self._PATH, 'resources', 'images', 'notepad.ico')
        if not os.path.exists(self.icon):
            self.icon = None
        self.fonts: list[str] = self._get_fonts()
        self.themes: list[Theme] = self._get_themes()
        self.theme = self.themes[0]
        self.MIN_FONT_SIZE = 12
        self.MAX_FONT_SIZE = 24
        self.menu_font = TextFont(self.fonts[0])
        self.text_font = TextFont(self.fonts[0])
        self.filetypes = (('Text documents (*.txt)', '*.txt'), ('All files (*.*)', '*.*'))

    def _get_themes(self) -> list[Theme]:
        try:
            xml_data = self._load_xml_file(os.path.join('resources', 'settings', 'themes.xml'))
            result = []
            for event, elem in xml_data:
                if elem.tag == 'Theme':
                    result.append(Theme().init_by_xml_element(ElTree.ElementTree(elem)))
            return result
        except:
            return []
        return []

    def _load_xml_file(self, file_path):
        return ElTree.iterparse(os.path.join(self._PATH, file_path))

    def set_theme_by_name(self, name):
        for theme in self.themes:
            if theme.name == name:
                self.theme = theme

    def _get_fonts(self):
        try:
            result = []
            with open(os.path.join(self._PATH, 'resources', 'settings', 'fonts.json')) as file:
                result = json.load(file)
            return result
        except:
            return ['Arial', 'Times New Roman']
        return ['Arial', 'Times New Roman']

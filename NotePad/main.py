import os.path
from tkinter import *
from tkinter import messagebox, filedialog
import settings


class State:

    def __init__(self):
        self.is_open = False
        self.path = False


class NotePad:

    def __init__(self):
        self.root = Tk()
        self.settings = settings.Settings()
        self.root.geometry(self.settings.geometry)
        self.root.title(self.settings.title)
        if self.settings.icon is not None:
            self.root.iconbitmap(self.settings.icon)
        self.ui = {}
        self._set_ui()
        self.STATE = State()

    def run(self):
        self.root.mainloop()

    def _set_ui(self):
        self._set_menu()
        self._set_workspace()
        self._set_ui_visual_settings()

    @staticmethod
    def _build_menu(menu: Menu, labels: dict):
        for _label in labels:
            if _label is None:
                continue
            if _label == '__sep__' and labels.get(_label) is None:
                menu.add_separator()
            else:
                menu.add_command(label=_label, command=labels.get(_label))

    def _set_menu(self):
        self.ui['main_menu'] = Menu(self.root, tearoff=0)

        self.ui['file_menu'] = Menu(self.ui['main_menu'], tearoff=0)
        self._build_menu(self.ui['file_menu'], {
            'Open': self.open_file,
            'Save': self.save,
            'Save as': self.save_as,
            '__sep__': None,
            'Close': self.close,
            'Exit': self._exit
        })

        self.ui['view_menu'] = Menu(self.ui['main_menu'], tearoff=0)

        self.ui['themes_menu'] = Menu(self.ui['view_menu'], tearoff=0)
        d = {}
        for i in range(len(self.settings.themes)):
            d.setdefault(self.settings.themes[i].name, self._get_theme_lambda(i))
        self._build_menu(self.ui['themes_menu'], d)

        self.ui['font_menu'] = Menu(self.ui['view_menu'], tearoff=0)
        d = {}
        for i in range(len(self.settings.fonts)):
            d.setdefault(self.settings.fonts[i], self._get_font_lambda(i))
        self._build_menu(self.ui['font_menu'], d)

        self.ui['text_size_menu'] = Menu(self.ui['view_menu'], tearoff=0)
        d = {}
        for i in range(self.settings.MIN_FONT_SIZE, self.settings.MAX_FONT_SIZE + 1):
            d.setdefault(f"Size {i}", self._get_size_lambda(i))
        self._build_menu(self.ui['text_size_menu'], d)

        self.ui['view_menu'].add_cascade(label='Themes', menu=self.ui['themes_menu'])
        self.ui['view_menu'].add_cascade(label='Fonts', menu=self.ui['font_menu'])
        self.ui['view_menu'].add_cascade(label='Font Size', menu=self.ui['text_size_menu'])

        self.ui['main_menu'].add_cascade(label='File', menu=self.ui['file_menu'])
        self.ui['main_menu'].add_cascade(label='View', menu=self.ui['view_menu'])

        self.root.config(menu=self.ui['main_menu'])

    def _set_workspace(self):
        self.ui['main_frame'] = Frame(self.root)

        self.ui['text_label'] = Text(self.ui['main_frame'], wrap=WORD, width=30)

        self.ui['scroll'] = Scrollbar(self.ui['main_frame'], command=self.ui['text_label'].yview)
        self.ui['text_label'].config(yscrollcommand=self.ui['scroll'].set)

        # pack ui elements
        self.ui['main_frame'].pack(fill=BOTH, expand=1)
        self.ui['text_label'].pack(expand=1, fill=BOTH, side=LEFT)
        self.ui['scroll'].pack(side=LEFT, fill=Y)

    def _set_ui_visual_settings(self):
        self._set_theme(0)
        self._set_font(0)

    def _set_theme(self, theme_number):
        try:
            self.settings.theme = self.settings.themes[theme_number]
        except:
            print("OutOfRange")
        for name in self.ui:
            self.settings.theme.apply_a_theme(self.ui.get(name))

    def _set_font(self, font_number=None):
        if font_number is not None:
            try:
                t = self.settings.text_font.get_Tk_font()
                self.settings.text_font = settings.TextFont(self.settings.fonts[font_number], t[1], t[2])
            except:
                pass
        for name in self.ui:
            try:
                if 'menu' in name:
                    self.ui[name]['font'] = self.settings.menu_font.get_Tk_font()
                else:
                    self.ui[name]['font'] = self.settings.text_font.get_Tk_font()
            except:
                # ignored exception
                pass

    def open_file(self):
        path = filedialog.askopenfilename(filetypes=self.settings.filetypes)
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as file:
                self.ui['text_label'].delete('1.0', END)
                self.ui['text_label'].insert('1.0', file.read())

            self._change_state(True, path)
        else:
            messagebox.showerror("Error!", f"File '{path}'not found!")

    def save(self):
        if self.STATE.is_open and self.STATE.path:
            with open(self.STATE.path, 'w', encoding='utf-8') as file:
                file.write(self.ui['text_label'].get('1.0', END))
            self._change_state(True, self.STATE.path)
        else:
            self.save_as()

    def save_as(self):
        path = filedialog.asksaveasfilename(filetypes=self.settings.filetypes)
        if path is None or path.strip() == '':
            self._change_state(False, None)
        else:
            with open(path, 'w', encoding='utf-8') as file:
                file.write(self.ui['text_label'].get('1.0', END))
            self._change_state(True, path)

    def close(self):
        self.save()
        self.ui['text_label'].delete('1.0', END)
        self._change_state(False, None)

    def _change_state(self, is_open, path):
        self.STATE.is_open = bool(is_open) and (path is not None)
        self.STATE.path = path

    def _get_theme_lambda(self, i):
        return lambda: self._set_theme(i)

    def _set_font_size(self, i):
        if self.settings.MIN_FONT_SIZE <= i <= self.settings.MAX_FONT_SIZE:
            self.settings.text_font.size = i
            self._set_font()
        else:
            messagebox.showerror("Invalid FontSize", f'FontSize "{i}" not supported.')

    def _get_font_lambda(self, i):
        return lambda: self._set_font(i)

    def _exit(self):
        self.save()
        self.root.destroy()
        self.root.quit()

    def _get_size_lambda(self, i):
        return lambda: self._set_font_size(i)


if __name__ == '__main__':
    notepad = NotePad()
    notepad.run()

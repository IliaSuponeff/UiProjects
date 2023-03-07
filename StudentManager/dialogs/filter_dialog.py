import logging
import random
from app_filters import *
from PySide6.QtWidgets import QDialog, QCheckBox
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6 import QtCore
from PySide6.QtGui import QIcon
from app_db import DataBase, Account
from .exception_dialogs import ExceptionDialog
from .choose_dialogs import ChooseDateDialog
from ui import filter_dialog_ui


class FilterTransactionDialog(QDialog):
    _super_filter_types = ['За этот год', 'За этот месяц']
    _convert_funcs = {
        'За этот год': TimeFilter.this_year, 'За этот месяц': TimeFilter.this_month,
    }

    def __init__(self, _filter: TableFilter, callback=None):
        super().__init__()
        self.ui = filter_dialog_ui.Ui_Dialog()
        self.ui.setupUi(self)
        self._filter = _filter
        self.callback = callback
        self.ui.save_btn.clicked.connect(self.save_filter)
        self.ui.sum_filter_box.addItems(FilterFlags.get_dict().keys())
        self.ui.time_filtr_box.addItems(list(FilterFlags.get_dict().keys()) + self._super_filter_types)
        self.ui.dete_to_btn.clicked.connect(lambda: self.choose_date(False))
        self.ui.date_from_btn.clicked.connect(lambda: self.choose_date(True))
        icon = QIcon()
        icon.addFile('./images/app_icon.png')
        self.setWindowIcon(icon)

    def choose_date(self, is_from):
        e = ChooseDateDialog()
        e.show()
        e.exec()
        if is_from:
            self.ui.from_lbl.setText(e.date)
        else:
            self.ui.to_lbl.setText(e.date)

    def save_filter(self):
        try:
            self.set_summary_filter()
            self.set_time_filter()
            if self.callback:
                self.callback()
            self.close()
        except Exception as ex:
            logging.exception(ex)
            self.tell_about_exception(ex)

    @staticmethod
    def tell_about_exception(msg: str):
        e = ExceptionDialog('Ошибка', msg)
        e.show()
        e.exec()

    def set_time_filter(self):
        filter_name = self.ui.time_filtr_box.currentText()
        if filter_name in self._super_filter_types:
            filter_type = FilterFlags.FROM_TO
        else:
            filter_type = FilterFlags.get_dict()[filter_name]
        if filter_type == FilterFlags.FROM_TO:
            if filter_name in self._super_filter_types:
                _from, _to = self._convert_funcs[filter_name]()
            else:
                _from = self.ui.from_lbl.text().strip()
                _to = self.ui.to_lbl.text().strip()
                if not TimeFilter.is_more(_to, _from):
                    _to, _from = _from, _to
                if _from == '-' or _to == '-':
                    raise Exception("Вы выбрали тип фильтра 'Из отрезка', но не настроили отрезок.\n"
                                    "Поля От и До на должны быть пустыми.")
            self._filter.time_filter = TimeFilter(filter_type, _from, _to)
        else:
            self._filter.time_filter = TimeFilter()

    def set_summary_filter(self):
        filter_type = FilterFlags.get_dict()[self.ui.sum_filter_box.currentText()]
        if filter_type == FilterFlags.FROM_TO:
            _from = self.ui.from_le.text()
            _to = self.ui.to_le.text()
            if len(_to) == 0 or len(_from) == 0:
                raise Exception('Вы выбрали категорию ОТРЕЗОК для фильтра сумм.\n'
                                'Поля "От" и "До" не должны быть пустыми')
            try:
                _from = float(_from)
                _to = float(_to)
                if _from > _to:
                    raise Exception("Exc")
                self._filter.summary_filter = SummaryFilter(filter_type, _from, _to)
            except:
                raise Exception('Вы выбрали категорию ОТРЕЗОК для фильтра сумм.\n'
                                'Поля "От" и "До" должны содержать целое или дробное число.\n'
                                'Поле "От" должно быть меньше значения в поле "До"')
        else:
            self._filter.summary_filter = SummaryFilter(filter_type)

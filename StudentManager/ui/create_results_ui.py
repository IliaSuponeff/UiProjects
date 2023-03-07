# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_results.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(787, 243)
        Dialog.setStyleSheet(u"QWidget {\n"
"	color: white;\n"
"	background-color: qlineargradient(spread:reflect, x1:0.647, y1:0.483864, x2:0, y2:0.972, stop:0.298507 rgba(130, 0, 255, 255), stop:0.935323 rgba(255, 102, 102, 255));\n"
"	font: 75 12pt \"Rubik\";\n"
"}\n"
"QLabel {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"QComboBox {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"QLineEdit {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {	\n"
"	color: black;\n"
"	background-color: #666;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #aaa;\n"
"}\n"
"\n"
"QTableView {\n"
"	background-color: rgba(255, 255, 255, 30); \n"
"	border: 1px solid rgba(255,255,255,40);\n"
"	border-bottom-right-radius: 7px; \n"
"	border-bottom-left-radius: 7px; \n"
"	color: white;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"	background-color: rgb(53, 53, 53);\n"
"	color: white;\n"
"	height: 50px;\n"
"	font-size: 16p"
                        "t;\n"
"}\n"
"\n"
"QTableView::item {\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgba(255,255,255,50);\n"
"    padding-left: auto;\n"
"    padding-right: auto;\n"
"}\n"
"\n"
"QTableView::item:selected{\n"
"	border: none;\n"
"	color: rgb(255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 50);\n"
"}")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lbl_2 = QLabel(Dialog)
        self.lbl_2.setObjectName(u"lbl_2")

        self.gridLayout.addWidget(self.lbl_2, 1, 0, 1, 1)

        self.file_type_box = QComboBox(Dialog)
        self.file_type_box.setObjectName(u"file_type_box")

        self.gridLayout.addWidget(self.file_type_box, 0, 1, 1, 1)

        self.lbl_1 = QLabel(Dialog)
        self.lbl_1.setObjectName(u"lbl_1")

        self.gridLayout.addWidget(self.lbl_1, 0, 0, 1, 1)

        self.get_path_btn = QPushButton(Dialog)
        self.get_path_btn.setObjectName(u"get_path_btn")

        self.gridLayout.addWidget(self.get_path_btn, 2, 0, 1, 1)

        self.file_name_le = QLineEdit(Dialog)
        self.file_name_le.setObjectName(u"file_name_le")

        self.gridLayout.addWidget(self.file_name_le, 1, 1, 1, 1)

        self.path_save_le = QLineEdit(Dialog)
        self.path_save_le.setObjectName(u"path_save_le")
        self.path_save_le.setReadOnly(True)

        self.gridLayout.addWidget(self.path_save_le, 2, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.create_results_btn = QPushButton(Dialog)
        self.create_results_btn.setObjectName(u"create_results_btn")

        self.verticalLayout.addWidget(self.create_results_btn)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u043e\u0442\u0447\u0451\u0442\u0430", None))
        self.lbl_2.setText(QCoreApplication.translate("Dialog", u"\u0418\u043c\u044f", None))
        self.lbl_1.setText(QCoreApplication.translate("Dialog", u"\u0422\u0438\u043f \u0444\u0430\u0439\u043b\u0430", None))
        self.get_path_btn.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u043f\u0443\u0442\u044c \u0434\u043b\u044f \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u044f", None))
        self.file_name_le.setText("")
        self.create_results_btn.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
    # retranslateUi


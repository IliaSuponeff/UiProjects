# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'filter_dialog.ui'
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
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(800, 300)
        Dialog.setStyleSheet(u"QWidget {\n"
"	color: white;\n"
"	background-color: qlineargradient(spread:reflect, x1:0.647, y1:0.483864, x2:0, y2:0.972, stop:0.298507 rgba(130, 0, 255, 255), stop:0.935323 rgba(255, 102, 102, 255));\n"
"	font: 75 12pt \"Rubik\";\n"
"}\n"
"\n"
"QLabel {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"QComboBox {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
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
"QListView {\n"
"	background-color: rgba(255, 255, 255, 30); \n"
"	border: 1px solid rgba(255,255,255,40);\n"
"	border-bottom-right-radius: 7px; \n"
"	border-bottom-left-radius: 7px; \n"
"	color: white;\n"
"}\n"
"\n"
"QTableView {\n"
"	background-color: rgba(255, 255, 255, 30); \n"
"	border: 1px solid rgba(255,255,255,40);\n"
""
                        "	border-bottom-right-radius: 7px; \n"
"	border-bottom-left-radius: 7px; \n"
"	color: white;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"	background-color: rgb(53, 53, 53);\n"
"	color: white;\n"
"	height: 50px;\n"
"	font-size: 16pt;\n"
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
        self.verticalLayout_3 = QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbl_6 = QLabel(Dialog)
        self.lbl_6.setObjectName(u"lbl_6")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_6.sizePolicy().hasHeightForWidth())
        self.lbl_6.setSizePolicy(sizePolicy)
        self.lbl_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lbl_6)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.sum_filter_box = QComboBox(Dialog)
        self.sum_filter_box.setObjectName(u"sum_filter_box")
        sizePolicy.setHeightForWidth(self.sum_filter_box.sizePolicy().hasHeightForWidth())
        self.sum_filter_box.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.sum_filter_box, 0, 1, 1, 1)

        self.lbl_3 = QLabel(Dialog)
        self.lbl_3.setObjectName(u"lbl_3")
        self.lbl_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbl_3, 0, 0, 1, 1)

        self.lbl_4 = QLabel(Dialog)
        self.lbl_4.setObjectName(u"lbl_4")
        self.lbl_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbl_4, 2, 0, 1, 1)

        self.lbl_5 = QLabel(Dialog)
        self.lbl_5.setObjectName(u"lbl_5")
        self.lbl_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbl_5, 1, 0, 1, 1)

        self.from_le = QLineEdit(Dialog)
        self.from_le.setObjectName(u"from_le")

        self.gridLayout.addWidget(self.from_le, 1, 1, 1, 1)

        self.to_le = QLineEdit(Dialog)
        self.to_le.setObjectName(u"to_le")

        self.gridLayout.addWidget(self.to_le, 2, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_10 = QLabel(Dialog)
        self.lbl_10.setObjectName(u"lbl_10")
        sizePolicy.setHeightForWidth(self.lbl_10.sizePolicy().hasHeightForWidth())
        self.lbl_10.setSizePolicy(sizePolicy)
        self.lbl_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_10)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.time_filtr_box = QComboBox(Dialog)
        self.time_filtr_box.setObjectName(u"time_filtr_box")
        sizePolicy.setHeightForWidth(self.time_filtr_box.sizePolicy().hasHeightForWidth())
        self.time_filtr_box.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.time_filtr_box, 0, 2, 1, 1)

        self.lbl_8 = QLabel(Dialog)
        self.lbl_8.setObjectName(u"lbl_8")
        self.lbl_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lbl_8, 2, 0, 1, 1)

        self.lbl_9 = QLabel(Dialog)
        self.lbl_9.setObjectName(u"lbl_9")
        self.lbl_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lbl_9, 1, 0, 1, 1)

        self.date_from_btn = QPushButton(Dialog)
        self.date_from_btn.setObjectName(u"date_from_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.date_from_btn.sizePolicy().hasHeightForWidth())
        self.date_from_btn.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.date_from_btn, 1, 2, 1, 1)

        self.lbl_7 = QLabel(Dialog)
        self.lbl_7.setObjectName(u"lbl_7")
        self.lbl_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lbl_7, 0, 0, 1, 1)

        self.dete_to_btn = QPushButton(Dialog)
        self.dete_to_btn.setObjectName(u"dete_to_btn")

        self.gridLayout_3.addWidget(self.dete_to_btn, 2, 2, 1, 1)

        self.from_lbl = QLabel(Dialog)
        self.from_lbl.setObjectName(u"from_lbl")

        self.gridLayout_3.addWidget(self.from_lbl, 1, 1, 1, 1)

        self.to_lbl = QLabel(Dialog)
        self.to_lbl.setObjectName(u"to_lbl")

        self.gridLayout_3.addWidget(self.to_lbl, 2, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.save_btn = QPushButton(Dialog)
        self.save_btn.setObjectName(u"save_btn")

        self.verticalLayout_3.addWidget(self.save_btn)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u0444\u0438\u043b\u044c\u0442\u0440\u0430", None))
        self.lbl_6.setText(QCoreApplication.translate("Dialog", u"\u0424\u0438\u043b\u044c\u0442\u0440 \u0441\u0443\u043c\u043c\u044b", None))
        self.lbl_3.setText(QCoreApplication.translate("Dialog", u"\u0422\u0438\u043f \u0444\u0438\u043b\u044c\u0442\u0440\u0430", None))
        self.lbl_4.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e", None))
        self.lbl_5.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442", None))
        self.lbl_10.setText(QCoreApplication.translate("Dialog", u"\u0424\u0438\u043b\u044c\u0442\u0440 \u0434\u0430\u0442\u044b", None))
        self.lbl_8.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e", None))
        self.lbl_9.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442", None))
        self.date_from_btn.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.lbl_7.setText(QCoreApplication.translate("Dialog", u"\u0422\u0438\u043f \u0444\u0438\u043b\u044c\u0442\u0440\u0430", None))
        self.dete_to_btn.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.from_lbl.setText(QCoreApplication.translate("Dialog", u" - ", None))
        self.to_lbl.setText(QCoreApplication.translate("Dialog", u" - ", None))
        self.save_btn.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi


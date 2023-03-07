# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_balance_dialog.ui'
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
        Dialog.resize(836, 172)
        Dialog.setStyleSheet(u"QWidget {\n"
"	color: white;\n"
"	background-color: qlineargradient(spread:reflect, x1:0.647, y1:0.483864, x2:0, y2:0.972, stop:0.298507 rgba(130, 0, 255, 255), stop:0.935323 rgba(255, 102, 102, 255));\n"
"	font: 75 12pt Rubik;\n"
"}\n"
"\n"
"QLabel {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"QLineEdit {\n"
"	font-size: 20pt;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"QComboBox {\n"
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
"}")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lbl_1 = QLabel(Dialog)
        self.lbl_1.setObjectName(u"lbl_1")
        self.lbl_1.setStyleSheet(u"background-color: rgba(255, 246, 247, 0);")

        self.gridLayout.addWidget(self.lbl_1, 0, 0, 1, 1)

        self.name_le = QLineEdit(Dialog)
        self.name_le.setObjectName(u"name_le")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_le.sizePolicy().hasHeightForWidth())
        self.name_le.setSizePolicy(sizePolicy)
        self.name_le.setStyleSheet(u"background-color: rgba(255, 246, 247, 0);")
        self.name_le.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.name_le, 0, 1, 1, 1)

        self.currency_box = QComboBox(Dialog)
        self.currency_box.setObjectName(u"currency_box")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.currency_box.sizePolicy().hasHeightForWidth())
        self.currency_box.setSizePolicy(sizePolicy1)
        self.currency_box.setStyleSheet(u"background-color: rgba(255, 246, 247, 0);")

        self.gridLayout.addWidget(self.currency_box, 1, 1, 1, 1)

        self.lbl_3 = QLabel(Dialog)
        self.lbl_3.setObjectName(u"lbl_3")
        self.lbl_3.setStyleSheet(u"background-color: rgba(255, 246, 247, 0);")

        self.gridLayout.addWidget(self.lbl_3, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.create_btn = QPushButton(Dialog)
        self.create_btn.setObjectName(u"create_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.create_btn.sizePolicy().hasHeightForWidth())
        self.create_btn.setSizePolicy(sizePolicy2)
        self.create_btn.setStyleSheet(u"border: none;")

        self.verticalLayout.addWidget(self.create_btn)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0443\u0447\u0435\u043d\u0438\u043a\u0430", None))
        self.lbl_1.setText(QCoreApplication.translate("Dialog", u"\u0418\u043c\u044f", None))
        self.lbl_3.setText(QCoreApplication.translate("Dialog", u"\u0414\u0435\u043d\u0435\u0436\u043d\u0430\u044f \u0435\u0434\u0435\u043d\u0438\u0446\u0430", None))
        self.create_btn.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'exception_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(691, 252)
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
        self.title_lbl = QLabel(Dialog)
        self.title_lbl.setObjectName(u"title_lbl")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_lbl.sizePolicy().hasHeightForWidth())
        self.title_lbl.setSizePolicy(sizePolicy)
        self.title_lbl.setStyleSheet(u"font-size: 18pt;")
        self.title_lbl.setWordWrap(True)

        self.verticalLayout.addWidget(self.title_lbl)

        self.msg_lbl = QLabel(Dialog)
        self.msg_lbl.setObjectName(u"msg_lbl")
        self.msg_lbl.setStyleSheet(u"font-size: 14pt;")
        self.msg_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.msg_lbl)

        self.close_btn = QPushButton(Dialog)
        self.close_btn.setObjectName(u"close_btn")

        self.verticalLayout.addWidget(self.close_btn)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.title_lbl.setText(QCoreApplication.translate("Dialog", u"\u041e\u0448\u0438\u0431\u043a\u0430!", None))
        self.msg_lbl.setText("")
        self.close_btn.setText(QCoreApplication.translate("Dialog", u"OK", None))
    # retranslateUi


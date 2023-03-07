# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'date_choose_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QDialog, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(669, 405)
        Dialog.setStyleSheet(u"QWidget {\n"
"	font: 75 16pt Rubik;\n"
"}\n"
"\n"
"QPushButton {\n"
"	font-size: 18pt;\n"
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
"QDialog {\n"
"	background-color: qlineargradient(spread:reflect, x1:0.647, y1:0.483864, x2:0, y2:0.972, stop:0.298507 rgba(130, 0, 255, 255), stop:0.935323 rgba(255, 102, 102, 255));\n"
"	font: 75 16pt Rubik;\n"
"}")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.calendar = QCalendarWidget(Dialog)
        self.calendar.setObjectName(u"calendar")

        self.verticalLayout.addWidget(self.calendar)

        self.choose_btn = QPushButton(Dialog)
        self.choose_btn.setObjectName(u"choose_btn")
        self.choose_btn.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0.647, y1:0.483864, x2:0, y2:0.972, stop:0.298507 rgba(130, 0, 255, 255), stop:0.935323 rgba(255, 102, 102, 255));")

        self.verticalLayout.addWidget(self.choose_btn)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.choose_btn.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
    # retranslateUi


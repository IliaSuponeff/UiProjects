# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'change_trans_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(897, 408)
        Dialog.setStyleSheet(u"QWidget {\n"
"	color: white;\n"
"	background-color: qlineargradient(spread:reflect, x1:0.647, y1:0.483864, x2:0, y2:0.972, stop:0.298507 rgba(130, 0, 255, 255), stop:0.935323 rgba(255, 102, 102, 255));\n"
"	font: 75 16pt Rubik;\n"
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
"QDoubleSpinBox {\n"
"	color: black;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"QComboBox {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"QPushButton {\n"
"	font-size: 18pt;\n"
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
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.sum_le = QLineEdit(Dialog)
        self.sum_le.setObjectName(u"sum_le")
        self.sum_le.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.sum_le, 0, 4, 1, 1)

        self.lbl_2 = QLabel(Dialog)
        self.lbl_2.setObjectName(u"lbl_2")
        self.lbl_2.setAlignment(Qt.AlignCenter)
        self.lbl_2.setMargin(15)

        self.gridLayout.addWidget(self.lbl_2, 0, 2, 1, 1)

        self.lbl_4 = QLabel(Dialog)
        self.lbl_4.setObjectName(u"lbl_4")
        self.lbl_4.setAlignment(Qt.AlignCenter)
        self.lbl_4.setMargin(15)

        self.gridLayout.addWidget(self.lbl_4, 1, 2, 1, 1)

        self.date_choose_btn = QPushButton(Dialog)
        self.date_choose_btn.setObjectName(u"date_choose_btn")

        self.gridLayout.addWidget(self.date_choose_btn, 1, 4, 1, 1)

        self.date_lbl = QLabel(Dialog)
        self.date_lbl.setObjectName(u"date_lbl")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.date_lbl.sizePolicy().hasHeightForWidth())
        self.date_lbl.setSizePolicy(sizePolicy)
        self.date_lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.date_lbl, 1, 3, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_3 = QLabel(Dialog)
        self.lbl_3.setObjectName(u"lbl_3")
        self.lbl_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_3)

        self.info_le = QTextEdit(Dialog)
        self.info_le.setObjectName(u"info_le")
        self.info_le.setStyleSheet(u"background-color: rgba(0,0,0, 50);")

        self.verticalLayout.addWidget(self.info_le)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.safe_btn = QPushButton(Dialog)
        self.safe_btn.setObjectName(u"safe_btn")

        self.verticalLayout_2.addWidget(self.safe_btn)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u043f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u0438", None))
        self.lbl_2.setText(QCoreApplication.translate("Dialog", u"\u0426\u0435\u043d\u0430 \u0443\u0440\u043e\u043a\u0430", None))
        self.lbl_4.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u0442\u0430 \u0443\u0440\u043e\u043a\u0430", None))
        self.date_choose_btn.setText(QCoreApplication.translate("Dialog", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.date_lbl.setText("")
        self.lbl_3.setText(QCoreApplication.translate("Dialog", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
        self.info_le.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Rubik'; font-size:16pt; font-weight:72; font-style:normal;\">\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.safe_btn.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0437\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi


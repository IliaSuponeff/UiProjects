# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'balancer_main.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 800)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1200, 800))
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget {\n"
"	color: white;\n"
"	background-color: qlineargradient(spread:reflect, x1:0.647, y1:0.483864, x2:0, y2:0.972, stop:0.298507 rgba(130, 0, 255, 255), stop:0.935323 rgba(255, 102, 102, 255));\n"
"	font: 75 12pt \"Rubik\";\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"QLabel {\n"
"	background-color: rgba(255, 255, 255, 0);	\n"
"}\n"
"\n"
"QComboBox {\n"
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
"	font-size: 16pt;\n"
"}\n"
"\n"
"QTableView::item {\n"
"    border-style: none;\n"
""
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
        self.horizontalLayout_4 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.balance_widget = QWidget(self.centralwidget)
        self.balance_widget.setObjectName(u"balance_widget")
        self.verticalLayout = QVBoxLayout(self.balance_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.balance_info_lbl = QLabel(self.balance_widget)
        self.balance_info_lbl.setObjectName(u"balance_info_lbl")
        self.balance_info_lbl.setStyleSheet(u"font-size: 15pt;\n"
"background-color: rgba(255, 255, 255, 0);")
        self.balance_info_lbl.setAlignment(Qt.AlignCenter)
        self.balance_info_lbl.setWordWrap(True)

        self.verticalLayout.addWidget(self.balance_info_lbl)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.prev_btn = QPushButton(self.balance_widget)
        self.prev_btn.setObjectName(u"prev_btn")
        self.prev_btn.setStyleSheet(u"border: none;")

        self.gridLayout.addWidget(self.prev_btn, 0, 0, 1, 1)

        self.add_account_btn = QPushButton(self.balance_widget)
        self.add_account_btn.setObjectName(u"add_account_btn")
        self.add_account_btn.setStyleSheet(u"border: none;")

        self.gridLayout.addWidget(self.add_account_btn, 2, 0, 1, 1)

        self.next_btn = QPushButton(self.balance_widget)
        self.next_btn.setObjectName(u"next_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.next_btn.sizePolicy().hasHeightForWidth())
        self.next_btn.setSizePolicy(sizePolicy1)
        self.next_btn.setStyleSheet(u"border: none;")

        self.gridLayout.addWidget(self.next_btn, 0, 1, 1, 1)

        self.del_account_btn = QPushButton(self.balance_widget)
        self.del_account_btn.setObjectName(u"del_account_btn")
        self.del_account_btn.setStyleSheet(u"border: none;")

        self.gridLayout.addWidget(self.del_account_btn, 2, 1, 1, 1)

        self.student_box = QComboBox(self.balance_widget)
        self.student_box.setObjectName(u"student_box")
        sizePolicy2 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.student_box.sizePolicy().hasHeightForWidth())
        self.student_box.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.student_box, 3, 1, 1, 1)

        self.fast_choose_btn = QPushButton(self.balance_widget)
        self.fast_choose_btn.setObjectName(u"fast_choose_btn")

        self.gridLayout.addWidget(self.fast_choose_btn, 3, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.lbl_1 = QLabel(self.balance_widget)
        self.lbl_1.setObjectName(u"lbl_1")
        self.lbl_1.setStyleSheet(u"font-size: 20pt;\n"
"background-color: rgba(255, 255, 255, 0);")

        self.verticalLayout.addWidget(self.lbl_1)

        self.balance_lbl = QLabel(self.balance_widget)
        self.balance_lbl.setObjectName(u"balance_lbl")
        self.balance_lbl.setStyleSheet(u"font-size: 26pt;\n"
"background-color: rgba(255, 255, 255, 0);")

        self.verticalLayout.addWidget(self.balance_lbl)

        self.results_table = QTableView(self.balance_widget)
        self.results_table.setObjectName(u"results_table")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.results_table.sizePolicy().hasHeightForWidth())
        self.results_table.setSizePolicy(sizePolicy3)
        self.results_table.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.results_table)

        self.create_results = QPushButton(self.balance_widget)
        self.create_results.setObjectName(u"create_results")

        self.verticalLayout.addWidget(self.create_results)


        self.horizontalLayout.addWidget(self.balance_widget)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.filter_settings_btn = QPushButton(self.centralwidget)
        self.filter_settings_btn.setObjectName(u"filter_settings_btn")
        sizePolicy1.setHeightForWidth(self.filter_settings_btn.sizePolicy().hasHeightForWidth())
        self.filter_settings_btn.setSizePolicy(sizePolicy1)
        self.filter_settings_btn.setStyleSheet(u"border: none;")

        self.gridLayout_2.addWidget(self.filter_settings_btn, 0, 1, 1, 1)

        self.add_trans_btn = QPushButton(self.centralwidget)
        self.add_trans_btn.setObjectName(u"add_trans_btn")
        sizePolicy1.setHeightForWidth(self.add_trans_btn.sizePolicy().hasHeightForWidth())
        self.add_trans_btn.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.add_trans_btn, 0, 0, 1, 1)

        self.del_trans_btn = QPushButton(self.centralwidget)
        self.del_trans_btn.setObjectName(u"del_trans_btn")
        sizePolicy1.setHeightForWidth(self.del_trans_btn.sizePolicy().hasHeightForWidth())
        self.del_trans_btn.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.del_trans_btn, 1, 0, 1, 1)

        self.change_trans_btn = QPushButton(self.centralwidget)
        self.change_trans_btn.setObjectName(u"change_trans_btn")
        sizePolicy1.setHeightForWidth(self.change_trans_btn.sizePolicy().hasHeightForWidth())
        self.change_trans_btn.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.change_trans_btn, 1, 1, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_2)

        self.balance_manager_table = QTableView(self.centralwidget)
        self.balance_manager_table.setObjectName(u"balance_manager_table")
        self.balance_manager_table.setGridStyle(Qt.DashLine)

        self.verticalLayout_4.addWidget(self.balance_manager_table)


        self.horizontalLayout_4.addLayout(self.verticalLayout_4)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"StudentManager", None))
        self.balance_info_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0447\u0435\u043d\u0438\u043a: -", None))
        self.prev_btn.setText(QCoreApplication.translate("MainWindow", u"\n"
"<\n"
"", None))
        self.add_account_btn.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \n"
" \u0423\u0447\u0435\u043d\u0438\u043a\u0430", None))
        self.next_btn.setText(QCoreApplication.translate("MainWindow", u"\n"
">\n"
"", None))
        self.del_account_btn.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \n"
" \u0423\u0447\u0435\u043d\u0438\u043a\u0430", None))
        self.fast_choose_btn.setText(QCoreApplication.translate("MainWindow", u" \u0412\u044b\u0431\u0440\u0430\u0442\u044c \n"
" \u0443\u0447\u0435\u043d\u0438\u043a\u0430 ", None))
        self.lbl_1.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0440\u0430\u0431\u043e\u0442\u043e\u043a", None))
        self.balance_lbl.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.create_results.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043e\u0442\u0447\u0451\u0442", None))
        self.filter_settings_btn.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0444\u0438\u043b\u044c\u0442\u0440 \u0434\u043b\u044f \u0442\u0430\u0431\u043b\u0438\u0446\u044b", None))
        self.add_trans_btn.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u0435", None))
        self.del_trans_btn.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u0435", None))
        self.change_trans_btn.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u0435", None))
    # retranslateUi


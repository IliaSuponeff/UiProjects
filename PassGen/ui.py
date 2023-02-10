from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
                               QHBoxLayout, QLabel, QLineEdit, QMainWindow,
                               QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import resources


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 350)
        icon = QIcon()
        icon.addFile(u":/icons/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QSize(50, 50))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(400, 350))
        self.centralwidget.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.length_label = QLabel(self.centralwidget)
        self.length_label.setObjectName(u"label")
        self.length_label.setStyleSheet(u"background-color: rgb(198, 68, 59);\n"
                                        "font: 13pt \"Rubik\";")
        self.length_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.length_label)

        self.combo_box = QComboBox(self.centralwidget)
        self.combo_box.setObjectName(u"comboBox")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_box.sizePolicy().hasHeightForWidth())
        self.combo_box.setSizePolicy(sizePolicy)
        self.combo_box.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.combo_box.setEditable(False)
        self.combo_box.setInsertPolicy(QComboBox.InsertAfterCurrent)

        self.horizontalLayout.addWidget(self.combo_box)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.label_help = QLabel(self.centralwidget)
        self.label_help.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_help.sizePolicy().hasHeightForWidth())
        self.label_help.setSizePolicy(sizePolicy)
        self.label_help.setStyleSheet(u"background-color: rgb(198, 68, 59);\n"
                                   "font: 13pt \"Rubik\";")
        self.label_help.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_help)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.simbols_2_box = QCheckBox(self.centralwidget)
        self.simbols_2_box.setObjectName(u"checkBox_8")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.simbols_2_box.sizePolicy().hasHeightForWidth())
        self.simbols_2_box.setSizePolicy(sizePolicy1)
        self.simbols_2_box.setAutoFillBackground(False)
        self.simbols_2_box.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(198, 68, 59);\n"
                                      "font: 9pt \"Rubik\";")

        self.gridLayout.addWidget(self.simbols_2_box, 4, 1, 1, 1)

        self.simbols_1_box = QCheckBox(self.centralwidget)
        self.simbols_1_box.setObjectName(u"checkBox_7")
        sizePolicy1.setHeightForWidth(self.simbols_1_box.sizePolicy().hasHeightForWidth())
        self.simbols_1_box.setSizePolicy(sizePolicy1)
        self.simbols_1_box.setAutoFillBackground(False)
        self.simbols_1_box.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(198, 68, 59);\n"
                                      "font: 9pt \"Rubik\";")

        self.gridLayout.addWidget(self.simbols_1_box, 4, 0, 1, 1)

        self.verticalLayout_2.addLayout(self.gridLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy2)
        self.pushButton.setStyleSheet(u"background-color: rgb(198, 68, 59);\n"
                                      "font: 20pt \"Rubik\";")
        self.pushButton.setAutoDefault(False)
        self.pushButton.setFlat(False)

        self.verticalLayout.addWidget(self.pushButton)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"background-color: rgb(198, 68, 59);\n"
                                    "font: 18pt \"Rubik\";")
        self.lineEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.lineEdit)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pushButton.setDefault(False)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PasswordGenerator", None))
        self.length_label.setText(QCoreApplication.translate("MainWindow",
                                                             u"\u0412\u044b\u0431\u0435\u0440\u0435\u0442\u0435 \u0434\u043b\u0438\u043d\u0443\n"
                                                             "\u043f\u0430\u0440\u043e\u043b\u044f", None))
        self.combo_box.setCurrentText("")
        self.label_help.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0433\u0435\u043d\u0435\u0440\u0430\u0442\u043e\u0440\u0430",
                                                           None))
        self.simbols_2_box.setText(
            QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043c\u0432\u043e\u043b\u044b [@#$%&<>*?]", None))
        self.simbols_1_box.setText(
            QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043c\u0432\u043e\u043b\u044b [_!-+=/|\\*?]", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow",
                                                           u"\u0421\u0433\u0435\u043d\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c",
                                                           None))
        # if QT_CONFIG(shortcut)
        self.pushButton.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
        # endif // QT_CONFIG(shortcut)
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"PassGen", None))
    # retranslateUi
